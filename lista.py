"""
Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
cabeceras:
"""
def estaEnRango(valor, minimo, maximo):
    """Devuelve True si valor se encuentra entre el mínimo y el máximo, False en caso contrario."""
    return minimo <= valor <= maximo

def estaEnLista(valor, lista):
    """Devuelve True si valor está en la lista, False en caso contrario."""
    return valor in lista

if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    try:
        # Solicitar al usuario un valor, mínimo y máximo
        valor = float(input("Introduce un valor: "))
        minimo = float(input("Introduce el valor mínimo: "))
        maximo = float(input("Introduce el valor máximo: "))

        # Verificar si el valor está en el rango especificado
        if estaEnRango(valor, minimo, maximo):
            print(f"{valor} está en el rango entre {minimo} y {maximo}.")
        else:
            print(f"{valor} no está en el rango entre {minimo} y {maximo}.")

        # Solicitar al usuario una lista y un valor
        lista = input("Introduce una lista de valores separados por espacios: ").split()
        valor_buscar = input("Introduce el valor que deseas buscar: ")

        # Convertir la lista a tipos apropiados
        lista = [float(elemento) for elemento in lista]

        # Verificar si el valor está en la lista
        if estaEnLista(float(valor_buscar), lista):
            print(f"{valor_buscar} está en la lista.")
        else:
            print(f"{valor_buscar} no está en la lista.")
    except ValueError:
        print("Error: Introduce valores numéricos válidos.")
