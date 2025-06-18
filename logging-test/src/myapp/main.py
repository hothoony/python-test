import os
import sys
import logging
import traceback
from typing import Any, Dict, Optional
from collections import defaultdict

# Import Config without triggering logging setup
from config.base_config import Config as _Config

# Get logger for this module
logger = logging.getLogger(__name__)


class Config(_Config):
    """Extended Config class with additional logging-related methods"""
    pass


# Custom adapter to add context to logs without conflicting with LogRecord attributes
class CustomAdapter(logging.LoggerAdapter):
    def __init__(self, logger, extra=None):
        super().__init__(logger, extra or {})
        self.logger = logger
        self.extra = {'context': {}}
        
    def process(self, msg, kwargs):
        # Get or create the 'extra' dict
        extra = kwargs.get('extra', {})
        
        # Create a context dict if it doesn't exist
        context = {}
        
        # Add our context
        context.update(self.extra['context'])
        
        # Add any context from the extra dict
        if 'context' in extra and isinstance(extra['context'], dict):
            context.update(extra['context'])
            del extra['context']
        
        # Add module context if not already present
        if 'module' not in context:
            context['module'] = 'myapp.main'
        
        # Update the extra dict with our context
        if context:
            extra['context'] = context
            
        kwargs['extra'] = extra
        return msg, kwargs
        
    def add_context(self, **kwargs):
        """Add contextual information to this logger's context"""
        self.extra['context'].update(kwargs)
        return self


# Create logger with our custom adapter
logger = CustomAdapter(logging.getLogger(__name__))

def method01() -> str:
    """
    예제 메서드 01
    
    Returns:
        str: 작업 결과 메시지
    """
    logger.debug("method01 시작")
    
    try:
        # 여기에 실제 비즈니스 로직 구현
        result = "ok"
        logger.info("method01 완료", extra={'data': {'result': result}})
        return result
        
    except Exception as e:
        logger.error(
            "method01 실행 중 오류 발생",
            exc_info=True,
            extra={'data': {'error': str(e)}}
        )
        raise

def method02(param1: str = None, param2: int = None) -> dict:
    """
    파라미터를 받아 처리하고 결과를 반환하는 메서드
    
    Args:
        param1: 문자열 파라미터 (기본값: None)
        param2: 정수 파라미터 (기본값: None)
        
    Returns:
        dict: 처리 결과를 포함한 딕셔너리
        
    Raises:
        ValueError: 필수 파라미터가 누락되었거나 유효하지 않은 경우
    """
    # Create a logger with method context
    method_logger = logger.add_context(method='method02')
    
    try:
        method_logger.debug("메서드 시작", extra={
            'context': {
                'parameters': {
                    'param1': param1,
                    'param2': param2
                }
            }
        })
        
        # 파라미터 유효성 검사
        errors = []
        
        if param1 is None or not str(param1).strip():
            errors.append("param1은(는) 필수이며 비어있을 수 없습니다")
            
        if param2 is None or not isinstance(param2, int):
            errors.append("param2는 필수이며 정수여야 합니다")
        
        if errors:
            error_msg = ", ".join(errors)
            method_logger.warning("유효성 검사 실패", extra={
                'context': {
                    'parameters': {
                        'param1': param1,
                        'param2': param2,
                        'expected_types': {
                            'param1': 'non-empty str',
                            'param2': 'int'
                        }
                    },
                    'validation_errors': errors,
                    'error_type': 'ValidationError'
                }
            })
            raise ValueError(error_msg)
            
        # 처리 로직 (여기서는 단순히 파라미터를 반환하는 예제)
        result = {
            'status': 'success',
            'message': '처리 완료',
            'data': {
                'processed_param1': str(param1).upper(),
                'processed_param2': param2 * 2
            },
            'metadata': {
                'input': {'param1': param1, 'param2': param2}
            }
        }
        
        method_logger.info("메서드 완료", extra={
            'context': {
                'result': {
                    'status': result['status'],
                    'message': result['message']
                }
            }
        })
        
        return result
        
    except Exception as e:
        method_logger.error(
            "메서드 실행 중 오류 발생",
            exc_info=True,
            extra={
                'context': {
                    'error': str(e),
                    'error_type': type(e).__name__,
                    'parameters': {
                        'param1': param1,
                        'param2': param2
                    },
                    'status': 'error'
                }
            }
        )
        raise

def run():
    """애플리케이션 메인 실행 함수"""
    # Create a logger with execution context
    run_logger = logger.add_context(component='application', phase='startup')
    
    try:
        # Log configuration at startup (using direct Config access)
        config_data = {
            'app_env': Config.APP_ENV,
            'debug': Config.DEBUG,
            'db_host': Config.DB_HOST,
            'db_port': Config.DB_PORT,
            'db_user': Config.DB_USER,
            'log_level': getattr(Config, 'LOG_LEVEL', 'INFO'),
            'log_dir': getattr(Config, 'LOG_DIR', 'logs')
        }
        
        run_logger.info("애플리케이션 시작 중...", extra={
            'context': {
                'config': config_data,
                'phase': 'initialization'
            }
        })
        
        # Example method calls with proper parameters
        run_logger.debug("method01 실행 시작")
        method01()
        run_logger.debug("method01 실행 완료")
        
        # Call method02 with valid parameters
        run_logger.debug("method02 실행 시작")
        result = method02(param1="test", param2=42)
        run_logger.debug("method02 실행 완료", extra={
            'context': {
                'result': {
                    'status': result.get('status'),
                    'message': result.get('message')
                }
            }
        })
        
        run_logger.info("애플리케이션 시작 완료", extra={
            'context': {
                'status': 'success',
                'phase': 'running'
            }
        })
        return 0
        
    except Exception as e:
        error_info = {
            'error': str(e),
            'error_type': type(e).__name__,
            'phase': 'startup',
            'status': 'failed'
        }
        
        run_logger.critical(
            "애플리케이션 시작 실패: %s",
            str(e),
            exc_info=True,
            extra={'context': error_info}
        )
        return 1

def init_app():
    """Initialize the application and its components"""
    try:
        # Import config after basic setup
        from config import base_config
        
        # Initialize logging
        if hasattr(base_config, 'init_logging'):
            base_config.init_logging()
        
        # Run the application
        return run()
        
    except Exception as e:
        # This is a last resort error handler if logging fails
        import traceback
        print(f"Critical error during initialization: {e}", file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(init_app())
