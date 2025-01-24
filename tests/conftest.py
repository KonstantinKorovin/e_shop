import pytest

from src.products import Product


# Фикстуры для products.py
@pytest.fixture()
def first_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture()
def second_product():
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture()
def add_product_first():
    return Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture()
def add_product_second():
    return Product.new_product(
        {
            "name": "Iphone 15",
            "description": "256GB, Серый цвет, 48MP камера",
            "price": 190000.0,
            "quantity": 3,
        }
    )
