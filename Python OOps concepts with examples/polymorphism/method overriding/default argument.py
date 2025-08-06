class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add())        # Output: 0
print(calc.add(10))      # Output: 10
print(calc.add(10, 20))  # Output: 30
print(calc.add(1, 2, 3)) # Output: 6
