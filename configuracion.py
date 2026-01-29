"""
archivo que se encarga de las funciones que controlan la selecion de modo de juego y la dificultad

"""
#Funcion que mostrara el menu con los modos de juego
def seleccionar_modo():
    
    while True: #imprimimos los modos de juego que manejaremos
        print("\nSelecciona el modo de juego:")
        print("1. Clásico")
        print("2. Velocidad")
        print("3. Inverso")
        print("4. Caos")
#controlamos con una excepcion lo que el jugador pueda introducir y que no haya fallos en nuestro bucle
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

#
def seleccionar_dificultad():

    #Con el bucle mostramos el menu de de opciones
    while True:
        print("\nSelecciona la dificultad:")
        print("1. Fácil")
        print("2. Media")
        print("3. Difícil")
#Para el bloque try usamos un diccionario que tome la clave y valor seleccionado
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
#controlamos errores con una excepcion para que solo se pueda introducir los numero entre 1 y 3
        except ValueError:
            print("Error: debes introducir un número.")
