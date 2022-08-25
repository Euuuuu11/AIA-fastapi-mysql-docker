from tokenize import Number


def calculate():
        pass

class Calculator(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def sum(self):
        result = self.first + self.second
        return result
    def subtract(self):
        result = self.first - self.second
        return result
    def mult(self):
        result = self.first * self.second
        return result
    def divide(self):
        result = self.first / self.second
        return result