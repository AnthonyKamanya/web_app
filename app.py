from example_routes import apply_example_routes
import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/wave', methods =["GET"])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/submit', methods =["POST"])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f"Thanks {name}, you sent this message:{message}"


@app.route('/count_vowels', methods =["POST"])
def post_count_vowels():
    text = request.form['text']
    num_of_vowels=0
    for vowels in text:
        if vowels in "aieou":
            num_of_vowels +=1
    return f'There are {num_of_vowels} vowels in "{text}"'
# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# POST
# Returns Thanks Leo, you sent this message: "Hello world"
# Try it:
#   ; curl http://127.0.0.1:5001/submit


# @app.route('/submit', methods=['POST'])
# def post_submit():
#     name = request.form['name']
#     message = request.form['message']
#     return f'Thanks {name}, you sent this message: "{message}"'


# GET
# Returns I am waving at Leo
# Try it:
#   ; curl http://127.0.0.1:5001/wave


@app.route('/wave', methods=['GET'])
def wave():
    name = request.form['name']
    return f'I am waving at {name}'

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
