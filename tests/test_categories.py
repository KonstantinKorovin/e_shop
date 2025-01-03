def test_categories(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )

    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert first_category.product_count == 3
    assert second_category.product_count == 3