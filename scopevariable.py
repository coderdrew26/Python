'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = "global x"
 
def test():
    y = "local y"
    # print(y)
    print(x)
     
test()