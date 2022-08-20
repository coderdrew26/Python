class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi I am", self.name, 'and i am', self.age, 'years old', self.color)
        

    def talk(self):
        print('Bark')
    
    
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def talk(self):
        print('meow')
        

tim = Cat('tim', 5, 'brown')
tim.speak()
