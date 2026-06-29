from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Spend Tracker API"
    environment: str = "local"  # local | staging | production
    debug: bool = True
    database_url: str
    test_database_url: str = ""


settings = Settings()