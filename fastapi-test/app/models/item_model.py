from typing import Optional, Dict, List
from app.schemas.item_schema import ItemSchema

class ItemModel:
    def __init__(self):
        self.items: List[Dict] = []
    
    def create(self, item: ItemSchema) -> Dict:
        item_dict = item.model_dump()
        self.items.append(item_dict)
        return {"id": len(self.items) - 1, **item_dict}
    
    def get_all(self) -> List[Dict]:
        return self.items
    
    def get_by_id(self, item_id: int) -> Optional[Dict]:
        if 0 <= item_id < len(self.items):
            return self.items[item_id]
        return None
    
    def update(self, item_id: int, item: ItemSchema) -> Optional[Dict]:
        if 0 <= item_id < len(self.items):
            item_dict = item.model_dump()
            self.items[item_id] = item_dict
            return {"id": item_id, **item_dict}
        return None
    
    def delete(self, item_id: int) -> Optional[Dict]:
        if 0 <= item_id < len(self.items):
            return self.items.pop(item_id)
        return None
