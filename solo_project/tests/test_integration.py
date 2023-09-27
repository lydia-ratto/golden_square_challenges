from lib.dishes_list import *
from lib.dish import *

def test_dishes_list_with_dish():
    dishes_list = DishesList()
    dish = Dish('Margherita', 10)
    dishes_list.add(dish)

    assert dishes_list.all() == [dish]
