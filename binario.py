""" 
Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
introduzca un número binario e imprima por pantalla el número en formato decimal.
Para desarrollar el programa, es necesario que desarrolles una función con la
siguiente cabecera:
"""
def esBinario(strbinario):
    # Verifica si todos los caracteres en strbinario son '0' o '1'
    return all(bit == '0' or bit == '1' for bit in strbinario)

def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)

    # Convierte el número binario a decimal
    for i in range(longitud):
        bit = int(binario[i])
        posicion = longitud - 1 - i
        decimal += bit * (2 ** posicion)

    return decimal

def obtener_numero_binario():
    while True:
        # Solicita al usuario que introduzca un número binario
        numero_binario = input("Introduce un número binario: ").strip()

        # Verifica si el número introducido es binario
        if esBinario(numero_binario):
            return numero_binario
        else:
            print("Error: Introduce un número binario válido.")

def main():
    try:
        # Obtiene un número binario válido del usuario
        numero_binario = obtener_numero_binario()

        # Convierte el número binario a decimal
        decimal = binario_a_decimal(numero_binario)

        # Imprime el resultado
        print(f"El número decimal equivalente es: {decimal}")
    except ValueError:
        print("Error: Introduce un número binario válido.")

if __name__ == "__main__":
    # Punto de entrada del programa
    main()