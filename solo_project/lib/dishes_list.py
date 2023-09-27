
class DishesList:
    def __init__(self):
        self.dishes_list = []
        self.ordered = False

    def add(self, dish):
        self.dishes_list.append(dish)

    def all(self):
        return self.dishes_list
    
    def all_available(self):
        self.available_dishes = list(filter(lambda dish: dish.available is True, self.dishes_list))
        return self.available_dishes

    def select_available(self, dish_names):
        available_dishes = self.all_available()
        if not available_dishes:
            return 'No dishes are available'

        self.selected_dishes = []
        select_statuses = []
        dish_names = dish_names.split(',')

        for given_dish_name in dish_names:
            matching_dishes = [
                dish for dish in available_dishes
                if given_dish_name.strip() in dish.name
            ]
            if matching_dishes:
                for dish in matching_dishes:
                    self.selected_dishes.extend(matching_dishes)
                    select_statuses.append(f'{dish.name} added')
            else:
                select_statuses.append(given_dish_name.strip() + ' not available')

        return select_statuses


    def show_receipt(self):
        dish_prices = [dish.price for dish in self.selected_dishes]
        print(dish_prices)
        total_price = sum(dish_prices)
        dish_details = [
            f'{dish.name} - £{dish.price}' for dish in self.selected_dishes
        ]
        dish_details.append(f"TOTAL: £{total_price}")
        return dish_details

    def is_ordered(self):
        self.ordered = True
