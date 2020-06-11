from typing import List

class Dish:

    def __init__(self, name: str, ingredients: list):
        self.name = name
        self.ingredients = ingredients


    def __eq__(self, other):
        return self.name == other.name


    def __hash__(self):
        return hash(self.name)

    def can_make(self, ingredients: List[str]) -> bool:
        given_ingredients = self.make_dict(ingredients)
        my_ingredients = self.make_dict(self.ingredients)
        for key, val in my_ingredients.items():
            if key not in given_ingredients or given_ingredients[key] < val:
                return False
        return True

    def make_dict(self, ingredients: List[str]):
        d = {}
        for i in ingredients:
            if i not in d:
                d[i] = 0
            d[i] += 1
        return d

