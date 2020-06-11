from cuisine_keeper import CuisineKeeper

from flask import Flask, request, jsonify

from typing import Tuple
from typing import Any

app = Flask(__name__)

keeper = CuisineKeeper()


@app.route('/cuisine-keeper/dishes/all', methods=['GET'])
def all_dishes() -> Tuple[Any, int]:
    return jsonify({"dishes": keeper.get_dishes()}), 200

@app.route('/cuisine-keeper/dishes', methods=['POST', 'DELETE'])
def new_dish() -> Tuple[Any, int]:
    content = request.json
    code = 200
    response = {"result": ''}
    try:
        dish = content['dish']
        if request.method == 'POST':
            if keeper.has_dish(dish):
                response['result'] = f'{dish} was already in your dishes!'
            else:
                keeper.add_dish(dish)
                response['result'] = f'{dish} was added to your dishes!'
        if request.method == 'DELETE':
            if not keeper.has_dish(dish):
                response['result'] = f'{dish} was not in your dishes!'
            else:
                keeper.remove_dish(dish)
                response['result'] = f'{dish} was removed from your dishes!'
    except KeyError:
        response['result'] = "You didn't include a dish!"
        code = 400
    return jsonify(response), code


if __name__ == '__main__':
    app.run()



