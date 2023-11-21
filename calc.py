class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def test_calculator():
    calculator = Calculator()

    assert calculator.add(1, 2) == 3
    assert calculator.subtract(5, 3) == 2
    assert calculator.multiply(2, 3) == 6
    assert calculator.divide(6, 2) == 3

    try:
        calculator.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
