from itertools import permutations
a, b = input("").split()
c = list(permutations(a, int(b)))
d = []
for i in c:
    d.append("".join(i))
d = sorted(d)
for i in d:
    print(i)