1. Customer Journey

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

1. Design
class DishesList:

    def __init____():
        Params:
            none
        Return:
            none
        Side effects:
            create empty list
    
    def add():
        Params:
            dish name, as string
        Return:
            none
        Side effects:
            add dish to list    

    def all():
        Params:
            none
        Return:
            list of dishes with name and price

    def_all_available:
        Params:
            none
        Returns:
            list of dishes, where is_available is True

    def_select_available:
        Params:
            dish names
        Returns:
            none
        Side effects:
            store params of dishes in list
    
    def see_receipt:
        Params:
            none
        Returns:
            list of selected dishes with names and prices, as well as a total of the prices

class Dish:
    def __init__:
        Params:
            price: integer
            name: string
            available: boolean
        Returns:
            none
        Side effects:
            store param in variables

    def is_available:
        Params:
            none
        Returns:
            boolean, True if available, false otherwise

    

        
    

    
