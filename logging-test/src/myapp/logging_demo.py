#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 로깅 데모 스크립트
# 로그 레벨을 변경해서 실행하기
#     LOG_LEVEL=DEBUG python3 src/myapp/logging_demo.py
#     LOG_LEVEL=INFO python3 src/myapp/logging_demo.py
#     LOG_LEVEL=WARNING python3 src/myapp/logging_demo.py
#     LOG_LEVEL=ERROR python3 src/myapp/logging_demo.py
# 모듈로 실행
#     LOG_LEVEL=DEBUG python3 -m src.myapp.logging_demo

import logging
import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = str(Path(__file__).parent.parent.absolute())
sys.path.insert(0, project_root)  # Insert at beginning to take precedence

try:
    from src.config.logger_config import setup_logger
except ImportError:
    # For direct execution
    from config.logger_config import setup_logger

def main():
    # 로거 초기화 (환경변수 LOG_LEVEL으로 설정, 기본값: INFO)
    logger = setup_logger()
    
    # 애플리케이션 시작 로그
    logger.info("애플리케이션 시작")
    
    # 로그 레벨별 예제 메시지
    logger.debug("디버깅을 위한 상세 정보")
    logger.info("정보성 메시지")
    logger.warning("경고가 발생했습니다")
    logger.error("오류가 발생했습니다")
    
    # 예외 처리 예제
    try:
        result = 10 / 0
    except Exception as e:
        logger.info("--------------------------------")
        logger.exception("오류 발생: %s", str(e)) # 권장 방식
        logger.info("--------------------------------")
        logger.error("오류 발생: %s\n%s", str(e), traceback.format_exc())
        logger.info("--------------------------------")
    
    # 로그 레벨 정보 출력
    level_name = logging.getLevelName(logger.getEffectiveLevel())
    logger.info(f"현재 로그 레벨: {level_name}")
    logger.info("애플리케이션 종료")

if __name__ == "__main__":
    main()
