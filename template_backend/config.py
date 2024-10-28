from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = True

    PORT: int = 8000


settings: Config = Config()
