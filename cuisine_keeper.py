from typing import List

from dish import Dish


class CuisineKeeper:

    def __init__(self):
        self.dishes = set()

    def add_dish(self, dish: Dish) -> None:
        self.dishes.add(dish)

    def get_dishes(self) -> List[Dish]:
        return list(self.dishes)

    def remove_dish(self, dish: Dish) -> None:
        if self.has_dish(dish):
            self.dishes.remove(dish)

    def has_dish(self, dish: Dish) -> bool:
        return dish in self.dishes

    def get_matching_dishes(self, ingredients: List[str]) -> List[Dish]: # O(n) * O(i)
        dishes = []
        for dish in self.dishes: # O(n)
            if dish.can_make(ingredients): # O(i)
                dishes.append(dish)
        return dishes

