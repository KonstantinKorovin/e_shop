import json
import os

from src.categories import Category
from src.products import Product


def read_json(path: str) -> list:
    """Функция чтения файла json"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list) -> list:
    """Функция преобразования списка словарей в обьекты класса 'Category'"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
