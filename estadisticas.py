"""
Este fichero se encarga de la gestión de todas las estadísticas del juego.
Aquí se inicializan, se actualizan durante la partida y se muestran
al finalizar el juego.

Incluye sistema de puntuación, que depende de la longitud
de la secuencia y del tiempo de respuesta del jugador.
"""

def inicializar_estadisticas():
    """
    Inicializa y devuelve un diccionario con todas las estadísticas
    necesarias para una partida nueva.

    Se usa al comienzo del juego para dejar todos los valores a cero.
    """
    return {
        "rondas": 0, #número total de rondas jugadas
        "intentos": 0, #número total de intentos
        "aciertos": 0, #rondas superadas correctamente
        "errores": 0, #rondas fallidas
        "secuencia_maxima": 0, #secuencia más larga alcanzada
        "tiempos_respuesta": [], #lista con los tiempos de respuesta
        "puntuacion_total": 0 #puntuación acumulada del jugador
    }


def sumar_puntos(estadisticas, longitud, tiempo_respuesta, tiempo_limite):
    """
    Suma puntos a la puntuación total del jugador cuando supera una ronda.

    La puntuación se calcula en base a:
    la longitud de la secuencia (puntos base)
    el tiempo de respuesta (bonus por rapidez)

    Solo se llama a esta función cuando el jugador acierta la ronda.
    """

    # Comprobamos que la longitud sea un número entero positivo
    if not isinstance(longitud, int) or longitud <= 0:
        return

    # Comprobamos que el tiempo de respuesta sea un número válido
    if not isinstance(tiempo_respuesta, (int, float)) or tiempo_respuesta < 0:
        return

    # Comprobamos que el tiempo límite sea válido
    if not isinstance(tiempo_limite, (int, float)) or tiempo_limite <= 0:
        return

    # Puntos base: cuantos más elementos tenga la secuencia, más puntos
    puntos_base = longitud * 100

    # Bonus por rapidez: si sobra tiempo se suman puntos extras
    tiempo_sobrante = tiempo_limite - tiempo_respuesta
    bonus = max(0, round(tiempo_sobrante * 10))

    # Sumamos los puntos a la puntuación total
    estadisticas["puntuacion_total"] += puntos_base + bonus


def actualizar_estadisticas(estadisticas, acierto, tiempo_respuesta, longitud_secuencia):
    """
    Actualiza las estadísticas después de cada ronda jugada.
    Se incrementan los contadores y se guardan los datos necesarios
    para calcular el resumen final.
    """
    # Aumentamos el número de rondas e intentos
    estadisticas["rondas"] += 1
    estadisticas["intentos"] += 1

    # Guardamos el tiempo de respuesta solo si es válido
    if isinstance(tiempo_respuesta, (int, float)) and tiempo_respuesta >= 0:
        estadisticas["tiempos_respuesta"].append(tiempo_respuesta)

    if acierto:
        # Si el jugador acierta, aumentamos los aciertos
        estadisticas["aciertos"] += 1

        # Actualizamos la secuencia máxima alcanzada
        estadisticas["secuencia_maxima"] = max(
            estadisticas["secuencia_maxima"],
            longitud_secuencia
        )
    else:
        # Si falla, aumentamos el contador de errores
        estadisticas["errores"] += 1


def calcular_precision(estadisticas):
    """
    Calcula y devuelve la precisión del jugador en porcentaje.
    La precisión se obtiene dividiendo los aciertos entre los intentos.
    """
    if estadisticas["intentos"] == 0:
        return 0

    return (estadisticas["aciertos"] / estadisticas["intentos"]) * 100


def calcular_tiempo_medio(estadisticas):
    """
    Calcula y devuelve el tiempo medio de respuesta del jugador.
    """
    tiempos = estadisticas["tiempos_respuesta"]

    # Si no hay tiempos registrados, devolvemos 0
    if len(tiempos) == 0:
        return 0

    return sum(tiempos) / len(tiempos)


def mostrar_resumen(estadisticas, modo, dificultad):
    """
    Muestra por pantalla un resumen final de la partida,
    incluyendo estadísticas y puntuación total.
    """
    precision = calcular_precision(estadisticas)
    tiempo_medio = calcular_tiempo_medio(estadisticas)

    print("\n--- RESUMEN DE LA PARTIDA ---") #mensajes en pantalla de resumen
    print(f"Modo de juego: {modo}")
    print(f"Dificultad: {dificultad}")
    print(f"Rondas jugadas: {estadisticas['rondas']}")
    print(f"Secuencia más larga: {estadisticas['secuencia_maxima']}")
    print(f"Aciertos: {estadisticas['aciertos']}")
    print(f"Errores: {estadisticas['errores']}")
    print(f"Precisión: {precision:.2f}%")
    print(f"Tiempo medio de respuesta: {tiempo_medio:.2f} segundos")
    print(f"Puntuación total: {estadisticas['puntuacion_total']}")