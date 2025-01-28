from typing import Any

from src.products import LawnGrass, Product, Smartphone


class Category:
    """Класс для представления категории продуктов"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация категорий продуктов"""
        self.name = name
        self.description = description
        self.__products = products
        if self.name not in self.__products:
            Category.category_count += 1
        for _ in self.__products:
            Category.product_count += 1

    def add_product(self, product: Any) -> None:
        """Метод для работы с приватным атрибутом '__products' который добавляет новый продукт в список"""
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Невозможно добавить продукт")

    @property
    def products(self) -> list:
        """Метод выводит информацию о продукте в определнном формате"""
        return [f"{product.name} {product.description}" for product in self.__products]

    def __str__(self) -> str:
        """Метод выводит строковое представление о количестве продуктов"""
        counter_quantity = 0
        for x in self.__products:
            counter_quantity += x.quantity
        return f"{self.name}, количество продуктов: {counter_quantity}"

    def middle_price(self) -> float:
        try:
            price_product_list = [product.price for product in self.__products]
            return sum(price_product_list) / len(self.__products)
        except ZeroDivisionError:
            return 0


"""if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
        "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())"""
