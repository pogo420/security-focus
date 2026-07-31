# DevSecOps & Application Security — Master Roadmap

## Phase 1 — Networking Foundations

### Linux Networking

* [x] Linux Networking Architecture
* [x] User Space → Kernel → Network Interface → Driver → Device
* [x] Network Interface
* [x] `struct net_device`
* [x] Physical vs Virtual Interfaces
* [x] Interface Naming
* [x] `ip link`
* [x] Interface States — UP / LOWER_UP

### IP Addressing

* [x] `ip addr`
* [x] IP addresses belong to Interfaces
* [x] Multiple IPs on Interface
* [x] `scope`
* [x] `dynamic`
* [x] `secondary`
* [x] IPv4
* [x] 32-bit Address
* [x] Binary Representation
* [x] CIDR
* [x] Prefix Length
* [x] Subnet Mask
* [x] Network Address
* [x] Host Address
* [x] Broadcast Address
* [x] Loopback
* [x] Private vs Public IP
* [x] Link-local Address

### Ethernet

* [x] Ethernet Frame
* [x] MAC Address
* [x] OUI
* [x] Unicast
* [x] Broadcast
* [x] Multicast
* [x] Switch

### ARP

* [x] Why ARP Exists
* [x] ARP Request
* [x] ARP Reply
* [x] ARP Cache
* [x] Gratuitous ARP
* [x] `ip neigh`

### Routing

* [x] Routing Table
* [x] Connected Routes
* [x] Default Route
* [x] Longest Prefix Match
* [x] Route Metric
* [x] Source Address Selection
* [x] `ip route`

### DNS Basics

* [x] Why DNS Exists
* [x] DNS Resolution
* [ ] `dig`
* [ ] `host`
* [ ] `nslookup`

### End-to-End Packet Journey

* [x] `curl https://example.com`
* [x] DNS
* [x] Route Lookup
* [x] ARP
* [x] Ethernet Frame
* [x] Packet Transmission
* [x] Switch
* [x] Router
* [x] Destination Host

---

## Phase 2 — TCP

* [x] TCP Header
* [x] Ports
* [x] Sockets
* [x] Listening Socket
* [x] Connected Socket
* [x] `socket()`
* [x] `bind()`
* [x] `listen()`
* [x] `accept()`
* [x] File Descriptors
* [x] Three-Way Handshake
* [x] Sequence Numbers
* [x] ACK
* [x] Retransmissions
* [x] Flow Control
* [x] Window
* [x] Congestion Control
* [x] Connection States
* [x] Connection Termination
* [x] `ss`
* [x] `netstat`
* [x] tcpdump
---

## Phase 3 — HTTP / HTTPS / TLS

* [ ] HTTP Request / Response
* [ ] HTTP Methods
* [ ] URL
* [ ] Headers
* [ ] Status Codes
* [ ] Cookies
* [ ] Sessions
* [ ] Keep-Alive
* [ ] HTTP/1.1
* [ ] HTTP/2 basics
* [ ] HTTP/3 / QUIC overview
* [ ] `curl`
* [ ] Browser DevTools
* [ ] TLS purpose
* [ ] TLS Handshake
* [ ] Certificates
* [ ] CA / Trust Chain
* [ ] Certificate validation
* [ ] SNI
* [ ] ALPN
* [ ] `openssl s_client`

---

## Phase 4 — Authentication & Authorization

* [ ] Authentication vs Authorization
* [ ] Basic Auth
* [ ] Cookies
* [ ] Sessions
* [ ] Session management
* [ ] Password authentication
* [ ] JWT
* [ ] OAuth2
* [ ] OpenID Connect
* [ ] RBAC
* [ ] Access control
* [ ] Token expiry / refresh
* [ ] Common authentication failures

---

## Phase 5 — Application Security

* [ ] OWASP Top 10
* [ ] SQL Injection
* [ ] XSS
* [ ] CSRF
* [ ] SSRF
* [ ] IDOR / Broken Access Control
* [ ] Command Injection
* [ ] Path Traversal
* [ ] File Upload vulnerabilities
* [ ] Security Misconfiguration
* [ ] Insecure Deserialization
* [ ] API Security
* [ ] Rate Limiting
* [ ] PortSwigger Labs

---

## Phase 6 — Secure Coding

* [ ] Input Validation
* [ ] Output Encoding
* [ ] Password Hashing
* [ ] Secrets Management
* [ ] Dependency Security
* [ ] Secure Error Handling
* [ ] Logging / Audit Logging
* [ ] Secure API Design
* [ ] Cryptography fundamentals
* [ ] Security testing

---

## Phase 7 — Docker / Container Fundamentals

* [ ] Container vs VM
* [ ] Images
* [ ] Layers
* [ ] Dockerfile
* [ ] Container lifecycle
* [ ] Registry
* [ ] Linux Namespaces
* [ ] Network Namespace
* [ ] PID Namespace
* [ ] Mount Namespace
* [ ] veth Pair
* [ ] Linux Bridge
* [ ] NAT
* [ ] Port Mapping
* [ ] Container DNS
* [ ] Container ↔ Host Networking

---

## Phase 8 — Docker Security

* [ ] Image Hardening
* [ ] Minimal Images
* [ ] Distroless Images
* [ ] Non-root Containers
* [ ] Linux Capabilities
* [ ] Seccomp
* [ ] AppArmor
* [ ] Read-only Filesystem
* [ ] Resource Limits
* [ ] Secrets
* [ ] Image Scanning
* [ ] Trivy
* [ ] Grype
* [ ] Docker Scout
* [ ] Container Escape concepts

---

## Phase 9 — Kubernetes Fundamentals

* [ ] Kubernetes Architecture
* [ ] Control Plane
* [ ] API Server
* [ ] etcd
* [ ] Scheduler
* [ ] Controller Manager
* [ ] kubelet
* [ ] Pod
* [ ] Deployment
* [ ] ReplicaSet
* [ ] Service
* [ ] ClusterIP
* [ ] NodePort
* [ ] LoadBalancer
* [ ] Ingress
* [ ] ConfigMap
* [ ] Secret

---

## Phase 10 — Kubernetes Networking

* [ ] Pod Network
* [ ] CNI
* [ ] Network Namespace
* [ ] veth
* [ ] Pod-to-Pod Networking
* [ ] Pod-to-Service Networking
* [ ] Service Discovery
* [ ] CoreDNS
* [ ] kube-proxy
* [ ] iptables / IPVS concepts
* [ ] Flannel
* [ ] NetworkPolicy
* [ ] Ingress Networking

---

## Phase 11 — Kubernetes Security

* [ ] RBAC
* [ ] Service Accounts
* [ ] Security Context
* [ ] Pod Security Standards
* [ ] Capabilities
* [ ] Seccomp
* [ ] Secrets
* [ ] Network Policies
* [ ] Admission Control
* [ ] Resource Limits
* [ ] Image Security
* [ ] Kubescape
* [ ] kube-bench
* [ ] Falco

---

## Phase 12 — DevSecOps / Supply Chain

* [ ] SAST
* [ ] Semgrep
* [ ] Dependency Scanning
* [ ] SCA
* [ ] SBOM
* [ ] Syft
* [ ] Container Image Scanning
* [ ] Trivy
* [ ] Image Signing
* [ ] Cosign
* [ ] Software Supply Chain
* [ ] GitHub Actions
* [ ] Jenkins
* [ ] Security Gates
* [ ] CI/CD Security

---

## Phase 13 — Production Security / Observability

* [ ] Application Logging
* [ ] Structured Logging
* [ ] Metrics
* [ ] Monitoring
* [ ] Alerting
* [ ] Security Events
* [ ] Audit Logs
* [ ] Runtime Detection
* [ ] Incident Investigation
* [ ] Network Troubleshooting
* [ ] Container Troubleshooting
* [ ] Kubernetes Troubleshooting

---

## Phase 14 — Final Project

Anomaly:
- Retranmission. 
- Flow control check.

Build and secure:

```text
Angular
   ↓
Nginx
   ↓
FastAPI
   ↓
PostgreSQL
```

Deploy:

```text
Docker / Podman
        ↓
       K3s
```

Add:

```text
TLS
RBAC
NetworkPolicies
Secrets
Trivy
Syft
Cosign
Falco
Kubescape
GitHub Actions
Monitoring
```

Final goal:

```text
Developer
    ↓
Secure Application
    ↓
Secure Container
    ↓
Secure Kubernetes Deployment
    ↓
Secure CI/CD Pipeline
    ↓
Monitor + Detect + Troubleshoot
```
