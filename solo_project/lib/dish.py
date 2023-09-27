class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.available = True
    
    def not_available(self):
        self.available = False