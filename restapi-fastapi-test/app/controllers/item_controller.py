from fastapi import APIRouter, Response, status
from app.schemas.item_schema import ItemSchema
from app.services.item_service import ItemService
import json

router = APIRouter(prefix="/items", tags=["items"])
service = ItemService()

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemSchema):
    result = service.create_item(item)
    return Response(
        content=json.dumps(result),
        media_type="application/json",
        status_code=status.HTTP_201_CREATED
    )

@router.get("", status_code=status.HTTP_200_OK)
async def read_items():
    result = service.get_all_items()
    return Response(
        content=json.dumps(result),
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: int):
    result = service.get_item_by_id(item_id)
    if result is None:
        return Response(
            content=json.dumps({"error": "Item not found"}),
            media_type="application/json",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return Response(
        content=json.dumps(result),
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

@router.put("/{item_id}", status_code=status.HTTP_200_OK)
async def update_item(item_id: int, item: ItemSchema):
    result = service.update_item(item_id, item)
    if result is None:
        return Response(
            content=json.dumps({"error": "Item not found"}),
            media_type="application/json",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return Response(
        content=json.dumps(result),
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )

@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
async def delete_item(item_id: int):
    result = service.delete_item(item_id)
    if result is None:
        return Response(
            content=json.dumps({"error": "Item not found"}),
            media_type="application/json",
            status_code=status.HTTP_404_NOT_FOUND
        )
    return Response(
        content=json.dumps({"message": "Item deleted", "item": result}),
        media_type="application/json",
        status_code=status.HTTP_200_OK
    )
