class Test:
    @staticmethod
    def main( args):
        k = 0
        while (k < 20):
            if (k % 3 == 1):
                print(str(k) + " ")
                
            k = k + 2
        

if __name__=="__main__":
    Test.main([])
    
   
animals = []
animals.append("dog")
animals.append("cat")
animals.append("snake")
animals.insert(2, "lizard")
animals.insert(1, "fish")
animals.pop(3)
print(animals)