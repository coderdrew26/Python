# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

a, b = map(int, input().split())
d = {}
for i in range(a):
    w = input()
    d.setdefault(w, [])
    d[w].append(i+1)
for i in range(b):
    w = input()
    print(*d[w]) if w in d else print(-1)