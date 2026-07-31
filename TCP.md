# TCP

* Transmission control protocol.
* A reliable, connection-oriented transport protocol.
* Here identifier is port.
* Its layer 4.
* Summarizing identifiers:

## Layers

| Layer    | Identifies                  |
| -------- | --------------------------- |
| Ethernet | **Network interface (MAC)** |
| IP       | **Network + Host**          |
| TCP/UDP  | **Application (Port)**      |

## Summary of IPs

```
IP is the pivot of the networking stack.

Below IP:
    Deliver packets across links.

Above IP:
    Deliver data to the correct application.

Routers usually process only up to the IP layer.
Destination hosts continue up to the application layer.
```
* Last ROuter will have entry of destination IP network

## Ports

Purpose:
- IP identifies the destination host.
- Port identifies the destination application/service on that host.

Addressing:
IP Address      → Which host?
Port Number     → Which application?

```
Example:
192.168.18.72:22
│              │
│              └── SSH service
└───────────────── Destination host
```
Port Size:
- 16 bits
- Range: 0 - 65535

Port Categories:
- 0 - 1023     → Well-known ports
- 1024 - 49151 → Registered ports
- 49152 - 65535 → Dynamic/Ephemeral ports

Common Ports:
- 22   → SSH
- 53   → DNS
- 80   → HTTP
- 443  → HTTPS

Ephemeral Ports:
- Chosen automatically by the OS for client connections.
- Usually temporary.

Example:
```
Browser:
192.168.18.72:52341
        │
        ▼
142.250.x.x:443

52341 → Client (ephemeral)
443   → Server (well-known)
```

TCP/UDP Header:
- Source Port
- Destination Port

```
Connection Identity (4-Tuple):
Source IP
Source Port
Destination IP
Destination Port
```

Key Points:
- Ports belong to the Transport Layer (TCP/UDP).
- Ports are stored in the TCP/UDP header, not the IP header.
- Multiple applications can share one IP because they use different ports.

## Socket

Port:
- Identifies a service/application.

Socket:
- Kernel communication endpoint used by an application to send and receive network data.

```
    High-Level Flow:

    Application
        ↕
    Socket
        ↕
    Transport Layer (TCP/UDP)
        ↕
    IP
        ↕
    Ethernet
        ↕
    Network Interface
        ↕
    Driver
        ↕
    NIC
```

## TCP handshake:

* Handshake:

```
SYN → "Can we connect?"
SYN+ACK → "Yes, I'm ready."
ACK → "Great, let's communicate."
```
* Post handshake connection is established.
* A TCP segment examaple:
    ```
    +-----------------------------------+
    | Sequence Number = 1000            |
    | ACK Number = ...                  |
    | Flags = ACK                       |
    | Window Size = ...                 |
    | ... other TCP header fields ...   |
    +-----------------------------------+
    |                                   |
    |      100 bytes of Application     |
    |              Data                 |
    |                                   |
    +-----------------------------------+
    ```
* Data transfer with sequence:

    ```
    Client                                      Server
    ------                                      ------

    Seq = 0
    Len = 100
    (Bytes 0-99)
    ------------------------------->

                            ACK = 100
            (Received 0-99, next expected 100)

    ------------------------------------------------------

    Seq = 100
    Len = 100
    (Bytes 100-199)
    ------------------------------->

                            ACK = 200
            (Received 100-199, next expected 200)

    ------------------------------------------------------

    Seq = 200
    Len = 100
    (Bytes 200-299)
    ------------------------------->

                            ACK = 300
            (Received 200-299, next expected 300)
    ```

* Packet loss case:

    ```
    Client                                      Server
    ------                                      ------

    Seq = 0
    Len = 100
    (Bytes 0-99)
    ------------------------------->

                            ACK = 100

    ------------------------------------------------------

    Seq = 100
    Len = 100
    (Bytes 100-199)
    ------------------------------->

                    ✗ Packet Lost

    ------------------------------------------------------

    Seq = 200
    Len = 100
    (Bytes 200-299)
    ------------------------------->

                            ACK = 100
        (Still waiting for byte 100)

    ------------------------------------------------------

    Seq = 300
    Len = 100
    (Bytes 300-399)
    ------------------------------->

                            ACK = 100
        (Still waiting for byte 100)
    ```
* Quick summary:
    ```
    Sequence Number
    ---------------
    First byte contained in this TCP segment.

    ACK Number
    ----------
    Next byte expected by the receiver.

    Rule:
    ACK = Sequence Number + Payload Length
    (Only when all previous bytes have been received in order.)
    ```
* Retransmit case:
    - Network may lose TCP segments.

    - Sender:
        - Detects loss using:
            - Retransmission timeout (RTO)
            - Duplicate ACKs
    - Flow:

    ```
    Client                                   Server
    ------                                   ------

    Seq=0
    Len=100
    ------------------------------->

                        ACK=100

    -----------------------------------------------

    Seq=100
    Len=100
    ------------------------------->

                    ✗ Lost

    -----------------------------------------------

    Seq=200
    Len=100
    ------------------------------->

                        ACK=100

    -----------------------------------------------

    Retransmit

    Seq=100
    Len=100
    ------------------------------->

                        ACK=300
    ```


## TCP Flow Control

Purpose:
- Prevent a fast sender from overwhelming a slow receiver.

Receive Window:
- Advertised by the receiver.
- Indicates how much additional data the receiver can currently accept.

Sender:
- Limits unacknowledged data to the advertised window.
- Sends more data as ACKs arrive and the window opens.

ACK:
- Tells what has been received.

Window:
- Tells how much more can be received.

Key Point:
- Flow Control protects the receiver, not the network.

Flow:

```
Client (Sender)                           Server (Receiver)
---------------                           -----------------

Window = 300

Seq=0   Len=100  ------------------------>

Seq=100 Len=100  ------------------------>

Seq=200 Len=100  ------------------------>

          (300 bytes outstanding)
          Sender stops sending.

                        ACK=300
                        Window=200
<----------------------------------------

Sender can now send:

Seq=300 Len=100  ------------------------>

Seq=400 Len=100  ------------------------>
```

## TCP Connection Termination

Purpose:
- Gracefully close a TCP connection.

Steps:

1. FIN
   "I have finished sending."

2. ACK
   "I received your FIN."

3. FIN
   "I have also finished sending."

4. ACK
   "I received your FIN."

Key Points:
- TCP is full-duplex.
- Each direction closes independently.
- Client usually enters TIME_WAIT before fully closing.

## Listening vs Established Socket:

* Sumarizing:

```
                    INCOMING PACKET
                          │
                          ▼
                Network Interface
                          │
                          ▼
                     IP Layer
                          │
                          ▼
                    TCP Layer
                          │
                 ┌────────┴────────┐
                 │                 │
              New SYN?          Existing
                 │              connection?
                 │                 │
                YES               YES
                 │                 │
                 ▼                 ▼
          LISTENING SOCKET    Connection Lookup
             :443                  │
                 │                 ▼
          TCP Handshake       Connected Socket
                 │                 │
                 ▼                 ▼
      Kernel creates NEW       Data delivered
      Connected Socket         to this socket
                 │
                 ▼
            accept()
                 │
                 ▼
          Application
          gets socket FD
                 │
                 ▼
          Data Transfer
```

* Listening socket → accepts new connections.
* Kernel creates connected socket → one per connection.
* accept() → gives that connected socket to the application.
* Established packets → kernel lookup → correct connected socket.
* Listening socket is not a funnel through which all packets pass.
Once a connection exists, its packets are delivered to its own connected socket.
