class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

# Object creation
p = Person("Alice")
p.greet()  # Output: Hello, my name is Alice
