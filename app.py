from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!doctype html>
    <html lang="en">
      <head>
        <title>Simple Calculator</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
      </head>
      <body class="bg-light">
        <div class="container mt-5">
          <div class="card shadow p-4">
            <h2 class="text-center mb-4">🧮 Simple Calculator</h2>
            <form action="/calculate" method="post">
              <div class="mb-3">
                <label class="form-label">Number 1:</label>
                <input type="text" name="num1" class="form-control" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Number 2:</label>
                <input type="text" name="num2" class="form-control" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Operation (+, -, *, /):</label>
                <input type="text" name="op" class="form-control" required>
              </div>
              <div class="text-center">
                <button type="submit" class="btn btn-primary">Calculate</button>
              </div>
            </form>
          </div>
        </div>
      </body>
    </html>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
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
    except Exception as e:
        result = f"Error: {str(e)}"

    return f'''
    <!doctype html>
    <html lang="en">
      <head>
        <title>Result</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
      </head>
      <body class="bg-light">
        <div class="container mt-5">
          <div class="card shadow p-4 text-center">
            <h2 class="mb-4">Calculation Result</h2>
            <h3 class="text-success">{result}</h3>
            <a href="/" class="btn btn-secondary mt-4">🔙 Try Again</a>
          </div>
        </div>
      </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
