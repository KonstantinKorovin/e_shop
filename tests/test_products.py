def test_product(first_product, second_product):
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8

    assert second_product.name == "Xiaomi Redmi Note 11"
    assert second_product.description == "1024GB, Синий"
    assert second_product.price == 31000.0
    assert second_product.quantity == 14
