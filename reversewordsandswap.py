swap = sentence.swapcase()
newlist=list(swap.split())
string=''
for i in range(len(newlist)-1, -1, -1):
    string=string+newlist[i]+" "
return string