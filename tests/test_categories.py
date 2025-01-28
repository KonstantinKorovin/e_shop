import unittest

import pytest

from src.categories import Category
from src.products import Product


class TestCategory(unittest.TestCase):
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    def test_init_category(self):
        mock_category = self.category
        assert mock_category.name == "Смартфоны"
        assert mock_category.description == (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        )

    def test_add_product(self):
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.category.add_product(self.product3)
        assert Category.category_count == 1
        with pytest.raises(TypeError):
            assert self.category.add_product("No product") == "TypeError: Невозможно добавить продукт"

    def test_products(self):
        assert self.category.products == [
            "Samsung Galaxy S23 Ultra 256GB, Серый цвет, 200MP камера",
            "Iphone 15 512GB, Gray space",
            "Xiaomi Redmi Note 11 1024GB, Синий",
        ]


def test_str_products():
    assert Category.product_count == 0
    my_products = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)],
    )
    assert str(my_products) == "Смартфоны, количество продуктов: 5"
    assert Category.product_count == 1


def test_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    category2 = Category("Пустая категория", "Категория без продуктов", [])
    assert category1.middle_price() == 140333.33333333334
    assert category2.middle_price() == 'В списке должен быть хотя бы один товар'


