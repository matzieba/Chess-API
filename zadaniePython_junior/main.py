from flask import Flask, jsonify
from classes import King, Queen, Rook, Bischop, Knight, Pawn

app = Flask(__name__)


@app.route("/")
def home():
    return "hello world!"


def creating_dict_moves(data, figure, current_field):
    moves = data.list_available_moves()
    dict = {
        "availableMoves": moves,
        "figure": figure,
        "currentfield": current_field,
        "error": "null",
    }
    return dict


@app.route("/api/v1/<string:figure>/<string:current_field>")
def avilable_moves(figure, current_field):
    try:
        if figure == "king":
            data = King(current_field)
            dict_to_publish = creating_dict_moves(data, figure, current_field)
            return jsonify(dict_to_publish)
        elif figure == "queen":
            data = Queen(current_field)
            dict_to_publish = creating_dict_moves(data, figure, current_field)
            return jsonify(dict_to_publish)
        elif figure == "rook":
            data = Rook(current_field)
            dict_to_publish = creating_dict_moves(data, figure, current_field)
            return jsonify(dict_to_publish)
        elif figure == "bischop":
            data = Bischop(current_field)
            dict_to_publish = creating_dict_moves(data, figure, current_field)
            return jsonify(dict_to_publish)
        elif figure == "knight":
            data = Knight(current_field)
            dict_to_publish = creating_dict_moves(data, figure, current_field)
            return jsonify(dict_to_publish)
        elif figure == "Pawn":
            data = Pawn(current_field)
            dict_to_publish = creating_dict_moves(data, figure, current_field)
            return jsonify(dict_to_publish)
        else:
            return (
                jsonify(
                    error={
                        "Not found": "Sorry,"
                                     "the figure "
                                     "you are looking "
                                     "for was not found"
                    }
                ),
                404,
            )
    except ValueError:
        dict = {
            "availableMoves": [],
            "figure": figure,
            "currentfield": "field do not exist",
        }
        return jsonify(error={"No such field on the board": dict}), 409


def creating_dict_valid(data, figure, current_field, dest_field):
    validation = data.validate_move(dest_field)
    dict_to_publish = {
        "MoveValid": validation,
        "figure": figure,
        "currentfield": current_field,
        "destintion_field": dest_field,
        "error": "null",
    }
    return dict_to_publish


@app.route("/api/v1/<string:figure>/"
           "<string:current_field>/<string:dest_field>")
def move_valid(figure, current_field, dest_field):
    try:
        if figure == "king":
            data = King(current_field)
            dict_to_publish = creating_dict_valid(
                data, figure, current_field, dest_field
            )
            return jsonify(dict_to_publish)

        elif figure == "queen":
            data = Queen(current_field)
            dict_to_publish = creating_dict_valid(
                data, figure, current_field, dest_field
            )
            return jsonify(dict_to_publish)
        elif figure == "rook":
            data = Rook(current_field)
            dict_to_publish = creating_dict_valid(
                data, figure, current_field, dest_field
            )
            return jsonify(dict_to_publish)
        elif figure == "bischop":
            data = Bischop(current_field)
            dict_to_publish = creating_dict_valid(
                data, figure, current_field, dest_field
            )
            return jsonify(dict_to_publish)
        elif figure == "knight":
            data = Knight(current_field)
            dict_to_publish = creating_dict_valid(
                data, figure, current_field, dest_field
            )
            return jsonify(dict_to_publish)
        elif figure == "pawn":
            data = Pawn(current_field)
            dict_to_publish = creating_dict_valid(
                data, figure, current_field, dest_field
            )
            return jsonify(dict_to_publish)
        else:
            return (
                jsonify(
                    error={
                        "Not found":
                            "Sorry, the figure you"
                            " are looking for was not found"
                    }
                ),
                404,
            )
    except ValueError:
        dict = {
            "availableMoves": [],
            "figure": figure,
            "currentfield": "field do not exist",
        }
        return jsonify(error={"No such field on the board": dict}), 409


if __name__ == "__main__":
    app.run(debug=True)
