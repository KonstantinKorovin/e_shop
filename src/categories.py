from typing import Any

from src.products import Product


class Category:
    """Класс для представления категории продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация категорий продуктов"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        if name not in self.name:
            Category.category_count += 1

    def add_product(self, product: Any) -> None:
        """Метод для работы с приватным атрибутом '__products' который добавляет новый продукт в список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        return [f"{product.name} {product.description}" for product in self.__products]

    def __str__(self) -> str:
        counter_quantity = 0
        for x in self.__products:
            counter_quantity += x.quantity
        return f"{self.name}, количество продуктов: {counter_quantity}"


'''if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)'''
