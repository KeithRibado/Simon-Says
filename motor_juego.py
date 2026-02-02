"""

Este fichero contiene toda la lógica principal del juego
"""

import random
import time


def generar_secuencia(secuencia, modo, dificultad, elementos):
    """
    Añade nuevos elementos a la secuencia según el modo de juego
    y la dificultad seleccionada.
    """

    # En los modos clásicos se añade siempre un solo elemento
    if modo in ("clasico", "velocidad", "inverso"):
        secuencia.append(random.choice(elementos))

    # En modo caos se añaden varios elementos aleatorios
    elif modo == "caos":
    # Obtenemos el número máximo de elementos a añadir
        caos_max = dificultad.get("caos_max", 2)

    # Validación simple por si el valor no es correcto
        if not isinstance(caos_max, int) or caos_max < 1:
            caos_max = 2

    # Añadimos entre 1 y caos_max elementos
        cantidad = random.randint(1, caos_max)
        for _ in range(cantidad):
            secuencia.append(random.choice(elementos))

    return secuencia


def mostrar_secuencia(secuencia, velocidad):
    """
    Muestra la secuencia al jugador con una pausa entre elementos,
    para que pueda memorizarla.
    """

# Validamos la velocidad para evitar valores incorrectos
    if not isinstance(velocidad, (int, float)) or velocidad < 0:
        velocidad = 1

    print("\nMemoriza la secuencia:")
    time.sleep(1)

# Mostramos cada elemento con una pequeña pausa
    for elemento in secuencia:
        print(elemento)
        time.sleep(velocidad)

# Saltos de línea para "limpiar" la pantalla
    print("\n" * 10)


def pedir_secuencia_usuario(longitud, tiempo_max):
    """
    Pide al usuario que introduzca la secuencia completa.
    La secuencia debe introducirse sin espacios (ejemplo: ABC).

    Se mide el tiempo total que tarda en responder, aunque no
    se corta la entrada de forma forzada.
    """
    print("Introduce la secuencia SIN espacios (ejemplo: ABC)")

    try:
    # Medimos el tiempo antes y después del input
        inicio = time.time()
        entrada = input("Secuencia: ")
        fin = time.time()

    except KeyboardInterrupt:
    # Permite salir limpiamente si el usuario pulsa Ctrl+C
        print("\nEntrada interrumpida por el usuario.")
        raise

    tiempo_respuesta = fin - inicio

    # Si se ha pasado del tiempo máximo, se considera fallo
    if isinstance(tiempo_max, (int, float)) and tiempo_max > 0:
        if tiempo_respuesta > tiempo_max:
            print("Has tardado demasiado tiempo.")
            return [], tiempo_respuesta

    # Normalizamos la entrada: quitamos espacios y pasamos a mayúsculas
    entrada = entrada.strip().upper()

    # Convertimos la cadena en una lista de caracteres
    secuencia_usuario = list(entrada)

    return secuencia_usuario, tiempo_respuesta


def comprobar_secuencia(secuencia_correcta, secuencia_usuario, modo):
    """
    Comprueba si la secuencia introducida por el usuario es correcta.
    En modo inverso, la comparación se hace al revés.
    """

    # Determinamos cuál es la secuencia correcta según el modo
    if modo == "inverso":
        objetivo = list(reversed(secuencia_correcta))
    else:
        objetivo = secuencia_correcta

    # Si la longitud no coincide, la secuencia es incorrecta
    if len(secuencia_usuario) != len(objetivo):
        return False

    # Comparación directa de las secuencias
    return secuencia_usuario == objetivo


def gestionar_vidas(vidas, acierto):
    """
    Resta una vida al jugador si falla la secuencia
    y muestra el mensaje correspondiente.
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

    Devuelve una tupla con:
    - acierto (True / False)
    - tiempo de respuesta del jugador
    - vidas restantes
    - longitud actual de la secuencia
    """

    # Generamos la nueva secuencia
    generar_secuencia(secuencia, modo, dificultad, elementos)

    # Mostramos la secuencia al jugador
    mostrar_secuencia(secuencia, dificultad["velocidad_mostrar"])

    # Pedimos la secuencia al usuario y medimos el tiempo
    secuencia_usuario, tiempo_respuesta = pedir_secuencia_usuario(
        len(secuencia),
        dificultad["tiempo_respuesta"]
    )

    # Comprobamos si la respuesta es correcta
    acierto = comprobar_secuencia(secuencia, secuencia_usuario, modo)

    # Actualizamos las vidas según el resultado
    vidas = gestionar_vidas(vidas, acierto)

    return acierto, tiempo_respuesta, vidas, len(secuencia)
