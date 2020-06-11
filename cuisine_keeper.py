
class CuisineKeeper:

    def __init__(self):
        self.dishes = set()

    def add_dish(self, dish):
        self.dishes.add(dish)

    def get_dishes(self):
        return list(self.dishes)

    def remove_dish(self, dish):
        if self.has_dish(dish):
            self.dishes.remove(dish)

    def has_dish(self, dish):
        return dish in self.dishes
