"""
Khyathi.ai – Configuration
Loads settings from environment variables using pydantic-settings.
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Required
    openai_api_key: str = ""
    serper_api_key: str = ""

    # Recommended
    anthropic_api_key: Optional[str] = None

    # Models
    openai_model: str = "gpt-4o"
    anthropic_model: str = "claude-3-5-sonnet-20241022"

    # Runtime
    workspace_dir: Path = Path("./workspace")
    log_level: str = "INFO"
    max_iterations: int = 15

    # Optional Phase 2+
    composio_api_key: Optional[str] = None
    pinecone_api_key: Optional[str] = None


settings = Settings()
