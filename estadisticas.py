"""
Fichero: estadisticas.py
Este módulo se encarga de gestionar todas las estadísticas del juego.
Aquí se inicializan, se actualizan durante la partida y se muestran
al finalizar el juego.
"""

def inicializar_estadisticas():
    """
    Inicializa y devuelve un diccionario con todas las estadísticas
    necesarias para una partida.
    """
    return {
        "rondas": 0,
        "intentos": 0,
        "aciertos": 0,
        "errores": 0,
        "secuencia_maxima": 0,
        "tiempos_respuesta": []
    }


def actualizar_estadisticas(estadisticas, acierto, tiempo_respuesta, longitud_secuencia):
    """
    Actualiza las estadísticas después de cada ronda.

    - estadisticas: diccionario con las estadísticas actuales
    - acierto: booleano que indica si el jugador acertó la ronda
    - tiempo_respuesta: tiempo que tardó el jugador en responder
    - longitud_secuencia: longitud actual de la secuencia
    """
    estadisticas["rondas"] += 1
    estadisticas["intentos"] += 1
    estadisticas["tiempos_respuesta"].append(tiempo_respuesta)

    if acierto:
        estadisticas["aciertos"] += 1
        # Guardamos la secuencia más larga alcanzada
        if longitud_secuencia > estadisticas["secuencia_maxima"]:
            estadisticas["secuencia_maxima"] = longitud_secuencia
    else:
        estadisticas["errores"] += 1


def calcular_precision(estadisticas):
    """
    Calcula y devuelve la precisión del jugador en porcentaje.
    """
    if estadisticas["intentos"] == 0:
        return 0

    return (estadisticas["aciertos"] / estadisticas["intentos"]) * 100


def calcular_tiempo_medio(estadisticas):
    """
    Calcula el tiempo medio de respuesta del jugador.
    """
    if len(estadisticas["tiempos_respuesta"]) == 0:
        return 0

    return sum(estadisticas["tiempos_respuesta"]) / len(estadisticas["tiempos_respuesta"])


def mostrar_resumen(estadisticas, modo, dificultad):
    """
    Muestra por pantalla un resumen final de la partida.
    """
    precision = calcular_precision(estadisticas)
    tiempo_medio = calcular_tiempo_medio(estadisticas)

    print("\n--- RESUMEN DE LA PARTIDA ---")
    print(f"Modo de juego: {modo}")
    print(f"Dificultad: {dificultad}")
    print(f"Rondas jugadas: {estadisticas['rondas']}")
    print(f"Secuencia más larga: {estadisticas['secuencia_maxima']}")
    print(f"Aciertos: {estadisticas['aciertos']}")
    print(f"Errores: {estadisticas['errores']}")
    print(f"Precisión: {precision:.2f}%")
    print(f"Tiempo medio de respuesta: {tiempo_medio:.2f} segundos")
