import itertools
import threading
from datetime import datetime, timezone

_lock = threading.Lock()
_id_counter = itertools.count(1)

# The "database": a list of inventory item dicts.
_inventory: list[dict] = []


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _next_id() -> int:
    return next(_id_counter)


def reset():
    """Clear all data and reset the id counter. Used mainly by tests."""
    global _id_counter
    with _lock:
        _inventory.clear()
        _id_counter = itertools.count(1)


def list_items() -> list[dict]:
    with _lock:
        return list(_inventory)


def get_item(item_id: int) -> dict | None:
    with _lock:
        for item in _inventory:
            if item["id"] == item_id:
                return dict(item)
    return None


def create_item(data: dict) -> dict:
    """
    Create a new inventory item.

    Expected/optional fields in `data`:
        name (str, required)
        brand (str, optional)
        barcode (str, optional)
        price (float, optional, default 0.0)
        quantity (int, optional, default 0)
        category (str, optional)
        ingredients_text (str, optional)
    """
    with _lock:
        item = {
            "id": _next_id(),
            "name": data["name"],
            "brand": data.get("brand", ""),
            "barcode": data.get("barcode", ""),
            "price": float(data.get("price", 0.0)),
            "quantity": int(data.get("quantity", 0)),
            "category": data.get("category", ""),
            "ingredients_text": data.get("ingredients_text", ""),
            "created_at": _now(),
            "updated_at": _now(),
        }
        _inventory.append(item)
        return dict(item)


def update_item(item_id: int, data: dict) -> dict | None:
    """Partially update an existing item (PATCH semantics)."""
    with _lock:
        for item in _inventory:
            if item["id"] == item_id:
                for field in (
                    "name",
                    "brand",
                    "barcode",
                    "price",
                    "quantity",
                    "category",
                    "ingredients_text",
                ):
                    if field in data:
                        item[field] = data[field]
                item["updated_at"] = _now()
                return dict(item)
    return None


def delete_item(item_id: int) -> bool:
    with _lock:
        for i, item in enumerate(_inventory):
            if item["id"] == item_id:
                del _inventory[i]
                return True
    return False