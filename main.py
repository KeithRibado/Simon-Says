"""
Primer archivo que se encargará de controlar todo el flujo del juego
tambien controlara las dificultades y als estadisticas
"""

# Importamos las funciones de los distintos módulos del proyecto
from configuracion import seleccionar_modo, seleccionar_dificultad
from motor_juego import jugar_ronda
from estadisticas import inicializar_estadisticas, actualizar_estadisticas, mostrar_resumen

# Definimos los elementos base del juego en una tupla para cumplir con los requisitos
ELEMENTOS_JUEGO = ['A', 'B', 'C', 'D', 'E', 'F']


def main(): # funcion que controla la ejecucion del jeugo
   
    print("************************************")
    print(" BIENVENIDO Al JUeGO DE SIMON SAYS  ")
    print("************************************")

    # variables que seleccionan el modo de juego y dificultad
    modo_juego = seleccionar_modo()
    dificultad = seleccionar_dificultad()

    #variables principales inicializadas
    secuencia = []          # Secuencia que el jugador debe memorizar
    vidas = 3               # El jugador empieza con 3 vidas
    ronda_actual = 0        # Contador de rondas
    estadisticas = inicializar_estadisticas()

    print("\nComienza la partida")
    print(f"Modo seleccionado: {modo_juego}")
    print(f"Dificultad seleccionada: {dificultad['nombre']}")

    # Como el juego terminará solo cuando el jugador pierde***********************
    # Bucle principal del juego
    # El juego solo termina cuando el jugador pierde todas las vidas
    while vidas > 0:
        ronda_actual += 1
        print(f"\n--- RONDA {ronda_actual} ---")

        # Calculamos el tiempo disponible para esta ronda
        # En modo velocidad el tiempo se reduce progresivamente
        if modo_juego == "velocidad":
            tiempo_ronda = dificultad["tiempo_respuesta"] - (ronda_actual - 1) * 0.2

            # Establecemos un tiempo mínimo para evitar valores negativos o imposibles
            if tiempo_ronda < 2:
                tiempo_ronda = 2
        else:
            # En el resto de modos el tiempo permanece constante
            tiempo_ronda = dificultad["tiempo_respuesta"]

        # Creamos una copia de la dificultad para no modificar la original
        dificultad_ronda = dificultad.copy()
        dificultad_ronda["tiempo_respuesta"] = tiempo_ronda

        # Ejecutamos una ronda completa del juego
        acierto, tiempo_respuesta, vidas, longitud_secuencia = jugar_ronda(
            secuencia,
            modo_juego,
            dificultad_ronda,
            ELEMENTOS_JUEGO,
            vidas
        )

        # Actualizamos las estadísticas con los datos de la ronda
        actualizar_estadisticas(
            estadisticas,
            acierto,
            tiempo_respuesta,
            longitud_secuencia
        )

        # Mensajes informativos para el jugador
        if acierto:
            print("Has superado la ronda.")
        else:
            print("No has superado la ronda.")

        print(f"Vidas restantes: {vidas}")

        # Pausa para que el jugador pueda leer el resultado antes de la siguiente ronda
        import time
        time.sleep(2)

        # Si no quedan vidas, se termina el juego
        if vidas <= 0:
            print("\nHas perdido todas las vidas.")
            break

    # Al finalizar el juego se muestra el resumen de la partida
    mostrar_resumen(
        estadisticas,
        modo_juego,
        dificultad["nombre"]
    )


# Punto de entrada del programa
if __name__ == "__main__":
    main()
