# Network Fundamentals

## TCP/IP layers

* Transmission Control Protocol / Internet Protocol
* Layer summary:
```
+------------------------------+
| Application Layer            |
| HTTP, HTTPS, DNS, SSH, TLS   |
+------------------------------+
| Transport Layer              |
| TCP, UDP                     |
+------------------------------+
| Internet Layer               |
| IPv4, IPv6, ICMP             |
+------------------------------+
| Link Layer                   |
| Ethernet, Wi-Fi, ARP, MAC    |
+------------------------------+
| Physical Layer               |
| Cable, Fibre, Radio Signals  |
+------------------------------+
```

## Network interfaces
* A network interface is a kernel-managed communication endpoint (struct net_device) through which packets enter or leave the Linux networking stack.
It connects the networking stack to a communication medium, which can be physical (Ethernet, Wi-Fi) or virtual (loopback, veth, bridge, tunnel).
* Flow of data in host:

```
                   User Space
+--------------------------------------+
| curl, nginx, browser, kubectl        |
+--------------------------------------+
               |
               | System Calls
               v
+--------------------------------------+
|      Linux Networking Stack          |
| IP, TCP, UDP, Routing, ARP           |
+--------------------------------------+
               |
               | Network Interface
               | (struct net_device)
               v
+--------------------------------------+
| Driver / Virtual Interface           |
+--------------------------------------+
               |
               v
 Physical NIC | Loopback | veth | Tunnel
```
* Examples of interfaces:
  * eth0 (Ethernet),
  * wlan0 (Wi-Fi),
  * lo (loopback),
  * veth (container networking),
  * wg0 (WireGuard),
* Describing interface status:
  * `ip addr` and `ip link`
  * UP -> Interface is enabled by user.
  * LOWER_UP -> The underlying physical or virtual link is operational and ready
  to carry packets to the directly connected peer.
  * scope -> Defines the validity of an IP address from the Linux kernel's perspective.
    * values: host, link , global
    * link: Only valid in layer 2(data link layer, eth, wifi)

## IPv4
* ipv4 is 32 bit address(8*4).
* CIDR notation: 126.90.100.23/12
  * First 12 bits are for network and remaining 20 bits are for devices.
* Private IPs range:
  * 10.0.0.0/8
  * 172.16.0.0/12
  * 192.168.0.0/16
* Loopback: 127.0.0.0/8 (packets never leaves the linux network stack)
* local link: 169.254.0.0/16
  * Assigned when DHCP fails or no static IP exists.
  * When two laptops connedted via ethernet. OS assigns IPs.
  * Only valid for layer 2 link. Packets with local link ips are never routed outside.
    They are routed to same layer 2 link.**
* IP is routed.
* IP packet are same throughout(sourceIP and destinationIP).

## Ethernet:
* Layer 2 protocol.
* Here addresses are MAC (48 bits = 24(manufacturer identifier) + 24(device))
* Data moves in ethernet frames.
* Ethernet provides communication on the local network (the local Layer 2 link).
* Packet flow:
```
Application │  TCP │  IP Packet │  Ethernet Frame │  Network Interface │ Local Network
```
* Communication types:
  * Unicast → One sender → One receiver.
  * Broadcast → One sender → All devices on the same Layer 2 link.
  * Multicast → One sender → A selected group of receivers.
* Important mac address:
  * Broadcast address: FF:FF:FF:FF:FF:FF
* Ethernet frames never travel through routers.
* Routers remove the incoming Ethernet frame and create a 
new Ethernet frame for the next link.
* Frames are switched.
* Frames are recreated every hop.

## Router/Switch
* Switch → Local delivery using MAC addresses.
* Router → Inter-network delivery using IP addresses.
* Wifi has -> Switch + Router + Wireless AP.

## ARP:
* Address resolution protocol.
* Flow:
```
Application
      │
      ▼
Need to send to 192.168.18.90
      │
      ▼
ARP Cache Lookup
      │
      ▼
MAC not found
      │
      ▼
Ethernet Broadcast
Dst MAC = FF:FF:FF:FF:FF:FF
      │
      ▼
"Who has 192.168.18.90?"
      │
      ▼
Server replies
"I am 192.168.18.90"
MAC = BB:BB:BB:BB:BB:BB
      │
      ▼
Linux updates ARP cache
      │
      ▼
Build Ethernet frame
Dst MAC = BB:BB:BB:BB:BB:BB
      │
      ▼
Send IP packet
```

## Routing
* IP identifies the final destination. Ethernet identifies the next hop on the local link.
* If linux find packets destination is not in local network.
* It sends the packet to router(default gateway).
  * If MAC is known from ARP cache it creates frame and send it to router via nic and switch.
  * Else it gets MAC via ARP and updates the cache.
* imp command: `ip route`
* Routing table answers:
  * Where should I send this packet?
  1. Which interface?
  2. Which next hop?
  * Gateway route: `default via 192.168.18.1 dev eth0`
  * Direct connected route: `192.168.18.0/24 dev eth0`
  * Longest Prefix Match: Linux always chooses the most specific matching route over default.
    The largest prefix length wins -> Network
    ```
    Routing table:
    10.0.0.0/8        dev eth0
    10.42.0.0/16      dev eth1
    10.42.0.0/24      dev eth2
    default           via 192.168.18.1

    Destination:
    10.42.0.15

    Route 1: Prefix match: 8
    Route 2: Prefix match: 16
    Route 3: Prefix match: 24 <--- selecte route
    Route 4: Matches all
    ```
  * Routing decision:
  ```
  1. Find all matching routes
        │
        ▼
  2. Choose the most specific route
    (Longest Prefix Match)
          │
          ▼
  3. If multiple routes are equally specific,
    compare metrics
          │
          ▼
  4. Lowest metric wins
  ```
  * Example table:
  ```
  default via 192.168.18.1 dev eth0 proto static
  default via 192.168.18.1 dev eth0 proto dhcp metric 100
  default via 192.168.18.1 dev wlan0 proto dhcp metric 600
  10.42.0.0/24 dev cni0 proto kernel scope link src 10.42.0.1
  10.89.1.0/24 dev podman2 proto kernel scope link src 10.89.1.1
  192.168.18.0/24 dev eth0 proto kernel scope link src 192.168.18.72
  192.168.18.0/24 dev wlan0 proto kernel scope link src 192.168.18.25 metric 600
  192.168.18.1 dev eth0 proto dhcp scope link src 192.168.18.26 metric 100
  192.168.18.1 dev wlan0 proto dhcp scope link src 192.168.18.25 metric 600
  ```
  * Source Address Selection: scr ip addressed to be used during sending via a interface.
  * dev -> device.

## DNS:
* Domain naming system.
* URL -> IP

## ip neigh

* Purpose:
  * Shows the kernel's Neighbor Cache (ARP Cache for IPv4).

* Contains:
  - Neighbor IP
  - Interface
  - Neighbor MAC
  - Entry State

* Flow:
  ```
    Need MAC
        │
    ARP Request
        │
    ARP Reply
        │
    Neighbor Cache Updated
        │
    ip neigh
  ```
