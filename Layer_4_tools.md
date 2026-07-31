# Linux `ss` — Quick Notes

## Basic Commands

```bash
ss -lntp
```

Shows **TCP listening sockets** and the process using them.

```text
-l → LISTEN
-n → Numeric IP/ports
-t → TCP
-p → Process/PID/FD
```

```bash
ss -ntp
```

Shows **established TCP connections** and the process using them.

---

## Reading `ss` Output

```text
State   Recv-Q   Send-Q   Local Address:Port   Peer Address:Port
ESTAB   0        0        A:A                  B:B
```

### Local Address:Port

The TCP endpoint belonging to the machine where `ss` is executed.

### Peer Address:Port

The other endpoint of the TCP connection.

```text
Local ↔ Peer
```

One `ESTAB` row represents the **whole bidirectional TCP connection**, not one packet direction.

---

## Recv-Q

Data received by the kernel/socket but **not yet consumed by the application**.

```text
Network
   ↓
TCP
   ↓
Recv-Q
   ↓
Application
```

A persistently high `Recv-Q` can indicate the application isn't reading fast enough.

---

## Send-Q

Data waiting to be sent/acknowledged on the connection.

```text
Application
   ↓
Send-Q
   ↓
TCP
   ↓
Network
```

A persistently high `Send-Q` can indicate the sender cannot drain data fast enough.

---

## File Descriptor (FD)

* FD = process-local numeric handle for an open kernel resource; it is not globally unique.
* The application accesses a socket through a **file descriptor**.
* accept() returns a file descriptor representing the newly connected socket.

```text
Client
  ↓
TCP connection
  ↓
Kernel socket
  ↓
File Descriptor
  ↓
Application process
```

Example:

```text
users:(("k3s-server",pid=1471,fd=334))
```

Means:

```text
Process = k3s-server
PID     = 1471
FD      = 334
Socket  = represented by FD 334
```

A high FD number does **not** mean that many network connections.

---

## Socket Lifecycle

```text
socket()
   ↓
bind()
   ↓
listen()
   ↓
LISTEN socket
   ↓
TCP connection
   ↓
Kernel creates connected socket
   ↓
accept()
   ↓
Application receives socket FD
   ↓
ESTABLISHED
   ↓
Data transfer
   ↓
Connection termination
```

### Core rule

> **Listening socket accepts new connections. Connected sockets carry data.**

---

## TCP Connection Identification

A TCP connection is identified by:

```text
Source IP
Source Port
Destination IP
Destination Port
```

Therefore many clients can connect to the same server port:

```text
Client A:50001 → Server:443
Client B:50002 → Server:443
Client C:50003 → Server:443
```

All can coexist as separate TCP connections.

---

## Most Important Mental Model

```text
                 Linux Kernel
                      │
                 TCP Stack
                      │
        ┌─────────────┴─────────────┐
        │                           │
    New connection             Existing connection
        │                           │
        ▼                           ▼
 Listening Socket             Socket Lookup
        │                           │
        ▼                           ▼
   accept()                  Connected Socket
                                    │
                                    ▼
                               Application
```

`ss` is essentially a **window into the kernel's socket/connection state**.


# TCP `tcpdump`

## Basics
* Usage: `tcpdump -i any -nn host host_ip`
* To get ip of a host use `dig hostname`

## Packet-by-Packet Reading

Example flow: `192.168.18.72:51306` → `172.217.24.174:80`

| Exact `tcpdump` line                                                                  | Explanation                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Flags [S], seq 487623976, win 64240, ... wscale 10`                                  | **SYN.** Client requests a TCP connection. Initial sequence number = `487623976`. Client advertises its initial receive window `64240` and negotiates window scaling `10`.                              |
| `Flags [S.], seq 2342531287, ack 487623977, win 65535, ... wscale 8`                  | **SYN + ACK.** Server accepts. Server's sequence starts at `2342531287`. `ACK 487623977` means it received the client's SYN and expects the next sequence number. Server advertises its receive window. |
| `Flags [.], ack 1, win 63, length 0`                                                  | **ACK.** Client acknowledges the server's SYN. `ACK 1` = next server sequence number expected is `1` (relative sequence numbers). No data.                                                              |
| `Flags [P.], seq 1:75, ack 1, win 63, length 74: HTTP: GET / HTTP/1.1`                | Client sends HTTP data. `seq 1:75` = sequence numbers `1–74`, therefore **74 bytes**. `ACK 1` = client expects server sequence `1` next. `WIN 63` = client's current advertised receive window.         |
| `Flags [.], ack 75, win 1050, length 0`                                               | Server acknowledges the client's data. `ACK 75` = received client sequence `1–74`, expects `75` next. `WIN 1050` = server's current advertised receive window.                                          |
| `Flags [P.], seq 1:774, ack 75, win 1050, length 773: HTTP/1.1 301 Moved Permanently` | Server sends HTTP response. `seq 1:774` = server sends sequence `1–773` (**773 bytes**). `ACK 75` = server expects client sequence `75` next. `WIN 1050` = server's current advertised receive window.  |
| `Flags [.], ack 774, win 63, length 0`                                                | Client acknowledges server data. `ACK 774` = received server sequence `1–773`, expects `774` next. `WIN 63` = client's current advertised receive window.                                               |
| `Flags [F.], seq 75, ack 774, win 63, length 0`                                       | **FIN + ACK.** Client has finished sending. `SEQ 75` is the next client sequence number; FIN consumes one sequence number.                                                                              |
| `Flags [F.], seq 774, ack 76, win 1050, length 0`                                     | **FIN + ACK.** Server has also finished sending. `SEQ 774` = server's next sequence number; FIN consumes it. `ACK 76` acknowledges the client's FIN.                                                    |
| `Flags [.], ack 775, win 63, length 0`                                                | Client acknowledges the server's FIN. `ACK 775` = server's FIN at sequence `774` has been acknowledged; next expected server sequence is `775`.                                                         |

## Core TCP Reading Rules

| Field       | Meaning                                                            |
| ----------- | ------------------------------------------------------------------ |
| `SEQ`       | Sequence number of the **first byte** carried by this TCP segment. |
| `seq 1:75`  | Carries sequence numbers `1–74`; therefore `74` bytes of data.     |
| `ACK 75`    | "I received through sequence `74`; I expect sequence `75` next."   |
| `WIN 1050`  | Current advertised receive window.                                 |
| `length 0`  | No TCP payload/application data.                                   |
| `length 74` | 74 bytes of TCP payload.                                           |
| `[S]`       | SYN — start connection.                                            |
| `[S.]`      | SYN + ACK.                                                         |
| `[.]`       | ACK.                                                               |
| `[P.]`      | PSH + ACK; TCP segment carries application data.                   |
| `[F.]`      | FIN + ACK; sender is finished sending.                             |

## The Mental Model

```text
SEQ  = what I am sending
ACK  = what I expect from you
WIN  = how much more I can currently receive
```

Each direction has its **own sequence-number space**:

```text
Client → Server
    SEQ: 1, 2, 3, ...

Server → Client
    SEQ: 1, 2, 3, ...
```

TCP is **byte-oriented**: sequence numbers advance according to the amount of TCP payload sent.

SYN and FIN each consume **one sequence number**, even though they carry no application payload.
