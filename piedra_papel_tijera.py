import random

def play():
    user = input("Empieza el juego selecciona una opcion 'r' para PIEDRA, \
'p' para PAPEL, 't' para TIJERA  -->> ")
    computer = random.choice(['r', 'p', 'o'])
    
    if user == computer:
        return '\nEmpate'
        
    if winner(user, computer):
        return '\nGanaste'
    
    return "\nPerdisteeeee.."
    
  

def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 't' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
            return True 

print(play())
