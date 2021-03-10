#Juego de ahorcado usando la funcion ramdom para escoger diferentes palabras de una lista 
#Developer Raul andres villamizar
# 08 / 03 / 2021 

import random
palabras=['hipopotamo','cabra','chivo','marrano','cacatua','cucaracha','leon','tigre','rinoceronte','jirafa','elefante','oso','gato','ornitorrinco','cocodrilo','perro','loro','camello',]


#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------


palabra= random.choice(palabras)#Escoge palabras al azar
errores = 0


progreso = []
for i in  range(len(palabra)):#Recorre letra por letra de la palabra
    progreso.append(" _ ")# Y agrega _ por cada letra a la lista progreso


palabra_con_espacios = []
for char in palabra:
    palabra_con_espacios.append(char + ' ')

letrasUsada = []
while errores < 7:
    if errores == 0:
        print(' __________ ')
        print(' |        | ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' =======    ')
    elif errores == 1:
        print(' __________ ')
        print(' |        | ')
        print(' |        ° ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' =======    ')
    elif errores == 2:
        print(' __________ ')
        print(' |        | ')
        print(' |        ° ')
        print(' |        | ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' =======    ')
    elif errores == 3:
        print(' __________ ')
        print(' |        | ')
        print(' |        ° ')
        print(' |        |\\')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' =======    ')
    elif errores == 4:
        print(' __________ ')
        print(' |        | ')
        print(' |        ° ')
        print(' |       /|\\')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' =======    ')
    elif errores == 5:
        print(' __________ ')
        print(' |        | ')
        print(' |        ° ')
        print(' |       /|\\')
        print(' |       /  ')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' =======    ')
    elif errores == 4:
        print(' __________ ')
        print(' |        | ')
        print(' |        o ')
        print(' |       /|\\')
        print(' |       / \\')
        print(' |          ')
        print(' |          ')
        print(' |          ')
        print(' =======    ')
        print('***PERDISTE***')
        break


  
    print(' '.join(progreso))#Añadir al string vacio todo los objetos de progreso
    print('Letras usadas: ', letrasUsada)
    print('Elegi una letra: ')
    letra = input()
    if letra in letrasUsada:
        print("Esta letra ya la usaste...")
    else:
        letrasUsada.append(letra)
        
        hay_error = True
        for i in range(len(palabra)):
            if letra == palabra[i]:
                progreso[i] = letra + ' '
                hay_error = False
        
        if hay_error:
            errores += 1
        if palabra_con_espacios == progreso:
                print(''.join(progreso))
                print('Ganaste!')



    