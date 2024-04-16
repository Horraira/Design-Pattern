
class User:
    # in python class attributes are public by default and should be declare in the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello, {self.name}!'