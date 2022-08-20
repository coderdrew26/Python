var = 9
loop = True
newVar = 4


def func(x):
    global loop
    loop = 7
    
    if x == 5:
        return newVar
    
    
def otherFunc():
    global newVar
    newVar = 5
    return newVar

func(2)
print(loop)