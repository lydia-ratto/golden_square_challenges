from lib.dish import *

def test_dishes_list_created():
    dish = Dish('Margherita', 10)

    assert dish is not None

def test_dishname_and_price():
    dish = Dish('Margherita', 10)

    assert dish.name == 'Margherita'
    assert dish.price == 10

def test_dish_available():
    dish = Dish('Margherita', 10)

    dish.available == True

def test_dish_not_available():
    dish = Dish('Margherita', 10)

    dish.not_available()

    dish.available == False