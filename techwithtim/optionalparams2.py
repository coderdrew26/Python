'''def func(x):
    return x **2

call = func(5)
print(call)

def func(x=1):
    return x **2

call = func()
print(call)

def func(word, freq=1, add=5):
    print(word*(freq+add))
    
call = func("da ", 3)'''


class car(object):
    def __init__(self, make, model, year, condition="New", kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
        
    def display(self, showAll=True):
        if showAll:
            print("This car is a %s %s from %s, It is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s." %(self.make, self.model, self.year))

whip = car("Ford", "Fusion", 2012)
whip.display(False)