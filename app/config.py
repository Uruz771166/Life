from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Life Mapping System"
    database_url: str = "sqlite:///./life.db"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
