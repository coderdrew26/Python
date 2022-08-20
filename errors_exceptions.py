# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
for _ in range(a):
    b, c = input().split()
    try:
        print(int(b)//int(c))
    except ZeroDivisionError as zde:
        print("Error Code:",zde)
    except ValueError as ve:
        print("Error Code:",ve)