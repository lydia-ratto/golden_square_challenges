from lib.dish import *
from lib.dish_formatter import *
from unittest.mock import Mock

def test_dish_formatter():
    mock_dish = Mock()
    mock_dish.name = 'Pizza Margherita'
    mock_dish.price = 10
    dish_formatter = DishFormatter(mock_dish)

    assert dish_formatter.format() == 'Pizza Margherita, £10'