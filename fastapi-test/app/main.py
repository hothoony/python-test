from fastapi import FastAPI, Response, status
from .config.logger_config import setup_logger
from .controllers.item_controller import router as item_router
from .controllers.qna_controller import router as qna_router

# 로거 설정
logger = setup_logger()

# FastAPI 애플리케이션 생성
app = FastAPI(title="Simple REST API")

# 루트 엔드포인트
@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    logger.debug("logger debug")        # debug 레벨 로그
    logger.info("logger info")          # info 레벨 로그
    logger.warning("logger warning")    # warning 레벨 로그
    logger.error("logger error")        # error 레벨 로그
    logger.critical("logger critical")  # critical 레벨 로그
    
    return Response(
        content='{"message": "Welcome to Simple REST API"}',
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

# 라우터 등록
app.include_router(item_router)
app.include_router(qna_router)
