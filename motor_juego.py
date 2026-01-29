"""
Fichero: motor_juego.py
Este fichero contiene toda la lógica principal del juego Simon Says
"""

import random
import time


def generar_secuencia(secuencia, modo, dificultad, elementos):
    """
    Añade nuevos elementos a la secuencia según el modo de juego
    y la dificultad seleccionada.
    """
    if modo == "clasico" or modo == "velocidad" or modo == "inverso":
        # En estos modos siempre se añade un solo elemento
        secuencia.append(random.choice(elementos))

    elif modo == "caos":
        # En modo caos se añaden varios elementos aleatorios
        cantidad = random.randint(1, dificultad["caos_max"])
        for _ in range(cantidad):
            secuencia.append(random.choice(elementos))

    return secuencia


def mostrar_secuencia(secuencia, velocidad):
    """
    Muestra la secuencia al jugador con una pausa entre elementos.
    """
    print("\nMemoriza la secuencia:")
    time.sleep(1)

    for elemento in secuencia:
        print(elemento)
        time.sleep(velocidad)

    # Separamos con saltos de linea para mayor limpieza
    print("\n" * 100)


def pedir_secuencia_usuario(longitud, tiempo_max):
    """
    Pide al usuario que introduzca la secuencia completa
    La secuencia debe introducirse sin espacios (por ejemplo: ABC)
    """
    print("Introduce la secuencia SIN espacios (ejemplo: ABC)")

    inicio = time.time()
    entrada = input("Secuencia: ")
    fin = time.time()

    tiempo_respuesta = fin - inicio

    # Comprobamos si el jugador se ha pasado del tiempo máximo
    if tiempo_respuesta > tiempo_max:
        print("Has tardado demasiado tiempo.")
        return [], tiempo_respuesta

    # Convertimos la entrada a mayúsculas
    entrada = entrada.upper()

    # Convertimos la cadena en una lista de caracteres
    secuencia_usuario = list(entrada)

    # Si la longitud no coincide, la secuencia es incorrecta
    if len(secuencia_usuario) != longitud:
        return secuencia_usuario, tiempo_respuesta

    return secuencia_usuario, tiempo_respuesta


def comprobar_secuencia(secuencia_correcta, secuencia_usuario, modo):
    """
    Se comprueba si la secuencia introducida por el usuario es correcta.
    """
    if modo == "inverso":
        # En modo inverso se compara al reves
        return secuencia_usuario == list(reversed(secuencia_correcta))

    # La comparacion es normal para el resto 
    return secuencia_usuario == secuencia_correcta


def gestionar_vidas(vidas, acierto):
    """
    Resta una vida si el jugador falla la secuencia.
    """
    if not acierto:
        vidas -= 1
        print(f"Has fallado. Te quedan {vidas} vidas.")
    else:
        print("¡Correcto!")

    return vidas


def jugar_ronda(secuencia, modo, dificultad, elementos, vidas):
    """
    Ejecuta una ronda completa del juego.
    Si el jugador acertó, devuelve el tiempo de respuesta y las vidas restantes.
    """
    secuencia = generar_secuencia(secuencia, modo, dificultad, elementos)
    mostrar_secuencia(secuencia, dificultad["velocidad_mostrar"])

    secuencia_usuario, tiempo_respuesta = pedir_secuencia_usuario(
        len(secuencia),
        dificultad["tiempo_respuesta"]
    )

    acierto = comprobar_secuencia(secuencia, secuencia_usuario, modo)
    vidas = gestionar_vidas(vidas, acierto)

    return acierto, tiempo_respuesta, vidas, len(secuencia)
