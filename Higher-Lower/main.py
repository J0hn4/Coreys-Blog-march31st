from flask import Flask

app = Flask(__name__)


def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0],args[1],args[2])
        print(f"It returned: {result} ")
    return wrapper_function

# Use the decorator 👇

@logging_decorator
def random_int():
    return random_int()


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)