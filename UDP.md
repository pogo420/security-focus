# UDP (User Datagram Protocol)

Purpose:
- Fast, lightweight transport protocol.

Characteristics:
- Connectionless
- No handshake
- No ACKs
- No retransmissions
- No sequencing
- No flow control

Uses:
- DNS
- Video streaming
- Voice calls
- Online gaming

Advantage:
- Low latency
- Low overhead

Disadvantage:
- No reliability guarantees.

Important:
- DNS queris are cheap; if lost we can ask again.
- UDP itself does not provide reliability. Application can do a workaround.
