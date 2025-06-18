import os
import sys
import logging
import traceback
from typing import Any, Dict, Optional
from collections import defaultdict

# Config import will initialize logging automatically
from config.base_config import Config

# Get logger for this module
logger = logging.getLogger(__name__)

# Add module-level context to all log records
logger = logging.LoggerAdapter(logger, {'module': 'myapp.main'})

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

def method02(param1: str = None, param2: int = None) -> Dict[str, Any]:
    """
    예제 메서드 02 - 매개변수와 반환값이 있는 버전
    
    Args:
        param1: 문자열 파라미터
        param2: 정수 파라미터
        
    Returns:
        Dict[str, Any]: 처리 결과 딕셔너리
        
    Raises:
        ValueError: 유효하지 않은 파라미터인 경우
    """
    logger.debug("method02 시작", extra={'data': {'param1': param1, 'param2': param2}})
    
    try:
        # 파라미터 유효성 검사
        if not param1 or not isinstance(param2, int):
            error_msg = "유효하지 않은 파라미터"
            logger.warning(error_msg, extra={
                'data': {
                    'param1': param1,
                    'param2': param2,
                    'param1_type': type(param1).__name__,
                    'param2_type': type(param2).__name__
                }
            })
            raise ValueError(error_msg)
            
        # 여기에 실제 비즈니스 로직 구현
        result = {
            'status': 'success',
            'processed': True,
            'input': {'param1': param1, 'param2': param2}
        }
        
        logger.info("method02 완료", extra={'data': result})
        return result
        
    except Exception as e:
        logger.error(
            "method02 실행 중 오류 발생",
            exc_info=True,
            extra={
                'data': {
                    'error': str(e),
                    'traceback': traceback.format_exc()
                }
            }
        )
        raise

def run():
    """애플리케이션 메인 실행 함수"""
    try:
        # Log configuration at startup
        logger.info("Application starting", extra={
            'data': {
                'config': {
                    'APP_ENV': Config.APP_ENV,
                    'DEBUG': Config.DEBUG,
                    'DB_HOST': Config.DB_HOST,
                    'DB_PORT': Config.DB_PORT,
                    'DB_USER': Config.DB_USER,
                    'LOG_LEVEL': Config.LOG_LEVEL,
                    'LOG_DIR': Config.LOG_DIR
                }
            }
        })
        
        # Example method calls
        method01()
        method02()
        
        logger.info("Application started successfully")
        
    except Exception as e:
        logger.critical(
            "Application failed to start",
            exc_info=True,
            extra={
                'data': {
                    'error': str(e),
                    'type': type(e).__name__
                }
            }
        )
        raise

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logger.critical(
            "애플리케이션이 예기치 않게 종료되었습니다",
            exc_info=True,
            extra={
                'data': {
                    'error': str(e),
                    'type': type(e).__name__
                }
            }
        )
        sys.exit(1)
