from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from typing import Optional
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG 레벨로 변경하여 모든 로그를 볼 수 있도록 함
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Simple REST API")

# 데이터 모델 정의
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# 메모리에 데이터 저장
items = []

@app.get("/", status_code=status.HTTP_200_OK)  # 방법 1: 데코레이터에서 status_code 지정
async def read_root():
    logger.debug("logger debug")        # debug 레벨 로그
    logger.info("logger info")          # info 레벨 로그
    logger.warning("logger warning")    # warning 레벨 로그
    logger.error("logger error")        # error 레벨 로그
    logger.critical("logger critical")  # critical 레벨 로그
    
    # 방법 2: Response 객체 사용
    return Response(
        content='{"message": "Welcome to Simple REST API"}',
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

@app.post("/items")
async def create_item(item: Item):
    logger.debug(f"Received request to create item: {item.dict()}")  # DEBUG 레벨 로그
    
    items.append(item)
    
    logger.info(f"Successfully created item with id: {len(items) - 1}")  # INFO 레벨 로그
    
    return Response(
        content=f'{{"id": {len(items) - 1}, {item.dict()}}}',
        media_type="application/json",
        status_code=status.HTTP_201_CREATED
    )

@app.get("/items")
async def read_items():
    logger.debug(f"Retrieving all items. Current count: {len(items)}")  # DEBUG 레벨 로그
    
    return Response(
        content=f"{items}",
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    logger.debug(f"Attempting to retrieve item with id: {item_id}")  # DEBUG 레벨 로그
    
    if item_id < 0 or item_id >= len(items):
        logger.warning(f"Item not found with id: {item_id}")  # WARNING 레벨 로그
        return Response(
            content='{"error": "Item not found"}',
            media_type="application/json",
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    logger.info(f"Successfully retrieved item: {items[item_id]}")  # INFO 레벨 로그
    
    return Response(
        content=f"{items[item_id]}",
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.debug(f"Attempting to update item {item_id} with data: {item.dict()}")  # DEBUG 레벨 로그
    
    if item_id < 0 or item_id >= len(items):
        logger.error(f"Failed to update: item not found with id: {item_id}")  # ERROR 레벨 로그
        return Response(
            content='{"error": "Item not found"}',
            media_type="application/json",
            status_code=status.HTTP_404_NOT_FOUND
        )
    items[item_id] = item
    
    logger.info(f"Successfully updated item {item_id}")  # INFO 레벨 로그
    
    return Response(
        content=f'{{"id": {item_id}, {item.dict()}}}',
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.debug(f"Attempting to delete item with id: {item_id}")  # DEBUG 레벨 로그
    
    if item_id < 0 or item_id >= len(items):
        logger.error(f"Failed to delete: item not found with id: {item_id}")  # ERROR 레벨 로그
        return Response(
            content='{"error": "Item not found"}',
            media_type="application/json",
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    deleted_item = items.pop(item_id)
    
    logger.info(f"Successfully deleted item: {deleted_item}")  # INFO 레벨 로그
    
    return Response(
        content=f'{{"message": "Item deleted", "item": {deleted_item}}}',
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )
