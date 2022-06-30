# Coding a simple Python BMI calculator

# Receive input from the user
weight=float(input("Enter your weight in kilograms:"))
height=float(input("Enter your height in centimeters:"))

# Calculate the BMI
bmi=weight/((height/100)*(height/100))

# Display the result to the user
print("Your Body Mass Index (BMI) is:",round(bmi,2))