from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Simple Calculator</h1>
        <form action="/calculate" method="post">
            Number 1: <input type="text" name="num1"><br><br>
            Number 2: <input type="text" name="num2"><br><br>
            Operation (+, -, *, /): <input type="text" name="op"><br><br>
            <input type="submit" value="Calculate">
        </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    op = request.form['op']

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
    else:
        result = 'Invalid operation'

    return f'<h2>Result: {result}</h2><br><a href="/">Try Again</a>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
