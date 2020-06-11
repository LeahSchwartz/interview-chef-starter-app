from cuisine_keeper import CuisineKeeper
from dish import Dish

from flask import Flask, request, jsonify

from typing import Tuple
from typing import Any

app = Flask(__name__)

keeper = CuisineKeeper()


@app.route('/cuisine-keeper/dishes/all', methods=['GET'])
def all_dishes() -> Tuple[Any, int]:
    dishes = keeper.get_dishes()
    response = {"dishes": []}
    for dish in dishes:
        response["dishes"].append(
            {"name": dish.name, "ingredients": list(dish.ingredients)}
        )
    return jsonify(response), 200

@app.route('/cuisine-keeper/dishes', methods=['POST', 'DELETE'])
def new_dish() -> Tuple[Any, int]:
    content = request.json
    code = 200
    response = {"result": ''}
    try:
        dish_dict = content['dish']
        name = dish_dict['name']
        ingredients = []
        if "ingredients" in dish_dict:
            ingredients = dish_dict['ingredients']
        dish = Dish(name, ingredients)
        if request.method == 'POST':
            if keeper.has_dish(dish):
                response['result'] = f'{dish.name} was already in your dishes!'
            else:
                keeper.add_dish(dish)
                response['result'] = f'{dish.name} was added to your dishes!'
        if request.method == 'DELETE':
            if not keeper.has_dish(dish):
                response['result'] = f'{dish.name} was not in your dishes!'
            else:
                keeper.remove_dish(dish)
                response['result'] = f'{dish.name} was removed from your dishes!'
    except KeyError:
        response['result'] = "Improperly formatted dish data"
        code = 400
    return jsonify(response), code

@app.route('/cuisine-keeper/dishes/find-new', methods=['POST']) # O(n) * O(i)
def makeable_dishes() -> Tuple[Any, int]:
    content = request.json
    code = 200
    response = {"result": []}
    try:
        ingredients = content['ingredients']
        dishes = keeper.get_matching_dishes(ingredients) # O(n) * O(i)
        for dish in dishes: # O(n)
            response["result"].append(dish.name)
    except KeyError:
        response['result'] = "Improperly formatted ingredient data"
        code = 400
    return jsonify(response), code





if __name__ == '__main__':
    app.run()



