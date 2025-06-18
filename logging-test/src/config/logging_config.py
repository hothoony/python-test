import os
import logging
import logging.handlers
from pathlib import Path
from typing import Optional, Dict, Any
import json
import sys

class JsonFormatter(logging.Formatter):
    def format(self, record):
        # Create a dict with the basic log record attributes
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'name': record.name,
            'message': record.getMessage(),
            'module': getattr(record, 'module', record.module if hasattr(record, 'module') else record.name),
            'function': record.funcName,
            'line': record.lineno,
        }
        
        # Add exception info if present
        if record.exc_info:
            log_record['exc_info'] = self.formatException(record.exc_info)
        
        # Handle extra data
        extra_data = {}
        if hasattr(record, 'data') and isinstance(record.data, dict):
            extra_data.update(record.data)
        
        # Add any other extra fields (excluding internal use fields)
        for key, value in record.__dict__.items():
            if key not in ('args', 'asctime', 'created', 'exc_info', 'exc_text', 
                         'filename', 'funcName', 'id', 'levelname', 'levelno', 
                         'lineno', 'module', 'msecs', 'message', 'msg', 'name', 
                         'pathname', 'process', 'processName', 'relativeCreated',
                         'stack_info', 'thread', 'threadName') and not key.startswith('_'):
                extra_data[key] = value
        
        if extra_data:
            log_record['data'] = extra_data
            
        return json.dumps(log_record, ensure_ascii=False, default=str)

class MaskingFilter(logging.Filter):
    """Filter to mask sensitive information in logs"""
    def __init__(self, patterns=None):
        super().__init__()
        self._patterns = patterns or [
            r'(?i)password',
            r'(?i)secret',
            r'(?i)api[_-]?key',
            r'(?i)token',
            r'(?i)access[_-]?key',
            r'(?i)secret[_-]?key',
        ]
        
    def filter(self, record):
        if not hasattr(record, 'msg') or not record.msg:
            return True
            
        if isinstance(record.msg, dict):
            record.msg = self._mask_dict(record.msg)
        elif isinstance(record.msg, str):
            record.msg = self._mask_string(record.msg)
            
        return True
    
    def _mask_dict(self, d: Dict) -> Dict:
        masked = {}
        for k, v in d.items():
            if any(re.search(p, k, re.IGNORECASE) for p in self._patterns):
                masked[k] = '***MASKED***'
            elif isinstance(v, dict):
                masked[k] = self._mask_dict(v)
            elif isinstance(v, str):
                masked[k] = self._mask_string(v)
            else:
                masked[k] = v
        return masked
    
    def _mask_string(self, s: str) -> str:
        # This is a simple implementation - you might want to enhance it
        # based on your specific needs
        for pattern in self._patterns:
            if re.search(pattern, s, re.IGNORECASE):
                return '***MASKED***'
        return s

def setup_logging(app_env: str = 'dev', log_level: Optional[str] = None, log_dir: str = 'logs') -> None:
    """
    Configure logging for the application.
    
    Args:
        app_env: Application environment ('dev' or 'prod')
        log_level: Override log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir: Directory to store log files
    """
    # Create a temporary console logger for setup debugging
    temp_console = logging.StreamHandler()
    temp_console.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    temp_logger = logging.getLogger('setup_logger')
    temp_logger.setLevel(logging.DEBUG)
    temp_logger.addHandler(temp_console)
    
    try:
        temp_logger.debug("Starting logging configuration")
        temp_logger.debug(f"Environment: {app_env}, Log Level: {log_level}, Log Directory: {log_dir}")
        
        # Ensure log directory exists
        log_path = Path(log_dir).resolve()  # Get absolute path
        temp_logger.debug(f"Resolved log path: {log_path}")
    except Exception as e:
        temp_logger.error(f"Error during logging setup: {e}", exc_info=True)
        # Re-raise the exception after logging it
        raise
    
    # Set default log level based on environment
    if log_level is None:
        log_level = 'DEBUG' if app_env == 'dev' else 'INFO'
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Clear existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Create formatters
    if app_env == 'dev':
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    else:
        console_formatter = JsonFormatter(
            datefmt='%Y-%m-%dT%H:%M:%S%z'
        )
    
    # Console handler (always enabled)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # File handler (only in production or when explicitly enabled in dev)
    enable_file_logging = os.getenv('ENABLE_FILE_LOGGING', '').lower() == 'true'
    temp_logger.debug(f"File logging enabled: {enable_file_logging} (app_env: {app_env})")
    
    if app_env == 'prod' or enable_file_logging:
        try:
            # Ensure log directory exists and is writable
            try:
                log_path.mkdir(parents=True, exist_ok=True, mode=0o755)
                temp_logger.debug(f"Created/verified log directory: {log_path}")
                
                # Test if directory is writable
                test_file = log_path / '.permission_test'
                try:
                    test_file.touch(exist_ok=True)
                    test_file.unlink()
                    temp_logger.debug("Successfully wrote to log directory")
                except (IOError, OSError) as e:
                    error_msg = f"Cannot write to log directory {log_path.absolute()}: {e}"
                    temp_logger.error(error_msg)
                    root_logger.warning(
                        error_msg,
                        extra={'context': {'log_dir': str(log_path.absolute())}}
                    )
                    raise
            except Exception as e:
                error_msg = f"Failed to create log directory {log_path.absolute()}: {e}"
                temp_logger.error(error_msg, exc_info=True)
                root_logger.error(error_msg, exc_info=True)
                raise
            
            # Daily rotating file handler
            try:
                log_file = log_path / 'app.log'
                log_file_str = str(log_file.absolute())
                temp_logger.debug(f"Configuring file handler for: {log_file_str}")
                
                file_handler = logging.handlers.TimedRotatingFileHandler(
                    filename=log_file_str,
                    when='midnight',     # Rotate at midnight
                    interval=1,          # Create new file daily
                    backupCount=30,      # Keep logs for 30 days
                    encoding='utf-8',
                    utc=False,          # Use local timezone
                    atTime=None,         # Rotate at midnight
                    delay=False          # Don't delay file opening
                )
                temp_logger.debug("Successfully created TimedRotatingFileHandler")
            except Exception as e:
                error_msg = f"Failed to create file handler: {e}"
                temp_logger.error(error_msg, exc_info=True)
                root_logger.error(error_msg, exc_info=True)
                raise
            
            # Set formatter based on environment
            file_formatter = console_formatter if app_env == 'dev' else JsonFormatter()
            file_handler.setFormatter(file_formatter)
            
            # Add filter to mask sensitive data
            masking_filter = MaskingFilter()
            file_handler.addFilter(masking_filter)
            
            # Set log level
            file_handler.setLevel(log_level)
            
            # Add to root logger
            root_logger.addHandler(file_handler)
            
            # Log successful file handler setup
            success_msg = f"File logging enabled. Logs will be saved to: {log_file.absolute()}"
            temp_logger.info(success_msg)
            root_logger.info(
                success_msg,
                extra={'context': {
                    'log_file': str(log_file.absolute()),
                    'backup_count': 30,
                    'when': 'midnight',
                    'log_level': logging.getLevelName(file_handler.level)
                }}
            )
            
        except Exception as e:
            root_logger.error(
                "Failed to initialize file logging",
                exc_info=True,
                extra={'context': {
                    'log_dir': str(log_path.absolute()),
                    'error': str(e)
                }}
            )
    
    # Add masking filter
    masking_filter = MaskingFilter()
    for handler in root_logger.handlers:
        handler.addFilter(masking_filter)
    
    # Configure third-party loggers
    logging.getLogger('urllib3').setLevel('WARNING')
    logging.getLogger('requests').setLevel('WARNING')
    logging.getLogger('boto3').setLevel('WARNING')
    logging.getLogger('botocore').setLevel('WARNING')
    logging.getLogger('s3transfer').setLevel('WARNING')
    
    # Set up exception hook for unhandled exceptions
    def handle_exception(exc_type, exc_value, exc_traceback):
        """Log unhandled exceptions"""
        if issubclass(exc_type, KeyboardInterrupt):
            # Call the default excepthook for keyboard interrupts
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
            
        root_logger.critical(
            "Uncaught exception",
            exc_info=(exc_type, exc_value, exc_traceback)
        )
    
    # Set the exception handler
    sys.excepthook = handle_exception
    
    # Log configuration
    config_info = {
        'environment': app_env,
        'log_level': log_level,
        'log_dir': str(log_path.absolute()),
        'file_logging_enabled': enable_file_logging,
        'handlers': [h.__class__.__name__ for h in root_logger.handlers]
    }
    
    temp_logger.debug("Final logging configuration: %s", config_info)
    root_logger.info("Logging configured", extra={'data': config_info})
    
    # Clean up temporary logger
    temp_logger.removeHandler(temp_console)
    temp_console.close()
