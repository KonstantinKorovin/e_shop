import unittest
from unittest.mock import patch

from src.products import Product


def test_product_init(first_product, second_product):
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8

    assert second_product.name == "Xiaomi Redmi Note 11"
    assert second_product.description == "1024GB, Синий"
    assert second_product.price == 31000.0
    assert second_product.quantity == 14


def test_product_first(add_product_first, add_product_second):
    assert add_product_first.name == "Samsung Galaxy S23 Ultra"
    assert add_product_first.description == "256GB, Серый цвет, 200MP камера"
    assert add_product_first.price == 180000.0
    assert add_product_first.quantity == 5

    assert add_product_second.name == "Iphone 15"
    assert add_product_second.description == "256GB, Серый цвет, 48MP камера"
    assert add_product_second.price == 190000.0
    assert add_product_second.quantity == 3


class TestProduct(unittest.TestCase):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    def test_price_getter(self):
        """Тест геттера цены"""
        self.assertEqual(self.product1.price, 180000.0)

    def test_price_setter_increase(self):
        """Тест сеттера цены при увеличении цены"""
        self.product1.price = 190000.0
        self.assertEqual(self.product1.price, 190000.0)

    @patch("builtins.input", return_value="y")
    def test_price_setter_decrease_confirm_yes(self, mock_input):
        """Тест сеттера цены при уменьшении цены с подтверждением пользователя"""
        self.product2.price = 100
        self.assertEqual(self.product2.price, 100)
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="n")
    def test_price_setter_decrease_confirm_no(self, mock_input):
        """Тест сеттера цены при уменьшении цены без подтверждения пользователя"""
        self.product3.price = 80.0
        self.assertEqual(self.product3.price, 31000.0)
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="y")
    def test_price_setter_decrease_invalid_price(self, mock_input):
        """Тест сеттера цены при попытке установить нулевую или отрицательную цену"""
        with patch("builtins.print") as mock_print:
            self.product3.price = -50.0
            self.assertEqual(self.product3.price, 31000.0)
            mock_print.assert_any_call("Цена не должна быть нулевая или отрицательная!")
            mock_input.assert_called_once()

    def test_price_setter_no_change(self):
        """Тест сеттера цены при установке той же цены"""
        self.product2.price = 210000.0
        self.assertEqual(self.product2.price, 210000.0)
