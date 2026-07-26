# DevSecOps & Application Security Weekend Roadmap

| Week | Topics | Hands-on | Deliverable |
|------|--------|----------|-------------|
| **Week 1** | Networking Fundamentals<br>- IP Address<br>- MAC Address<br>- ARP<br>- Routing Table<br>- Default Gateway<br>- Switch vs Router<br>- DNS Resolution | `ip addr`<br>`ip route`<br>`ip neigh`<br>`dig`<br>`traceroute`<br>Wireshark | Explain the complete flow of `https://abc.com` from browser to server. Capture DNS, ARP, TCP and HTTPS in Wireshark. |
| **Week 2** | TCP Deep Dive<br>- TCP Header<br>- Ports<br>- 3-Way Handshake<br>- Connection States<br>- Retransmissions<br>- Flow Control | `ss`<br>`netstat`<br>`lsof -i`<br>Wireshark | Explain every packet in a TCP handshake and identify why a connection fails (RST, Timeout, FIN). |
| **Week 3** | HTTP & HTTPS<br>- Requests/Responses<br>- Headers<br>- Cookies<br>- Sessions<br>- TLS Handshake<br>- Certificates | `curl -v`<br>Browser DevTools<br>`openssl s_client` | Trace an HTTPS request and explain every request/response header. Verify a server certificate manually. |
| **Week 4** | DNS Deep Dive<br>- Recursive Resolver<br>- Root<br>- TLD<br>- Authoritative DNS<br>- DNS Records<br>- TTL | `dig`<br>`host`<br>`nslookup` | Explain how `abc.com` resolves to an IP. Query multiple record types and understand caching. |
| **Week 5** | Docker Networking<br>- Namespaces<br>- Bridge Networks<br>- NAT<br>- Port Mapping<br>- Container DNS | `docker network`<br>`docker inspect`<br>`ip addr` | Explain how a request reaches a Docker container from your browser. |
| **Week 6** | Kubernetes Networking<br>- Pod Networking<br>- Services<br>- ClusterIP<br>- NodePort<br>- LoadBalancer<br>- Ingress<br>- CoreDNS | `kubectl get svc`<br>`kubectl exec` | Trace a request from Browser → Ingress → Service → Pod. Explain every networking hop. |
| **Week 7** | Reverse Proxy & Load Balancing | Configure Nginx | Explain Reverse Proxy vs Forward Proxy vs Load Balancer. Configure Nginx for two backend services. |
| **Week 8** | Authentication & Authorization<br>- Basic Auth<br>- Sessions<br>- JWT<br>- OAuth2<br>- RBAC | Decode JWTs<br>Secure an API | Implement JWT authentication in FastAPI and explain the complete login flow. |
| **Week 9** | OWASP Top 10 | PortSwigger Labs | Exploit and then fix SQL Injection, XSS and IDOR vulnerabilities in a lab environment. |
| **Week 10** | Secure Coding | Review one of your APIs | Harden one API using secure coding practices and secrets management. |
| **Week 11** | Container Security | Trivy<br>Grype<br>Docker Scout | Scan a container image, fix high-severity findings and explain the vulnerabilities. |
| **Week 12** | Kubernetes Security | Kubescape<br>kube-bench<br>Falco | Secure a Kubernetes workload using RBAC, Security Context and Network Policies. |
| **Week 13** | DevSecOps | Semgrep<br>Trivy<br>Syft<br>Cosign<br>GitHub Actions/Jenkins | Build a CI/CD pipeline that performs SAST, dependency scan, SBOM generation, image scan and image signing. |
| **Week 14** | Capstone Project | Integrate everything | Deploy a production-style application with Angular, FastAPI, PostgreSQL, Docker/Podman, K3s, Nginx, TLS, GitHub Actions, Trivy, Syft, Cosign, Kubescape and monitoring. |