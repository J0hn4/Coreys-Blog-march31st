from flask import Flask
import random

app = Flask(__name__)

def random_num():
    return random.randint(0,10)

magic_number = random_num()
print(magic_number)


# def (function):
#     def wrapper_function(*args, **kwargs):
#         print(f"You called {function.__name__}{args}")
#         result = function(args[0],args[1],args[2])
#         print(f"It returned: {result} ")
#     return wrapper_function


@app.route("/")
def hello():
    return "Hello. Guess a number between 1 and 10"




@app.route("/<int:number>")
def choice(number):
    if number == magic_number:
        return '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"><h1>Correct</h1>'
    elif magic_number > number:
        print("too low")
        return '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"><h1>Too Low</h1>'
    elif magic_number < number:
        print("too high")
        return '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"><h1>Too High</h1>'



if __name__ == "__main__":
    app.run(debug=True)