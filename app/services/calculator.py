from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self):
        pass
        
    def calculate(self,first, second):
        calculator = Calculator()               # # '1' = 자연어, 1 = 기계어
        print(f'첫번째수 : {calculator.first}')
        print(f'두번째수 : {calculator.second}')
        print(f'{calculator.first} + {calculator.second} = {calculator.sum()}')     
        print(f'{calculator.first} - {calculator.second} = {calculator.subtract()}')     
        print(f'{calculator.first} * {calculator.second} = {calculator.mult()}')    
        print(f'{calculator.first} / {calculator.second} = {calculator.divide()}')    
            
 