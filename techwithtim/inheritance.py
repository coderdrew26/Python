class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color
        
    def fullTank(self):
        self.gas = 5
        
    def emptyTank(self):
        self.gas = 0
        
    def gasLeft(self):
        return self.gas
    
    
class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed
        
    def beep(self):
        print('Beep beep')
        

class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
        
    def beep(self):
        print('Honk honk')