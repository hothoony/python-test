"""Tests for the main application."""

import os
import sys
from unittest.mock import patch, MagicMock

import pytest
from loguru import logger

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestConfig:
    """Tests for the Config class."""

    def test_config_defaults(self):
        """Test that Config has the correct default values."""
        from src.main import Config

        with patch.dict(os.environ, {}, clear=True):
            config = Config()
            assert config.env == "development"
            assert config.debug is False
            assert config.app_name == "Python Project Template"
            assert config.app_version == "0.1.0"
            assert config.database_url == "sqlite:///./sql_app.db"

    def test_config_from_env(self):
        """Test that Config reads values from environment variables."""
        from src.main import Config

        env_vars = {
            "ENV": "testing",
            "DEBUG": "true",
            "APP_NAME": "Test App",
            "APP_VERSION": "1.0.0",
            "DATABASE_URL": "sqlite:///:memory:",
        }

        with patch.dict(os.environ, env_vars, clear=True):
            config = Config()
            assert config.env == "testing"
            assert config.debug is True
            assert config.app_name == "Test App"
            assert config.app_version == "1.0.0"
            assert config.database_url == "sqlite:///:memory:"

    def test_to_dict_redaction(self):
        """Test that sensitive data is redacted in to_dict()."""
        from src.main import Config

        with patch.dict(os.environ, {"DATABASE_URL": "postgresql://user:pass@localhost/db"}, clear=True):
            config = Config()
            config_dict = config.to_dict()
            assert config_dict["database_url"] == "[REDACTED]"


class TestMain:
    """Tests for the main application."""

    @patch("src.main.logger")
    @patch("src.main.Config")
    @patch("builtins.print")
    def test_main_success(self, mock_print, mock_config_class, mock_logger):
        """Test that main() runs successfully."""
        from src.main import main

        # Setup mock config
        mock_config = mock_config_class.return_value
        mock_config.app_name = "Test App"
        mock_config.app_version = "1.0.0"
        mock_config.to_dict.return_value = {"test": "config"}

        # Run the main function
        main()


        # Verify the expected calls were made
        mock_logger.info.assert_any_call("Starting Test App v1.0.0")
        mock_logger.debug.assert_called_once_with("Configuration: {'test': 'config'}")
        mock_logger.info.assert_any_call("Application started successfully!")
        mock_print.assert_called_once_with("Hello from Test App!")
        mock_logger.info.assert_any_call("Application shutdown complete")

    @patch("src.main.logger")
    @patch("src.main.Config")
    def test_main_keyboard_interrupt(self, mock_config_class, mock_logger):
        """Test that main() handles KeyboardInterrupt gracefully."""
        from src.main import main

        # Setup mock to raise KeyboardInterrupt
        mock_config = mock_config_class.return_value
        mock_config.app_name = "Test App"
        mock_logger.info.side_effect = KeyboardInterrupt()

        # Run the main function
        with pytest.raises(SystemExit) as exc_info:
            main()

        # Verify exit code is 0 for KeyboardInterrupt
        assert exc_info.value.code == 0
        mock_logger.info.assert_any_call("Application interrupted by user")
        mock_logger.info.assert_any_call("Application shutdown complete")

    @patch("src.main.logger")
    @patch("src.main.Config")
    def test_main_unhandled_exception(self, mock_config_class, mock_logger):
        """Test that main() logs unhandled exceptions."""
        from src.main import main

        # Setup mock to raise an exception
        mock_config = mock_config_class.return_value
        mock_config.app_name = "Test App"
        mock_logger.info.side_effect = Exception("Test error")

        # Run the main function
        with pytest.raises(SystemExit) as exc_info:
            main()

        # Verify exit code is 1 for unhandled exceptions
        assert exc_info.value.code == 1
        mock_logger.exception.assert_called_once_with(
            "An error occurred while running the application"
        )
        mock_logger.info.assert_called_with("Application shutdown complete")