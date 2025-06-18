#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 로깅 설정 파일

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import time

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
    log_format = '%(asctime)s [%(levelname)-7s] %(filename)-20s:%(lineno)-4d - %(message)s'
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
        
        # when='midnight'은 "자정을 기준점으로 삼는다"는 의미이고, 
        # atTime은 "그 기준점으로부터 얼마나 지연시킬지"를 지정하는 것입니다.
        file_handler = TimedRotatingFileHandler(
            log_file,
            interval=1,         # 1일 간격으로 로테이션
            when='midnight',    # 자정을 기준점으로 설정
            atTime=time(0, 0),  # 매일 자정 00:00에 로테이션
            # backupCount=30,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        
        # 로그 파일명 포맷: app.YYYY-MM-DD.log
        def namer(default_name):
            # default_name은 logs/app.log.YYYYMMDD 형태
            # logs/app.YYYY-MM-DD.log 형태로 변경
            directory = os.path.dirname(default_name)  # logs
            filename = os.path.basename(default_name)  # app.log.YYYYMMDD
            
            # app.log.YYYYMMDD에서 날짜 부분 추출
            parts = filename.split('.')
            if len(parts) >= 3:
                date_part = parts[-1]  # YYYYMMDD
                if len(date_part) == 8 and date_part.isdigit():
                    # YYYYMMDD를 YYYY-MM-DD로 변환
                    formatted_date = f"{date_part[:4]}-{date_part[4:6]}-{date_part[6:8]}"
                    return os.path.join(directory, f"app.{formatted_date}.log")
            
            # 기본값 반환
            return default_name
        
        file_handler.namer = namer
        file_handler.suffix = "%Y%m%d"  # 로그 파일명에 날짜 추가 (namer에서 변환됨)
        # file_handler.suffix = "%Y%m%d"  # 로그 파일명에 날짜 추가
        logger.addHandler(file_handler)
        logger.debug(f'로그 파일이 다음 위치에 생성됩니다: {log_file}')
    except Exception as e:
        logger.warning(f'파일 로그 초기화 실패: {e}')
    
    return logger
