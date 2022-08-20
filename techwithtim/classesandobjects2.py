
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi I am", self.name, 'and i am', self.age, 'years old')
        
    def change_age(self, age):
        self.age = age
    

tim = Dog('Tim', 34)
fred = Dog('Fred', 3)
tim.change_age(5)
tim.speak()
fred.speak()


print(type(tim))
print(tim.age)