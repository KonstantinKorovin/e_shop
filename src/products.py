from abc import ABC, abstractmethod
from multiprocessing.managers import Value
from typing import Any


class BaseProduct(ABC):
    """Базовое описание продукта"""

    @abstractmethod
    def __init__(self) -> None:
        pass


class MixinProduct:

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinProduct, BaseProduct):
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    @classmethod
    def new_product(cls, dict_product: dict) -> "Product":
        """Класс-метод который принимет на вход параметры товара и возвращает созданный объект класса Product"""
        product = cls(**dict_product)
        return product

    def __str__(self) -> str:
        """Метод для работы с приватным атрибутом '__products' который выводит информацию в заданном формате"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float | str:
        """Магический метод для вывода стоимости всех товаров на складе"""
        if type(self) is type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError("Невозможно сложить продукты разной категории")

    @property
    def price(self) -> float:
        """Метод возвращает атрибут типа 'private'"""
        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        """Метод-сеттер для работы с приватным атрибутом '__price' который в зависимости от
        полученного аргумента выполняет соответствующую логику"""
        if (new_price > self.__price) > 0:
            self.__price = new_price
        elif (new_price < self.__price) > 0:
            print('Введите "y" для уменьшения цены или любой другой символ для отмены')
            user_input = input()
            if user_input.lower() == "y" and new_price > 0:
                self.__price = new_price
            elif new_price <= 0:
                print("Цена не должна быть нулевая или отрицательная!")
                self.__price = self.__price


class Smartphone(Product):
    """Класс для представления смартфона"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления травки"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
