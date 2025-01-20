import unittest

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
        assert Category.product_count == 0
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.category.add_product(self.product3)
        assert Category.product_count == 3
        assert Category.category_count == 1

    """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
    Iphone 15, 210000.0 руб. Остаток: 8 шт.
    Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."""

    def test_products(self):
        assert self.category.products == (
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
            "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        )
