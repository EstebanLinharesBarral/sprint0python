import random

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

victoria = {
    "piedra": ["tijera", "lagarto"],
    "papel": ["piedra", "spock"],
    "tijera": ["papel", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["piedra", "tijera"]
}

def jugadorJ():
    posible = False
    jugada = ""
    while not posible:
        jugada = input("¡Piedra, papel tijera, lagarto, Spock! Elige:").lower()
        
        try:
            opciones.index(jugada)
            posible = True
        except ValueError:
            print("No es un valor válido")
    
    return jugada

def cpuJ():
    rnd = random.randint(0, len(opciones))
    return opciones[rnd]


def jugada(jugador, cpu):
    ganador = ""
    try:
        victoria[jugador].index(cpu)
        ganador = "jugador"
    except ValueError:
        try:
            victoria[cpu].index(jugador)
            ganador = "cpu"
        except ValueError:
            ganador = "empate"

    print(f"CPU: {cpu} - Jugador: {jugador}")
    if ganador == "jugador":
        print("¡El jugador gana!")
    elif ganador == "cpu":
        print("¡La CPU gana esta ronda!")
    else:
        print("¡Es un empate esta ronda!")
    
    return ganador

nuevoJuego = True

while nuevoJuego:
    corr = False
    jugador = 0
    cpu = 0

    while not corr:
        rondas = input("¿Al mejor de cuanto quieres jugar?")
        try:
            rondas = int(rondas)
            corr = True
        except:
            print("EL valor debe ser numérico")
    
    while jugador < rondas/2 and cpu < rondas/2:
        ganador = jugada(jugadorJ(), cpuJ())

        if ganador == "jugador":
            jugador = jugador+1
        elif ganador == "cpu":
            cpu = cpu+1

    if jugador > cpu:
        print("¡El jugador gana la partida!")
    else:
        print("¡La CPU gana la partida!")

    siNo = ""
    while siNo != "s" and siNo != "n":
        siNo = input("¿Quieres jugar de nuevo (s/n)")
        print(siNo)
        if siNo == "s":
            nuevoJuego = True
        elif siNo == "n":
            nuevoJuego = False

print("FIN DEL JUEGO")