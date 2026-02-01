"""
Primer archivo que se encargará de controlar todo el flujo del juego
tambien controlara las dificultades y las estadisticas
"""
#importamos las funciones de los modulos del proyecto
from configuracion import seleccionar_modo, seleccionar_dificultad
from motor_juego import jugar_ronda
import time
from estadisticas import (
    inicializar_estadisticas,
    actualizar_estadisticas,
    mostrar_resumen,
    sumar_puntos
)
#Aqui definimos una tupla con los elementos del juego
ELEMENTOS_JUEGO = ("A", "B", "C", "D", "E", "F")
TIEMPO_MINIMO = 2  # para que en modo velocidad no baje a tiempos imposibles

def calcular_tiempo_ronda(modo_juego, dificultad, ronda_actual):
    """
    Calcula el tiempo disponible para la ronda actual.
    En modo velocidad va bajando un poco cada ronda.
    """
    tiempo_base = dificultad["tiempo_respuesta"]

    if modo_juego == "velocidad":
        tiempo = tiempo_base - (ronda_actual - 1) * 0.2
        if tiempo < TIEMPO_MINIMO:
            tiempo = TIEMPO_MINIMO
    else:
        tiempo = tiempo_base

    return round(tiempo, 2)

def main(): #funcion que controla la ejecucion del juego

    print("************************************")
    print(" BIENVENIDO AL JUEGO DE SIMON SAYS ")
    print("************************************")

    try:
        modo_juego = seleccionar_modo() # variables que seleccionan el modo de juego y dificultad
        dificultad = seleccionar_dificultad()

        # Validación básica (robustez)
        if not isinstance(dificultad, dict):
            raise TypeError("La dificultad debe ser un diccionario.")
        if ("nombre" not in dificultad or
            "tiempo_respuesta" not in dificultad or
            "velocidad_mostrar" not in dificultad):
            raise KeyError("Faltan claves en la dificultad (nombre/tiempo_respuesta/velocidad_mostrar).")
       
        # variables principales inicializadas
        secuencia = []
        vidas = 3
        ronda_actual = 0
        estadisticas = inicializar_estadisticas()
#mostramos mensajes al jugador
        print("\nComienza la partida")
        print(f"Modo seleccionado: {modo_juego}")
        print(f"Dificultad seleccionada: {dificultad['nombre']}")

        while vidas > 0: # Como el juego terminará solo cuando el jugador pierde, codificamos un bucle principal
            ronda_actual += 1
            print(f"\n*** RONDA {ronda_actual} ***")

        # Tiempo de la ronda (en velocidad baja progresivamente)
            tiempo_ronda = calcular_tiempo_ronda(modo_juego, dificultad, ronda_actual)

            # Copia para no modificar la dificultad original
            dificultad_ronda = dificultad.copy()
            dificultad_ronda["tiempo_respuesta"] = tiempo_ronda

            # Ejecutamos una ronda
            resultado = jugar_ronda(
                secuencia,
                modo_juego,
                dificultad_ronda,
                ELEMENTOS_JUEGO,
                vidas
            )

            #comprobamos que devuelve lo esperado
            if not isinstance(resultado, tuple) or len(resultado) != 4:
                raise ValueError("jugar_ronda debe devolver 4 valores: (acierto, tiempo, vidas, longitud).")

            acierto, tiempo_respuesta, vidas, longitud_secuencia = resultado

            # Actualizamos estadísticas
            actualizar_estadisticas(estadisticas, acierto, tiempo_respuesta, longitud_secuencia)

            # Si acierta, sumamos puntos (solo cuando supera una ronda)
            if acierto:
                sumar_puntos(estadisticas, longitud_secuencia, tiempo_respuesta, tiempo_ronda)
                print("Has superado la ronda.")
            else:
                print("No has superado la ronda.")

            print(f"Vidas restantes: {vidas}")

            # Pausa para que se lea el resultado
            time.sleep(2)

        print("\nHas perdido todas las vidas.")

        # Resumen finaldel la partida
        mostrar_resumen(estadisticas, modo_juego, dificultad["nombre"])

    except KeyboardInterrupt:
        # si existiera algun interrupción del sistema inesperada por teclado
        print("\n\nPartida interrumpida por el usuario. Saliendo...")

    except (ValueError, TypeError, KeyError) as e:
        # Errores controlados típicos
        print(f"\nError controlado: {e}")

    except Exception as e:
        # Último recurso
        print(f"\nError inesperado: {e}")


if __name__ == "__main__":
    main()