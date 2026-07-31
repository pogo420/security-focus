# DevSecOps & Application Security - Learning Journey

> Learn from first principles. Do not skip fundamentals.

---

## Week 1 - Networking Fundamentals

### Linux Networking Foundations

- [x] Linux Networking Architecture
- [x] User Space → Kernel → Network Interface → Driver → Device
- [x] Network Interface
- [x] `struct net_device`
- [x] Physical vs Virtual Interfaces
- [x] Interface Naming
- [x] `ip link`
- [x] Interface States
  - [x] UP
  - [x] LOWER_UP

### IP Addressing

- [x] `ip addr`
- [x] IP addresses belong to Interfaces
- [x] Multiple IP addresses on an Interface
- [x] `scope`
- [x] `dynamic`
- [x] `secondary`
- [x] What is an IPv4 Address?
- [x] 32-bit Address
- [x] Binary Representation
- [x] CIDR
- [x] Prefix Length
- [x] Subnet Mask
- [x] Network Address
- [x] Host Address
- [x] Broadcast Address
- [x] Loopback Address
- [x] Private vs Public IP
- [x] Link-local Address

### Ethernet

- [x] Ethernet Frame
- [x] MAC Address
- [x] OUI
- [x] Unicast
- [x] Broadcast
- [x] Multicast
- [x] Switch

### ARP

- [x] Why ARP Exists
- [x] ARP Request
- [x] ARP Reply
- [x] ARP Cache
- [x] Gratuitous ARP
- [x] `ip neigh`

### Routing

- [x] Routing Table
- [x] Connected Routes
- [x] Default Route
- [x] Longest Prefix Match
- [x] Route Metric
- [x] Source Address Selection
- [x] `ip route`

### DNS Basics

- [x] Why DNS Exists
- [x] DNS Resolution
- [ ] `dig`
- [ ] `host`
- [ ] `nslookup`

### End-to-End Packet Journey

- [x] Trace `curl https://example.com`
- [x] DNS
- [x] Route Lookup
- [x] ARP
- [x] Ethernet Frame
- [x] Packet Transmission
- [x] Switch
- [x] Router
- [x] Destination Host

---

## Week 2 - TCP

- [x] TCP Header
- [x] Ports
- [x] Three-Way Handshake
- [x] Connection States
- [x] Retransmissions
- [x] Flow Control
- [ ] Congestion Control
- [ ] `ss`
- [ ] `netstat`
- [ ] Wireshark

---

## Week 3 - HTTP & HTTPS

- [ ] HTTP
- [ ] HTTP Headers
- [ ] Cookies
- [ ] Sessions
- [ ] Status Codes
- [ ] TLS
- [ ] Certificates
- [ ] TLS Handshake
- [ ] `curl`
- [ ] Browser DevTools
- [ ] `openssl s_client`

---

## Week 4 - DNS Deep Dive

- [ ] Recursive Resolver
- [ ] Root Server
- [ ] TLD
- [ ] Authoritative DNS
- [ ] A Record
- [ ] AAAA Record
- [ ] CNAME
- [ ] MX
- [ ] TXT
- [ ] TTL

---

## Week 5 - Docker Networking

- [ ] Linux Namespaces
- [ ] Network Namespace
- [ ] veth Pair
- [ ] Linux Bridge
- [ ] NAT
- [ ] Port Mapping
- [ ] Container DNS

---

## Week 6 - Kubernetes Networking

- [ ] Pod Network
- [ ] CNI
- [ ] Service
- [ ] ClusterIP
- [ ] NodePort
- [ ] LoadBalancer
- [ ] Ingress
- [ ] CoreDNS
- [ ] kube-proxy
- [ ] Flannel

---

## Week 7 - Reverse Proxy

- [ ] Reverse Proxy
- [ ] Forward Proxy
- [ ] Nginx
- [ ] Load Balancing
- [ ] Health Checks
- [ ] Sticky Sessions

---

## Week 8 - Authentication & Authorization

- [ ] Basic Auth
- [ ] Cookies
- [ ] Sessions
- [ ] JWT
- [ ] OAuth2
- [ ] OpenID Connect
- [ ] RBAC

---

## Week 9 - Application Security

- [ ] OWASP Top 10
- [ ] SQL Injection
- [ ] XSS
- [ ] CSRF
- [ ] SSRF
- [ ] IDOR
- [ ] Command Injection
- [ ] Path Traversal
- [ ] PortSwigger Labs

---

## Week 10 - Secure Coding

- [ ] Input Validation
- [ ] Output Encoding
- [ ] Password Hashing
- [ ] Secrets Management
- [ ] Dependency Security

---

## Week 11 - Container Security

- [ ] Image Layers
- [ ] Image Hardening
- [ ] Distroless Images
- [ ] Non-root Containers
- [ ] Linux Capabilities
- [ ] Seccomp
- [ ] AppArmor
- [ ] Trivy
- [ ] Grype
- [ ] Docker Scout

---

## Week 12 - Kubernetes Security

- [ ] RBAC
- [ ] Service Accounts
- [ ] Security Context
- [ ] Pod Security Standards
- [ ] Network Policies
- [ ] Secrets
- [ ] Kubescape
- [ ] kube-bench
- [ ] Falco

---

## Week 13 - DevSecOps

- [ ] SAST
- [ ] Semgrep
- [ ] Dependency Scanning
- [ ] SBOM
- [ ] Syft
- [ ] Cosign
- [ ] Image Signing
- [ ] GitHub Actions
- [ ] Jenkins

---

## Final Project

- [ ] FastAPI
- [ ] Angular
- [ ] PostgreSQL
- [ ] Docker / Podman
- [ ] K3s
- [ ] Nginx
- [ ] GitHub Actions
- [ ] Trivy
- [ ] Syft
- [ ] Cosign
- [ ] Falco
- [ ] Kubescape
- [ ] RBAC
- [ ] Network Policies
- [ ] TLS
- [ ] Monitoring
