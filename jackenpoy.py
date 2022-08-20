import random

def play():
    print("Laro tayo ng Bato-Bato-Pik!")
    user = input("I-type ang 'b' para sa bato, 'p' para sa papel at 'g' para sa gunting.\n")
    computer = random.choice(['b', 'p', 'g'])
    
    if user == computer:
        return "Tabla ang laro"
    
    if is_win(user, computer):
        return "Ikaw ay panalo!"
    
    return "Ikaw ay natalo."

def is_win(player, opponent):
    if (player == 'b' and opponent == 'g') or (player == 'g' and opponent == 'p') \
        or (player == 'p' and opponent == 'b'):
            return True
        

print(play())