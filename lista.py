"""
Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
cabeceras:
"""
# lista.py

def esta_en_rango(valor, minimo, maximo):
    """
    Devuelve True o False determinando si el valor se encuentra entre el mínimo y el máximo.
    """
    return minimo <= valor <= maximo

def esta_en_lista(valor, lista):
    """
    Devuelve True o False determinando si el valor está en la lista.
    """
    return valor in lista

def main():
    # Lista proporcionada
    numeros_validos = [6, 14, 11, 3, 2, 1, 15, 19]

    try:
        # Solicitar al usuario que ingrese un número del 1 al 20
        numero_usuario = int(input("Ingresa un número del 1 al 20: "))

        # Verificar si el número está en el rango y en la lista
        if esta_en_rango(numero_usuario, 1, 20) and esta_en_lista(numero_usuario, numeros_validos):
            print(f"¡El número {numero_usuario} está en el rango y en la lista!")
        else:
            print(f"El número {numero_usuario} no cumple con los requisitos.")

    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
