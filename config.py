import os

class Config:
    DEBUG = True
    JSON_SORT_KEYS = False

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_FILE = os.path.join(BASE_DIR, "inventory.json")

    OPENFOODFACTS_URL = "https://world.openfoodfacts.org/api/v0/product"