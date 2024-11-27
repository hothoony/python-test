from typing import Optional, Dict, List
from app.models.item_model import ItemModel
from app.schemas.item_schema import ItemSchema
import logging

logger = logging.getLogger(__name__)

class ItemService:
    def __init__(self):
        self.model = ItemModel()
    
    def create_item(self, item: ItemSchema) -> Dict:
        logger.debug(f"Creating new item: {item.model_dump()}")
        result = self.model.create(item)
        logger.info(f"Successfully created item with id: {result['id']}")
        return result
    
    def get_all_items(self) -> List[Dict]:
        logger.debug(f"Retrieving all items. Current count: {len(self.model.items)}")
        return self.model.get_all()
    
    def get_item_by_id(self, item_id: int) -> Optional[Dict]:
        logger.debug(f"Attempting to retrieve item with id: {item_id}")
        item = self.model.get_by_id(item_id)
        if item is None:
            logger.warning(f"Item not found with id: {item_id}")
        else:
            logger.info(f"Successfully retrieved item: {item}")
        return item
    
    def update_item(self, item_id: int, item: ItemSchema) -> Optional[Dict]:
        logger.debug(f"Attempting to update item {item_id} with data: {item.model_dump()}")
        result = self.model.update(item_id, item)
        if result is None:
            logger.error(f"Failed to update: item not found with id: {item_id}")
        else:
            logger.info(f"Successfully updated item {item_id}")
        return result
    
    def delete_item(self, item_id: int) -> Optional[Dict]:
        logger.debug(f"Attempting to delete item with id: {item_id}")
        result = self.model.delete(item_id)
        if result is None:
            logger.error(f"Failed to delete: item not found with id: {item_id}")
        else:
            logger.info(f"Successfully deleted item: {result}")
        return result
