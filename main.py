"""
Primer archivo que se encargará de controlar todo el flujo del juego.
También controlará las dificultades y las estadísticas.
"""

# Importamos las funciones de los distintos módulos del proyecto
from configuracion import seleccionar_modo, seleccionar_dificultad
from motor_juego import jugar_ronda
from estadisticas import inicializar_estadisticas, actualizar_estadisticas, mostrar_resumen
import time

# Definimos los elementos base del juego (el enunciado acepta lista o tupla)
ELEMENTOS_JUEGO = ['A', 'B', 'C', 'D', 'E', 'F']

TIEMPO_MINIMO = 2  # para que en modo velocidad no llegue a tiempos imposibles


def calcular_tiempo_ronda(modo_juego, dificultad, ronda_actual):
    """
    Calcula el tiempo disponible para esta ronda.
    En modo velocidad baja un poco cada ronda.
    """
    tiempo_base = dificultad["tiempo_respuesta"]

    if modo_juego == "velocidad":
        tiempo_ronda = tiempo_base - (ronda_actual - 1) * 0.2

        # Establecemos un tiempo mínimo para evitar valores negativos o imposibles
        if tiempo_ronda < TIEMPO_MINIMO:
            tiempo_ronda = TIEMPO_MINIMO
    else:
        # En el resto de modos el tiempo permanece constante
        tiempo_ronda = tiempo_base

    # Redondeamos para que no salgan decimales raros tipo 2.199999999
    return round(tiempo_ronda, 2)


def main():  # funcion que controla la ejecucion del juego

    print("************************************")
    print("  BIENVENIDO AL JUEGO DE SIMON SAYS  ")
    print("************************************")

    try:
        # variables que seleccionan el modo de juego y dificultad
        modo_juego = seleccionar_modo()
        dificultad = seleccionar_dificultad()

        # Validación básica (robustez): comprobamos que dificultad tenga lo importante
        if not isinstance(dificultad, dict) or "nombre" not in dificultad or "tiempo_respuesta" not in dificultad:
            raise ValueError("La dificultad no tiene el formato esperado (faltan claves).")

        # variables principales inicializadas
        secuencia = []  # Secuencia que el jugador debe memorizar
        vidas = 3  # El jugador empieza con 3 vidas
        ronda_actual = 0  # Contador de rondas
        estadisticas = inicializar_estadisticas()

        # mostramos mensajes a usuario
        print("\nComienza la partida")
        print(f"Modo seleccionado: {modo_juego}")
        print(f"Dificultad seleccionada: {dificultad['nombre']}")

        # Como el juego terminará solo cuando el jugador pierde, codificamos un bucle principal
        while vidas > 0:
            ronda_actual += 1
            print(f"\n*** RONDA {ronda_actual} ***")

            # Calculamos el tiempo disponible para esta ronda
            tiempo_ronda = calcular_tiempo_ronda(modo_juego, dificultad, ronda_actual)

            # Creamos una copia de la dificultad para no modificar la original
            dificultad_ronda = dificultad.copy()
            dificultad_ronda["tiempo_respuesta"] = tiempo_ronda

            # Ejecutamos una ronda completa del juego
            resultado = jugar_ronda(
                secuencia,
                modo_juego,
                dificultad_ronda,
                ELEMENTOS_JUEGO,
                vidas
            )

            # Robustez: comprobamos que jugar_ronda devuelve lo esperado
            if not isinstance(resultado, tuple) or len(resultado) != 4:
                raise TypeError("jugar_ronda debe devolver 4 valores: (acierto, tiempo_respuesta, vidas, longitud).")

            acierto, tiempo_respuesta, vidas, longitud_secuencia = resultado

            # Actualizamos las estadísticas con los datos de la ronda
            actualizar_estadisticas(
                estadisticas,
                acierto,
                tiempo_respuesta,
                longitud_secuencia
            )

            # mostramos mensajes al jugador si acierta o no
            if acierto:
                print("Has superado la ronda.")
            else:
                print("No has superado la ronda.")

            print(f"Vidas restantes: {vidas}")

            # Pausa para que el jugador pueda leer el resultado antes de la siguiente ronda
            time.sleep(2)

        # Si sale del bucle es que ya no quedan vidas
        print("\nHas perdido todas las vidas.")

        # Al finalizar el juego se muestra el resumen de la partida
        mostrar_resumen(
            estadisticas,
            modo_juego,
            dificultad["nombre"]
        )

    except KeyboardInterrupt:
        # Interrupción del sistema (Ctrl+C). Esto encaja con UT05.
        print("\n\nPartida interrumpida por el usuario. Saliendo...")

    except (ValueError, TypeError, KeyError) as e:
        # Errores controlados típicos
        print(f"\nError controlado: {e}")

    except Exception as e:
        # Último recurso
        print(f"\nError inesperado: {e}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
