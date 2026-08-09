from fastapi import FastAPI, Cookie, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import secrets

app = FastAPI()

# Very simple in-memory session store for learning
sessions = {}


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/")
def home():
    return {"message": "Hello from HTTP lab"}


@app.post("/login")
def login(data: LoginRequest):
    if data.username == "alice" and data.password == "password":
        session_id = secrets.token_hex(16)
        sessions[session_id] = data.username

        response = JSONResponse({"message": "Login successful"})

        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=True,
            samesite="lax",
        )

        return response

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/profile")
def profile(session_id: str | None = Cookie(default=None)):
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return {
        "username": sessions[session_id],
        "message": "You are authenticated",
    }
