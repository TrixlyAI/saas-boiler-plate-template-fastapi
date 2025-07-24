from fastapi import FastAPI
from app.api import users, agents

app = FastAPI(title="VoiceAI SaaS")

app.include_router(users.router)
app.include_router(agents.router)

@app.get("/health")
def health_check():
    return {"status": "ok"} 