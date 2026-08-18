## App security goldel rule

* Treat all externally controlled data as untrusted until the application has safely validated and authorized its use. All examples are described in the remaining points.
* OWASP 10 (Open Worldwide Application Security Project) and Imp App security checklist.
    ```text
    Untrusted input?
        ↓
    Authentication?
        ↓
    Authorization?
        ↓
    Data/code separation?
        ↓
    Safe resource access?
        ↓
    Least privilege?
        ↓
    Secure configuration?
        ↓
    Integrity / provenance?
        ↓
    Safe failure?
        ↓
    Logging / alerting?
    ```

## AuthN vs AuthZ

* AuthN -> Authentication -> Indentify -> Who are you?
* AuthZ -> Authorization -> Permissing -> What resources you have access?

## Broken Access Control
* Take care of AuthZ; If user is athenticated, does not mean he/she can access any resource.

## SQL Injection

```text
SQL Injection (SQLi)
--------------------

Definition:
Attacker-controlled input becomes part of the SQL command,
allowing the attacker to change the intended query.


Vulnerable:

query = "SELECT * FROM users WHERE name = '" + name + "'"

Problem:
SQL + user input → one SQL string
                    ↓
              SQL parser
                    ↓
               SQL Injection


Example:

Normal input:
name = alice

SELECT * FROM users WHERE name = 'alice';


Malicious input can contain SQL syntax and alter
the meaning of the query.

Example:

name = ' OR '1'='1' --

SELECT * FROM users WHERE name = '' OR '1'='1' --';
# Returns true

Root Cause:
Mixing DATA with CODE.

The database cannot reliably distinguish:
    - intended SQL
    - attacker-controlled SQL syntax


Fix:

query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (name,))


The SQL structure and user data remain separate:

SQL structure → fixed
User input    → parameter/data


Key Rule:
"Separate data from code."

"Never build SQL by concatenating untrusted input."


Preferred defenses:
- Parameterized queries / prepared statements
- Safe ORM parameter binding
- Least-privileged database accounts
- Input validation as defense-in-depth


Important:
Escaping input alone should NOT be the primary defense.
Use parameterized queries.
```


## XSS (Cross site scripting)

* Cross -> Attacker's content crosses into a website's page and runs in the victim's browser.

### Reflected XSS:

```text
Attacker
   │
   │ /search?q=malicious-input
   ▼
Server
   │
   │ puts q directly into HTML response
   ▼
Browser
   │
   └── interprets it
        💥 XSS

Encode the q and use to prevent q to be interpreted as html.
```

### Stored XSS:

```text
Attacker
   │
   │ Submit malicious input
   ▼
Application
   │
   │ Stores input
   ▼
Database / Storage
   │
   │ Stored untrusted data
   ▼
Victim requests page
   │
   ▼
Application
   │
   │ Inserts stored data into HTML
   ▼
Browser
   │
   │ Interprets it as HTML/JS
   ▼
💥 XSS
```

* Root Cause: 
   - Stored user input is later inserted into an HTML/JS context without appropriate output encoding/sanitization.


* Defense:
  ```text
      Untrusted input
          ↓
      Context-appropriate output encoding
          ↓
      HTML
          ↓
      Browser treats it as DATA
  ```

* Key Rule:
   - "Never trust data just because it came from your database."


### DOM XSS

* Definition:
   * A client-side XSS vulnerability where attacker-controlled data
flows through JavaScript into a dangerous DOM/API sink.

```text
Flow:

Attacker-controlled input
        ↓
Browser / JavaScript
        ↓
Dangerous DOM sink
        ↓
Browser interprets it
        ↓
💥 XSS
```

Common Sources:
- URL query parameters
- URL hash
- Form input
- API responses
- localStorage / other client-side data


Common Dangerous Sinks:
- innerHTML
- outerHTML
- document.write()
- insertAdjacentHTML()

Example:
```
const name = location.search;

element.innerHTML = name;
```

Problem:

`Untrusted data → innerHTML → interpreted as HTML`


Safer:

`element.textContent = name;`


* Key Rule:
   * Keep untrusted data as DATA.
Don't put it into dangerous DOM sinks.



## CSRF(Cross Site Request Frogery)

```text
Victim is logged into bank.com
        ↓
Browser has bank.com session cookie
        ↓
Victim visits attacker.com
        ↓
attacker.com causes a request to bank.com
        ↓
Browser may attach bank.com's cookie
        ↓
bank.com sees an authenticated request
        ↓
💥
```

Defence:

```text
CSRF tokens (generated from page, attacker can't read, not saved in session cookie)
     +
SameSite cookies (cookie not valid for diferent sites)
     +
Origin / Referer validation
```

## SSRF(Server Side Request Frogery)

* SSRF = Untrusted input controls where the server makes an outbound request.

## Command Injection

* Don't let untrusted data become executable instructions.

## Path traversal

* Path Traversal = untrusted input controls a filesystem path and escapes the intended directory.

```text
API: 

GET /download?file=report.pdf

----
Intended:

/app/uploads/report.pdf
             ↑
        allowed area

----
Attacker-controlled path:

/app/uploads/...
             ↓
       resolves elsewhere
             ↓
       unintended file
```

## File Upload

* Treat uploaded files as untrusted data, not trusted application files.

## API Security

* Every API endpoint must independently enforce authentication, authorization, input constraints, and appropriate resource limits.

## Rate limiting

* Rate limiting prevents an actor from abusing an operation faster or more often than intended.


## CORS

* **CORS = Cross-Origin Resource Sharing**
* Browser security mechanism for **cross-origin requests**
* Controls **which origins can read the response**
* Server declares allowed origins using response headers
* Some requests trigger a **preflight `OPTIONS` request**
* CORS is mainly **browser-enforced**; it is not an API authorization mechanism
* `Access-Control-Allow-Origin: *` is risky for sensitive APIs (In response header of server/API)
* Never blindly trust/reflect the incoming `Origin`
* So the server defines the CORS policy, and the browser enforces it.

```text
* Browser
   ↓ OPTIONS
Server
   ↓ allowed?
Browser
   ↓ actual request
Server
```