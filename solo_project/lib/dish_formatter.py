class DishFormatter:
    def __init__(self, dish):
        self.dish = dish
    
    def format(self):
        return f"{self.dish.name}, £{self.dish.price}"