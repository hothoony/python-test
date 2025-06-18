import os
import logging
import logging.handlers
from pathlib import Path
from typing import Optional, Dict, Any
import json
import sys

class JsonFormatter(logging.Formatter):    
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'name': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }
        
        # Add exception info if present
        if record.exc_info:
            log_record['exc_info'] = self.formatException(record.exc_info)
            
        # Add extra fields if present
        if hasattr(record, 'data'):
            log_record.update(record.data)
            
        return json.dumps(log_record, ensure_ascii=False)

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
    # Ensure log directory exists
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True, parents=True)
    
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
    if app_env == 'prod' or os.getenv('ENABLE_FILE_LOGGING', '').lower() == 'true':
        # Rotating file handler
        file_handler = logging.handlers.RotatingFileHandler(
            log_path / 'app.log',
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setFormatter(console_formatter if app_env == 'dev' else JsonFormatter())
        root_logger.addHandler(file_handler)
    
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
    root_logger.info("Logging configured", extra={
        'data': {
            'environment': app_env,
            'log_level': log_level,
            'log_dir': str(log_path.absolute())
        }
    })
