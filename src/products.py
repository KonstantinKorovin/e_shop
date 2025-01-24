class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product: dict) -> "Product":
        """Класс-метод который принимет на вход параметры товара и возвращает созданный объект класса Product"""
        product = cls(**dict_product)
        return product

    def __str__(self) -> str:
        """Метод для работы с приватным атрибутом '__products' который выводит информацию в заданном формате"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Магический метод для вывода стоимости всех товаров на складе"""
        return (self.__price * self.quantity) + (other.__price * other.quantity)

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
