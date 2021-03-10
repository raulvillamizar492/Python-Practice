import random

def adivinar (x):
    random_number = random.randint(1, x)
    adivinar = 0
    
    while adivinar != random_number:
        adivinar= int(input(f'Adivina un numero entre 1 y {x}: '))
        if adivinar < random_number:
            print('Lo siento ese no es el numero demaciado Bajo !!')
        elif adivinar > random_number:
            print('Lo siento ese no es el numero demaciado Alto !!')
            
    print(f"**---- Felicitaciones acertaste..!! El numero correcto es: {random_number} ----**")
    



    