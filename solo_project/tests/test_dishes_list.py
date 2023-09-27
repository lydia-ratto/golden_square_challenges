from lib.dishes_list import *
from lib.dish_formatter import *
from unittest.mock import Mock

def test_dishes_list_created():
    dishes_list = DishesList()

    assert dishes_list is not None

def test_dish_added_to_list():
    dishes_list = DishesList()
    dish = Mock()

    dishes_list.add(dish)

    assert dishes_list.all() == [dish]

def test_dishes_list_format():
    dishes_list = DishesList()
    dish_formatter = Mock()
    dish_formatter.format.return_value = 'Pizza Margherita, £10'
    dishes_list.add(dish_formatter.format())

    assert dishes_list.all() == ['Pizza Margherita, £10']

def test_all_available():
    dishes_list = DishesList()
    dish_1 = Mock()
    dish_1.available = True
    dish_2 = Mock()
    dishes_list.add(dish_1)
    dishes_list.add(dish_2)

    dish_2.available = False

    assert dishes_list.all_available() == [dish_1]

def test_selected_multiple_available_dishes():
    dishes_list = DishesList()
    dish_1 = Mock()
    dish_2 = Mock()
    dishes_list.add(dish_1)
    dishes_list.add(dish_2)
    dish_1.name = 'Pizza Margherita'
    dish_2.name = 'Lasagna'
    dish_1.price = '10'
    dish_2.price = '8'
    dish_1.available = True
    dish_2.available = True

    assert dishes_list.select_available('Margherita, Lasagna') == ['Pizza Margherita added', 'Lasagna added']

def test_receipt_shown():
    dishes_list = DishesList()
    dish_1 = Mock()
    dish_2 = Mock()
    dishes_list.add(dish_1)
    dishes_list.add(dish_2)
    dish_1.name = 'Pizza Margherita'
    dish_2.name = 'Lasagna'
    dish_1.price = 10
    dish_2.price = 8
    dish_1.available = True
    dish_2.available = True
    dishes_list.select_available('Margherita, Lasagna')
    
    assert dishes_list.show_receipt() == ['Pizza Margherita - £10', 'Lasagna - £8', 'TOTAL: £18']


