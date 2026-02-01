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

ELEMENTOS_JUEGO = ['A', 'B', 'C', 'D', 'E', 'F']


def main():

    print("************************************")
    print(" BIENVENIDO AL JUEGO DE SIMON SAYS ")
    print("************************************")

    modo_juego = seleccionar_modo()
    dificultad = seleccionar_dificultad()

    secuencia = []
    vidas = 3
    ronda_actual = 0
    estadisticas = inicializar_estadisticas()

    print("\nComienza la partida")
    print(f"Modo seleccionado: {modo_juego}")
    print(f"Dificultad seleccionada: {dificultad['nombre']}")

    while vidas > 0:
        ronda_actual += 1
        print(f"\n*** RONDA {ronda_actual} ***")

        if modo_juego == "velocidad":
            tiempo_ronda = dificultad["tiempo_respuesta"] - (ronda_actual - 1) * 0.2
            if tiempo_ronda < 2:
                tiempo_ronda = 2
        else:
            tiempo_ronda = dificultad["tiempo_respuesta"]

        dificultad_ronda = dificultad.copy()
        dificultad_ronda["tiempo_respuesta"] = tiempo_ronda

        acierto, tiempo_respuesta, vidas, longitud_secuencia = jugar_ronda(
            secuencia,
            modo_juego,
            dificultad_ronda,
            ELEMENTOS_JUEGO,
            vidas
        )

        actualizar_estadisticas(
            estadisticas,
            acierto,
            tiempo_respuesta,
            longitud_secuencia
        )

        if acierto:
            sumar_puntos(
                estadisticas,
                longitud_secuencia,
                tiempo_respuesta,
                dificultad_ronda["tiempo_respuesta"]
            )
            print("Has superado la ronda.")
        else:
            print("No has superado la ronda.")

        print(f"Vidas restantes: {vidas}")

        time.sleep(2)

        if vidas <= 0:
            print("\nHas perdido todas las vidas.")
            break

    mostrar_resumen(
        estadisticas,
        modo_juego,
        dificultad["nombre"]
    )


if __name__ == "__main__":
    main()
