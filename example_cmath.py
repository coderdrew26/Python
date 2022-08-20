# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

a = complex(input().strip())
b = cmath.polar(a)
print(b[0])
print(b[1])