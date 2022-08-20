#square star
'''
n = 5
for i in range(n):
    for j in range(n):
        print('*', end=" ")
    print('')'''
    
#inc triangle star
'''n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=" ")
    print("")'''
    
#dec triangle star    
'''n = 5
for i in range(n):
    for j in range(i, n):
        print('*', end=" ")
    print("")'''
    
#right side triangle
'''n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=" ")
    for j in range(i+1):
        print('* ', end="")
    print("")'''
    
#hill pattern    
'''n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=" ")
    for j in range(i):
        print('* ', end="")
    for j in range(i+1):
        print('* ', end="")   
    print("")'''
    
    
#reverse hill   
'''n = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end=" ")
    for j in range(i, n-1):
        print('* ', end="")
    for j in range(i, n):
        print('* ', end="")   
    print("")'''
    

#diamond pattern    
'''n = 5
for i in range(n-1):
    for j in range(i, n):
        print(' ', end=" ")
    for j in range(i):
        print('* ', end="")
    for j in range(i+1):
        print('* ', end="")   
    print("")
for i in range(n):
    for j in range(i+1):
        print(' ', end=" ")
    for j in range(i, n-1):
        print('* ', end="")
    for j in range(i, n):
        print('* ', end="")   
    print("")'''
    
#right triangle
'''n = 5
for i in range(n):
    for j in range(i+1):
        print('* ', end="")
    print('')'''
    
    
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)

