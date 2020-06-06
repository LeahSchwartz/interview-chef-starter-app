from flask import Flask, request, jsonify
from cuisine_keeper import CuisineKeeper

app = Flask(__name__)

keeper = CuisineKeeper()


@app.route('/cuisine-keeper/dishes/all', methods=['GET'])
def all_dishes():
    return jsonify({"dishes": keeper.get_dishes()})

@app.route('/cuisine-keeper/dishes', methods=['POST', 'DELETE'])
def new_dish():
    if request.method == 'POST':
        content = request.json
        print(content['dish'])
        result = {"response": "Success"}
        if keeper.has_dish(content['dish']):
            result["message"] = content['dish'] + " was already in your dishes!"
        else:
            keeper.add_dish(content['dish'])
        return jsonify(result), 200
    if request.method == 'DELETE':
        content = request.json
        print(content['dish'])
        result = {"response": "Success"}
        if not keeper.has_dish(content['dish']):
            result["message"] = content['dish'] + " was not in your dishes!"
        else:
            keeper.remove_dish(content['dish'])
        return jsonify(result), 200


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Cuisine Keeper</h1>
<p>A prototype API for storing and retrieving all the best cuisine.</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    app.run()



