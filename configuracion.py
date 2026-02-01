"""
Archivo que se encarga de las funciones que controlan la selección
del modo de juego y la dificultad, con validaciones de entrada del jugador.
"""

def seleccionar_modo():
    """
    Función que muestra el menú de modos de juego y devuelve
    el modo seleccionado por el jugador.
    """

    # Bucle para insistir hasta que el usuario introduzca una opción válida
    while True:
        print("\nSelecciona el modo de juego:")
        print("1. Clásico")
        print("2. Velocidad")
        print("3. Inverso")
        print("4. Caos")

        try:
            # Convertimos la entrada a entero
            opcion = int(input("Introduce una opción (1-4): "))

            if opcion == 1:
                return "clasico"
            elif opcion == 2:
                return "velocidad"
            elif opcion == 3:
                return "inverso"
            elif opcion == 4:
                return "caos"
            else:
                print("Opción no válida. Debe ser un número del 1 al 4.")

        except ValueError:
            # Controlamos que el usuario introduzca un número
            print("Error: debes introducir un número.")
        except KeyboardInterrupt:
            # Permite salir limpiamente si el usuario pulsa Ctrl+C
            print("\nSelección interrumpida por el jugador.")
            raise


def seleccionar_dificultad():
    """
    Muestra el menú de dificultad y devuelve
    un diccionario con la configuración seleccionada.
    """

    # Bucle para insistir hasta que el jugador introduzca una opción válida
    while True:
        print("\nSelecciona la dificultad:")
        print("1. Fácil")
        print("2. Media")
        print("3. Difícil")

        try:
            # Convertimos la entrada a entero
            opcion = int(input("Introduce una opción (1-3): "))

            if opcion == 1:
                return {
                    "nombre": "facil",
                    "tiempo_respuesta": 10,
                    "velocidad_mostrar": 1.5,
                    "caos_max": 2
                }
            elif opcion == 2:
                return {
                    "nombre": "media",
                    "tiempo_respuesta": 7,
                    "velocidad_mostrar": 1.0,
                    "caos_max": 3
                }
            elif opcion == 3:
                return {
                    "nombre": "dificil",
                    "tiempo_respuesta": 5,
                    "velocidad_mostrar": 0.6,
                    "caos_max": 4
                }
            else:
                print("Opción no válida. Debe ser un número del 1 al 3.")

        except ValueError:
            # Controlamos que el jugador introduzca un número
            print("Error: debes introducir un número.")
        except KeyboardInterrupt:
            # Permite salir limpiamente si el jugador pulsa Ctrl+C
            print("\nSelección interrumpida por el jugador.")
            raise
