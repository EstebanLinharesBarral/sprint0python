import random

#Ejercicio 1
print("El programa pensará un número entre 1 y un máximo que tú elijas. Intenta adivinarlo con la menor cantidad de intentos posible.")
bool = False

#Selector de dificultad
while not bool:
    dificultad = input("Elige un nivel de dificultad: 1. Fácil / 2. Media / 3. Difícil (Escoja entre 1, 2 y 3)")
    if dificultad == "1" or dificultad == "2" or dificultad == "3":
        bool = True
    else:
        print("Debe elegir una de las opciones")

#Crear numero random y prueba de función
def crearRandom(num):
    if num == "1":
        rm = random.randint(1, 50)
    elif num == "2":
        rm = random.randit(1, 100)
    elif num == "3":
        rm = random.randint(1, 500)
    return rm

#Bucle de juego
random = crearRandom(dificultad)
acierto = False
intentos = 0

while not acierto:
    try:
        intentos = intentos+1
        userNum = input("Intente adivinar el número, introduzca uno:")
        userNum = int(userNum)
        if userNum > random:
            print("Demasiado alto")
        elif userNum < random:
            print("Demasiado bajo")
        else:
            acierto = True
    except:
        print("Debe introducir un número")
        
print(f"¡Acertaste! Nº de intentos: {intentos}")