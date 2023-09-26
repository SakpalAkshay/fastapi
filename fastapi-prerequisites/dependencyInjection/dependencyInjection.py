class Logger:
    def log(self, message):
        print(f"Log: {message}")

class Calculator:
    def __init__(self):
        # Create a Logger instance within the Calculator
        self.logger = Logger()

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Adding {x} and {y} = {result}")
        return result

# Using the Calculator without dependency injection
calculator = Calculator()
result = calculator.add(5, 3)

#with dependency injection
class SecondCalculator:
    def __init__(self, logger):
        # Receive a Logger instance from outside
        self.logger = logger

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Adding {x} and {y} = {result}")
        return result

# Create a Logger instance
secondLogger = Logger()

# Using the Calculator with dependency injection
secondCalculator = SecondCalculator(secondLogger)
secondResult = SecondCalculator.add(5, 3)


