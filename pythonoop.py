

#def hello():
#   print("hello")


#x = 1
#y = 2
#print(x + y)

#string = "hello"
#print(string.capitalize())

class Dog:
    
    def __init__(self, name):
        self.name = name
        #print(name)
    
    def get_name(self):
        return self.name
           
    #def add_one(self, x):
        #return x + 1
    
    #def bark(self):
        #print("bark")
        
        
d = Dog("Tim")
print(d.get_name())
d2 = Dog("Bill")

#d.bark()
#print(d.add_one(5))

#print(type(d))