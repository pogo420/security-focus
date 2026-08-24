# Containers

## Container / Image Security Checklist

### 🏗️ Build & Dockerfile

* [ ] Use a **trusted, minimal base image**
* [ ] Keep dependencies updated and scan them
* [ ] Don't hardcode secrets in Dockerfile/source
* [ ] Use **multi-stage builds** where appropriate
* [ ] Remove unnecessary packages/tools
* [ ] Run application as **non-root**
* [ ] Pin versions/digests where appropriate

### 🔐 Container Security

* [ ] Drop unnecessary **Linux capabilities**
* [ ] Never use `--privileged` unless absolutely required
* [ ] Use a **read-only filesystem** where possible
* [ ] Restrict host filesystem mounts
* [ ] Give containers only required volumes/access
* [ ] Set **CPU, memory and PID limits**
* [ ] Minimize container privileges and isolation weaknesses

### 🔑 Secrets & Configuration

* [ ] Inject secrets at **runtime**
* [ ] Never bake secrets into images
* [ ] Use a proper **secret manager** where possible
* [ ] Treat environment variables as configuration, **not automatically secure secret storage**
* [ ] Restrict secret access
* [ ] Rotate secrets

### 🛡️ Image Security / Supply Chain

* [ ] Scan images for vulnerabilities
* [ ] Scan **base OS + application dependencies**
* [ ] Prefer minimal/distroless images where practical
* [ ] Generate an **SBOM**
* [ ] Generate/verify **provenance**
* [ ] **Sign images**
* [ ] Verify signatures/provenance before deployment
* [ ] Use trusted registries and control who can push images

### 🚨 Runtime Security

* [ ] Monitor container behavior
* [ ] Detect unexpected/suspicious processes
* [ ] Minimize exposed ports
* [ ] Restrict unnecessary network communication
* [ ] Monitor container/network activity
* [ ] Centralize container logs
* [ ] Never log secrets

### 🧠 Final Mental Model

```text
SOURCE
  ↓
SECURE DOCKERFILE
  ↓
MINIMAL IMAGE
  ↓
SCAN
  ↓
SBOM + PROVENANCE
  ↓
SIGN
  ↓
TRUSTED REGISTRY
  ↓
VERIFY
  ↓
NON-ROOT CONTAINER
  ↓
LEAST PRIVILEGE
  ↓
LIMIT RESOURCES
  ↓
RESTRICT NETWORK/FILESYSTEM
  ↓
MONITOR + LOG
```

**The core rule:**

> **Build securely → verify the image → run with least privilege → restrict access → monitor at runtime.**

----

## Containers intro

```text
VM
└── Virtual machine / complete OS

Image
└── Immutable package/template

Container
└── Running instance of an image

Registry
└── Stores/distributes images

Docker
└── Tooling/platform for building and running containers
```

## Docker Images — Notes

* **Image** → Immutable package/template used to create containers.
* Contains → Application + dependencies + runtime + filesystem + metadata.
* **Container** → Running instance of an image.
* Images are built in **layers** → improves caching, reuse, and efficient distribution.
* **Base image** → Starting image used to build your application image.
* Vulnerabilities in the base image can be **inherited** by your image.
* **Tag** → Human-readable image identifier, e.g. `myapp:1.0`.
* `latest` → Mutable tag; **not necessarily latest or safest**.
* **Digest** (`sha256:...`) → Identifies specific image content; better for reproducibility.
* **Image security** → Check source, base image, vulnerabilities, dependencies, secrets, unnecessary software, root user, and provenance.
* Security flow → **Build → Scan → Verify → Store → Deploy**.


## Dockerfile — Notes

* **Dockerfile** → Text file containing instructions to build a Docker image.
* Flow → `Dockerfile → docker build → Image → docker run → Container`

**Key instructions:**

* `FROM` → Base image
* `WORKDIR` → Working directory
* `COPY` → Copy files into image
* `RUN` → Execute commands at **build time**
* `ENV` → Environment variables
* `USER` → User container runs as
* `EXPOSE` → Documents intended port
* `CMD` → Default command at **runtime**
* `ENTRYPOINT` → Main executable

**Important:**

* `RUN` = **build time**
* `CMD` = **runtime**

**Security checklist:**

* Trusted/minimal base image
* No secrets in image
* Pin dependencies
* Run as non-root
* Remove unnecessary packages
* Safe `ENTRYPOINT` / `CMD`
* Core: **A container should have the minimum software, privileges, permissions, and access required to do its job.**

## Using linux capabilities

```text
Container
└── non-root
    └── only required capabilities
```

## Filesystem Security — Notes 
* Read-only filesystem → Prevents unnecessary file modifications inside the container. 
* Volumes → Persistent storage used by containers. 
* Bind mounts → Expose a specific host path inside a container. 
* Sensitive host paths → Avoid mounting /, /etc, /home, etc. unless absolutely necessary. 
* Read-only mounts → Use when the container only needs to read host data. 
* Principle: Give containers the minimum filesystem access required.

## Secrets
* Secrets should be injected at runtime, not baked into images.


## For production containers: 
* Set reasonable CPU limits 
* Set memory limits * Consider PID limits 
* Monitor actual usage 
* Don’t give significantly more resources than the application needs

## Container isolation:
* Container isolation limits the container’s visibility, privileges, filesystem access, and resource consumption—but the host kernel remains a critical security boundary.

## Image Identifiers
* SBOM = What’s inside?
* Provenance = Where did it come from/how was it built?
* Signature = Can I trust this artifact?

## Container escape
A container escape happens when a process inside a container breaks out of the container's isolation and gains access to the host or other protected resources.
