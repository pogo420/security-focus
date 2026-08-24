# Security Upskill Roadmap

## 1. Application Security 🟢

* [x] OWASP Top 10
* [x] Injection
* [x] Broken Access Control
* [x] Authentication & Authorization
* [x] Session Management
* [x] CSRF
* [x] CORS
* [x] SSRF
* [x] Security Misconfiguration
* [x] Cryptographic Failures
* [x] Vulnerable Components
* [x] Logging & Monitoring
* [x] Secure API Basics
* [x] Threat Modeling Basics
* [x] Security Testing Mindset

## 2. Container Security 🔵

### Container Fundamentals

* [x] Containers vs VMs
* [x] Docker Architecture
* [x] Images, Layers & Registries
* [x] Containers vs Images
* [x] Dockerfile Basics

### Container Security

* [x] Secure Dockerfiles
* [x] Non-root Containers
* [x] Linux Capabilities
* [x] Privileged Containers
* [x] Filesystem Security
* [x] Secrets
* [x] Resource Limits
* [x] Container Isolation

### Image Security

* [x] Vulnerability Scanning
* [x] Base Image Selection
* [x] Minimal/Distroless Images
* [x] Image Signing
* [x] Image Provenance
* [x] SBOM

### Runtime Security

* [x] Container Escape — Concept
* [x] Runtime Monitoring
* [x] Suspicious Processes
* [x] Network Exposure
* [x] Container Logging

## 3. Kubernetes Security 🔵

### Kubernetes Fundamentals

* [ ] Kubernetes Architecture
* [ ] Control Plane
* [ ] Nodes
* [ ] Pods
* [ ] Deployments
* [ ] Services
* [ ] ConfigMaps
* [ ] Secrets

### Identity & Access

* [ ] Service Accounts
* [ ] RBAC
* [ ] Roles
* [ ] RoleBindings
* [ ] ClusterRoles
* [ ] Least Privilege

### Workload Security

* [ ] Security Context
* [ ] Run as Non-root
* [ ] Linux Capabilities
* [ ] Privileged Pods
* [ ] Read-only Filesystem
* [ ] Pod Security Standards

### Network Security

* [ ] Kubernetes Networking Basics
* [ ] NetworkPolicies
* [ ] Namespace Isolation
* [ ] Ingress
* [ ] Service Exposure

### Kubernetes Attack Surface

* [ ] Compromised Pod
* [ ] Service Account Abuse
* [ ] Excessive RBAC
* [ ] Exposed API Server
* [ ] Secret Exposure
* [ ] Container Escape
* [ ] Lateral Movement

### Kubernetes Security Controls

* [ ] Admission Control
* [ ] Image Policies
* [ ] Secrets Management
* [ ] Audit Logging
* [ ] Runtime Security
* [ ] Policy Enforcement

## 4. DevSecOps 🔵

### CI/CD Fundamentals

* [ ] CI vs CD
* [ ] Pipeline Architecture
* [ ] Build → Test → Package → Deploy
* [ ] Artifacts
* [ ] Runners/Agents

### Security in CI/CD

* [ ] SAST
* [ ] SCA
* [ ] Secret Scanning
* [ ] DAST
* [ ] Container Scanning
* [ ] IaC Scanning

### Supply Chain Security

* [ ] Dependencies
* [ ] SBOM
* [ ] Artifact Integrity
* [ ] Dependency Confusion
* [ ] Typosquatting
* [ ] Software Signing
* [ ] Provenance
* [ ] Build Security

### Pipeline Security

* [ ] Secrets in Pipelines
* [ ] Runner Security
* [ ] Branch Protection
* [ ] Pull Request Security
* [ ] Least Privilege
* [ ] Pipeline Permissions
* [ ] Security Gates

### Deployment Security

* [ ] Secure Promotion
* [ ] Image Verification
* [ ] Environment Separation
* [ ] Production Access
* [ ] Continuous Monitoring

## 5. Final Integration 🔵

* [ ] Developer → Application
* [ ] Application → Dependencies
* [ ] Dependencies → Container
* [ ] Container → CI/CD
* [ ] CI/CD → Registry
* [ ] Registry → Kubernetes
* [ ] Kubernetes → Cloud
* [ ] Cloud → Runtime
* [ ] End-to-end Attack Paths
* [ ] End-to-end Security Controls
