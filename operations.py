from enum import Enum
from config import Config

class Operation(Enum):
    ADD = Config.OPERATIONS['add']
    SUBTRACT = Config.OPERATIONS['subtract']
    MULTIPLY = Config.OPERATIONS['multiply']
    DIVIDE = Config.OPERATIONS['divide']
    MAMAS = Config.OPERATIONS['mamas']

class Calculator:
    def __init__(self):
        self.operations = {
            Operation.ADD: self.add,
            Operation.SUBTRACT: self.subtract,
            Operation.MULTIPLY: self.multiply,
            Operation.DIVIDE: self.divide,
            Operation.MAMAS: self.mamasnik
        }

    def calculate(self, operation: Operation, operand1: float, operand2: float) -> float:
        return self.operations[operation](operand1, operand2)


    @staticmethod
    def mamasnik(x, y):
        return x + y - x - y + 6
    
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y