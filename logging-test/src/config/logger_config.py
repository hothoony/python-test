#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 로깅 설정 파일

import logging
import os
from logging.handlers import TimedRotatingFileHandler

def setup_logger(name=__name__):
    """로거 설정 및 반환"""
    logger = logging.getLogger(name)
    
    # 이미 핸들러가 설정되어 있으면 기존 로거 반환
    if logger.handlers:
        return logger
    
    # 로그 레벨 설정 (환경변수에서 가져오거나 기본값 INFO 사용)
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logger.setLevel(log_level)
    
    # 로그 포맷 (고정 폭 로그 레벨)
    # log_format = '%(asctime)s %(filename)s:%(lineno)d - [%(levelname)-7s] %(message)s'
    log_format = '%(asctime)s %(filename)-20s:%(lineno)-4d - [%(levelname)-7s] %(message)s'
    formatter = logging.Formatter(log_format)
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 파일 핸들러 (매일 자정에 로테이션, 최대 30일 보관)
    try:
        # 프로젝트 루트 디렉토리 계산 (src의 부모 디렉토리)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # 로그 디렉토리 생성
        log_dir = os.path.join(project_root, 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        # 로그 파일 경로 설정
        log_file = os.path.join(log_dir, 'app.log')
        
        file_handler = TimedRotatingFileHandler(
            log_file,
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        file_handler.suffix = "%Y%m%d"  # 로그 파일명에 날짜 추가
        logger.addHandler(file_handler)
        logger.debug(f'로그 파일이 다음 위치에 생성됩니다: {log_file}')
    except Exception as e:
        logger.warning(f'파일 로그 초기화 실패: {e}')
    
    return logger
