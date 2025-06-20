class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        if not all(isinstance(arg, (int, float)) for arg in (a, b)):
            raise TypeError("add arguments must be numbers")
        return a + b

    @classmethod
    def multiply(cls, a, b):
        if not all(isinstance(arg, (int, float)) for arg in (a, b)):
            raise TypeError("multiply arguments must be numbers")
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
