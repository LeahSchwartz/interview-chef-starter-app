from typing import List


class CuisineKeeper:

    def __init__(self):
        self.dishes = set()

    def add_dish(self, dish: str) -> None:
        self.dishes.add(dish)

    def get_dishes(self) -> List[str]:
        return list(self.dishes)

    def remove_dish(self, dish: str) -> None:
        if self.has_dish(dish):
            self.dishes.remove(dish)

    def has_dish(self, dish) -> bool:
        return dish in self.dishes
