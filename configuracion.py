"""
Fichero: configuracion.py
Este fichero contiene las funciones relacionadas con la configuración
inicial del juego: selección del modo de juego y nivel de dificultad.
"""

def seleccionar_modo():
    """
    Muestra un menú con los distintos modos de juego y devuelve
    el modo seleccionado por el usuario.
    """
    while True:
        print("\nSelecciona el modo de juego:")
        print("1. Clásico")
        print("2. Velocidad")
        print("3. Inverso")
        print("4. Caos")

        try:
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
            print("Error: debes introducir un número.")


def seleccionar_dificultad():
    """
    Permite seleccionar el nivel de dificultad del juego y devuelve
    un diccionario con los parámetros asociados a dicha dificultad.
    """
    while True:
        print("\nSelecciona la dificultad:")
        print("1. Fácil")
        print("2. Media")
        print("3. Difícil")

        try:
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
            print("Error: debes introducir un número.")
