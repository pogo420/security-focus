# HTTP

## Introduction

* HTTP is an application-layer request/response protocol: Client sends a request → Server sends a response.
* HTTP request contains method (GET, POST, etc.), target (/path), headers, and optionally a body.
* HTTP response contains status code (200, 404, etc.), headers, and optionally a body.
* HTTP runs over TCP (for HTTP/1.1 and HTTP/2): TCP transports the bytes; HTTP gives those bytes application meaning.
* Mental model: TCP = reliable byte transport → HTTP = meaning of those bytes.


## Http method

```text
GET       → "Give me this"
POST      → "Here is some data / do this"
PUT       → "Make this resource exactly this"
PATCH     → "Change these parts"
DELETE    → "Remove this"
HEAD      → "Tell me about it, but don't send the body"
OPTIONS   → "What can I do here?"
```

## URL

* Example: `https://api.example.com:8443/users/42?verbose=true#profile`
* **Scheme** → Protocol (`http`, `https`)
* **Host** → Destination hostname (`api.example.com`)
* **Port** → Service port (`80`, `443`, `8443`)
* **Path** → Resource being requested (`/users/42`)
* **Query** → Parameters (`?role=admin&limit=20`)
* **Fragment** → Client-side reference (`#profile`); normally **not sent to the server**.

## Headers

* **HTTP headers = metadata/instructions** about an HTTP request or response.
* **Request headers** describe what the client wants/sends: `Host`, `Accept`, `Content-Type`, `Authorization`, `Cookie`, `User-Agent`.
* **Response headers** describe what the server returns/controls: `Content-Type`, `Content-Length`, `Set-Cookie`, `Cache-Control`, `Location`.
* **Headers ≠ body**: headers describe the message; the body contains the actual application data.
* **Security-critical headers** include `Authorization`, `Cookie`, `Set-Cookie`, CORS headers, `Content-Security-Policy`, and `Strict-Transport-Security`.

## Status codes
```text
2xx → "It worked"
3xx → "Go/look somewhere else"
4xx → "Your request can't be fulfilled"
5xx → "Something failed on the server side"
401 → "You need valid authentication."
403 → "I know who you are, but you're not allowed."
```

## Cookies

* **Cookie** → Small data stored by the client and sent back to the server with matching requests.
* **`Set-Cookie`** → Server tells the browser to store a cookie.
* **`Cookie`** → Browser sends the stored cookie back to the server.
* Common use → **Session/login state**, preferences, tracking.
* Key security attributes → **`Secure`**, **`HttpOnly`**, **`SameSite`**, `Domain`, `Path`, `Expires/Max-Age`.
* **Treat session cookies like credentials** because they can represent an authenticated user.

```text
Server
  │
  │ Set-Cookie
  ▼
Browser
  │
  │ Cookie
  ▼
Server
```

## Curl summarised

```text
curl -i → Show HTTP response headers + body.
curl -v → Show detailed request/connection information.
curl -X POST → Send a POST request.
-H 'Content-Type: application/json' → Set request header.
-d '{"username":"alice","password":"password"}' → Send request body.
-c cookies.txt → Save cookies received from server to a file.
-b cookies.txt → Send cookies from a file with the request.
Session → Server-side state associated with the session ID.
401 → Request requires valid authentication/session.
```

## Keep Alive

```text
Keep-Alive → Reuse TCP connection
Session     → Maintain application/user state
Cookie      → Carry session identifier
```
HTTP/1.1 normally keeps the TCP connection open after a request, allowing subsequent HTTP requests to reuse the same TCP connection.

## Caching 

```text
First request
Client → Server
          ↓
       Response
       ETag: "abc"

Later request
Client → Server
       If-None-Match: "abc"
          ↓
     Nothing changed?
          ↓
      304 Not Modified
```
Caching improves performance by reusing HTTP responses; cache headers control when/how responses may be stored and reused, while ETags enable efficient revalidation.

### HTTP/2

* **Same HTTP semantics** → Methods, URLs, headers, status codes, body remain.
* **Binary framing** → HTTP messages are split into binary frames.
* **Multiplexing** → Multiple HTTP streams share one TCP connection.
* **Header compression (HPACK)** → Reduces repeated header overhead.
* **Main benefit** → Better performance and reduced connection overhead.
* **Security** → HTTP/2 does not provide encryption; **HTTPS/TLS provides security**.
* HTTP/2 stream = an independent HTTP request/response exchange multiplexed over a shared TCP connection.
* HTTP/1.1 = walkie-talkie 📻
* HTTP/2 = phone call 📞 — multiple conversations can share one connection.


## HTTPS

> **HTTPS = HTTP over TLS.**
> **TLS provides confidentiality, integrity, and server authentication.**
> **Certificates allow the client to authenticate the server.**
> **TLS protects HTTP data while it travels over the network.**

```text
Client
  ↓
HTTP request
  ↓
TLS encryption
  ↓
Network
  ↓
TLS decryption
  ↓
HTTP request
  ↓
FastAPI
```

## TLS Certificates

* **Certificate** = signed statement binding a **domain identity to a public key**.
* **CA signs the certificate** using its **private key** → produces a digital signature.
* **Client verifies** the signature using the CA's **public key**; it does **not** create a new signature.
* **Certificate chain:** `Root CA → Intermediate CA → Server certificate`.
* Root's public key verifies the **Intermediate certificate**; Intermediate's public key verifies the **Server certificate**.
* Server sends **server + intermediate certificates**; the client/OS already has trusted **Root certificates**.
* Browser/TLS stack checks **signature, trust chain, expiry, and hostname (SAN)**.
* Anyone can create a certificate, but a **publicly trusted CA requires proof of domain control** before issuing one.
* **Private keys stay secret**; certificates and public keys are not secret.
* **Signing ≠ encryption:** private key signs → public key verifies.
* Certificate flow 
```text
                 1. SERVER CREATES KEYS
                 ──────────────────────

                 Google Server
                      │
                Generate key pair
                      │
               ┌──────┴──────┐
               │             │
             GPUK           GPRK 🔒
           Public key      Private key
               │
               │ GPUK
               ▼


                 2. SERVER → CA
                 ──────────────

        Google ──────────────► CA
                  CSR
             "google.com"
                 +
                GPUK

                      CA
                      │
              verifies domain
                      │
                      ▼
             Intermediate CA
                      │
             IPRK signs Google
                      │
                      ▼
              Google Certificate
              ┌─────────────────┐
              │ google.com      │
              │ GPUK            │
              │ CA Signature    │
              └─────────────────┘


                 3. CA → SERVER
                 ──────────────

        CA ──────────────────► Google
              Google Certificate
              +
              Intermediate Certificate

              Server keeps:
              GPRK 🔒


                 4. SERVER → CLIENT
                 ──────────────────

        Server ──────────────► Client
                 TLS handshake
                    │
                    ├── Google Certificate
                    ├── Intermediate Certificate
                    └── handshake signature
                         (created using GPRK)


                 5. CLIENT VALIDATES
                 ───────────────────

        Client already has:
             Trusted Root Certificate
                    │
                   RPUK
                    │
                    ▼
          RPUK verifies Intermediate
                    │
                   IPUK
                    │
                    ▼
          IPUK verifies Google Cert
                    │
                   GPUK
                    │
                    ▼
          GPUK verifies Server's
          handshake signature
                    │
                    ▼
                   ✅

```

## SNI (Server name identification)

> SNI = hostname sent in TLS ClientHello so a server hosting multiple HTTPS domains can select the correct certificate.

```text
Client
  │
  │ TLS ClientHello
  │ SNI = google.com
  ├──────────────────► Server
  │
  │ Certificate for google.com
  │◄──────────────────
```

## ALPN

* **ALPN = Application-Layer Protocol Negotiation.**
* Client advertises supported protocols in TLS ClientHello.
* Server selects one.
* Example: `h2` = HTTP/2, `http/1.1` = HTTP/1.1.
* **SNI selects the website; ALPN selects the application protocol.**

ALPN is sent inside the **TLS ClientHello**:

```text
Client
  │
  │ TLS ClientHello
  │
  ├── SNI: example.com
  │
  └── ALPN: h2, http/1.1
  │
  ▼
Server
```

The client is saying:

> "I support HTTP/2 and HTTP/1.1. Pick one."

The server chooses one:

```text
ServerHello
    ALPN: h2
```

## TLS

* Certificate = identity
* Private key = proves identity
* Key exchange = creates temporary session keys
* Session keys = encrypt the actual HTTP traffic
* Summary:
```
Client                              Server
  │                                   │
  │ ClientHello                       │
  │ SNI + ALPN + ECDHE value          │
  ├──────────────────────────────────>│
  │                                   │
  │ ServerHello + ECDHE value         │
  │ Certificate                       │
  │ Server signature                  │
  │<──────────────────────────────────┤
  │                                   │
  │ Verify certificate                │
  │ Verify server signature           │
  │                                   │
  │ Calculate shared secret           │
  │                         Calculate shared secret
  │                                   │
  │ 🔑 Session keys                   🔑
  │                                   │
  │════════ Encrypted HTTP ══════════>│
```
