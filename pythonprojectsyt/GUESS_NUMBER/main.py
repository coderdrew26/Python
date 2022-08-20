import random

def guess(x):
    random_number = random.randint(1, x) #get a random number
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess again, number too low")
        elif guess > random_number:
            print("Guess again, number too high")
        
        
    print(f"Congrats you guess the secret number {random_number}")
            
guess(10)