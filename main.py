from flask import Flask 
app = Flask(__name__)
@app.route('/calk/')
def calculator():
    a = int()
    b = int()
    plus = a+b
    minus = a-b
    multiply = a*b
    divide = a//b

    return plus, minus, multiply, divide

app.run()