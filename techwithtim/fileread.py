file = open('file.txt', 'r')
f = file.readlines()

newlist = []
for line in f:
    if line[-1] == '\n':
        newlist.append(line[:-1])
    else:
        newlist.append(line)

print(newlist)