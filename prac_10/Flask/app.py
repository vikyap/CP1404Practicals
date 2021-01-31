from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/<celsius>')
def c_to_f(celsius=""):
    celsius = float(celsius)
    fahrenheit = celsius * 9 / 5 + 32
    fahrenheit = str(fahrenheit)
    return fahrenheit


if __name__ == '__main__':
    app.run()
