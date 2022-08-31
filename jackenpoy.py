import random

def play():
    print("Laro tayo ng Bato-Bato-Pik!")
    user = input("Pumili sa bato, papel o gunting.\n")
    computer = random.choice(['bato', 'papel', 'gunting'])
    
    print(f"Ang napili mo ay {user}, ang napili ng kalaban mo ay {computer}")
    
    if user == computer:
        return "Tabla ang laro"
    
    if is_win(user, computer):
        return "Ikaw ay panalo!"
    
    return "Ikaw ay natalo."

def is_win(player, opponent):
    if (player == 'bato' and opponent == 'gunting') or (player == 'gunting' and opponent == 'papel') \
        or (player == 'papel' and opponent == 'bato'):
            return True
        

print(play())