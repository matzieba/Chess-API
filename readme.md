#Chess move Validator with API-Layer

#tech: Flask,

## creating an API with data in json format, depending on request returns list of moves or validate if the move is possbile.

### url for moves list : http://localhost:8000/api/v1/<string:figure>/<string:current_field>
####where
<string:figure>
is a name of the figure given as follows: king, queen, rook, bischop, knight, pawn 
<string:current_field>
is alphanumeric field markup of current field, letter has to be written capitalized
####eg: http://localhost:8000/api/v1/king/A7

### url for validation : http://localhost:8000/api/v1/<string:figure>/<string:current_field>/<string:dest_field>
####where
<string:figure>
is a name of the figure given as follows: king, queen, rook, bischop, knight, pawn 
<string:current_field>
is alphanumeric field markup of current field, letter has to be written capitalized
<string:dest_field>is alphanumeric field markup of destination, letter has to be written capitalized
####eg: http://localhost:8000/api/v1/king/A7/A8

### eg : http://localhost:8000/api/v1/king/A7
response:200, {
  "availableMoves": [
    "A8", 
    "B8", 
    "B6", 
    "A6", 
    "B7"
  ], 
  "currentfield": "A7", 
  "error": "null", 
  "figure": "king"
}
