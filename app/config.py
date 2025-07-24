from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "VoiceAI SaaS"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    stripe_api_key: str
    smtp_server: str
    smtp_port: int
    smtp_user: str
    smtp_password: str
    voice_ai_api_key: str

    class Config:
        env_file = ".env"

settings = Settings() 