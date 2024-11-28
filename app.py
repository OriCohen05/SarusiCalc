from flask import Flask, request, jsonify, render_template
from operations import Calculator, Operation

app = Flask(__name__)
calculator = Calculator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    operand1 = data.get('operand1')
    operand2 = data.get('operand2')

    try:
        operation_enum = Operation[operation.upper()]
        result = calculator.calculate(operation_enum, operand1, operand2)
        return jsonify(result=result)
    except KeyError:
        return jsonify(error="Invalid operation."), 400
    except ValueError as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)