#!/usr/bin/env python3
"""
Main entry point for the application.
"""

import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file
load_dotenv()

# Configure logging
logger.remove()  # Remove default handler
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    backtrace=True,
    diagnose=True,
)

# Add file logging in production
if os.getenv("ENV") == "production":
    log_path = Path("logs")
    log_path.mkdir(exist_ok=True)
    logger.add(
        log_path / "app.log",
        rotation="500 MB",
        retention="30 days",
        level="INFO",
        enqueue=True,
    )


class Config:
    """Application configuration."""

    def __init__(self) -> None:
        """Initialize configuration from environment variables."""
        self.env: str = os.getenv("ENV", "development")
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"
        self.app_name: str = os.getenv("APP_NAME", "Python Project Template")
        self.app_version: str = os.getenv("APP_VERSION", "0.1.0")

        # Add more configuration as needed
        self.database_url: str = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary.

        Returns:
            Dict[str, Any]: Configuration as dictionary
        """
        return {
            "env": self.env,
            "debug": self.debug,
            "app_name": self.app_name,
            "app_version": self.app_version,
            "database_url": "[REDACTED]" if "sqlite" not in self.database_url else self.database_url,
        }


def main() -> None:
    """Main application entry point."""
    try:
        # Initialize configuration
        config = Config()
        logger.info(f"Starting {config.app_name} v{config.app_version}")
        logger.debug(f"Configuration: {config.to_dict()}")

        # Your application logic goes here
        logger.info("Application started successfully!")

        print(f"Hello from {config.app_name}!")


    except Exception as e:
        logger.exception("An error occurred while running the application")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        sys.exit(0)
    finally:
        logger.info("Application shutdown complete")


if __name__ == "__main__":
    main()