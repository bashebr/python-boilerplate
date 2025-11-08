from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "development"
    debug: bool = True

    class Config:
        env_file = ".env"


settings: Settings = Settings()
