try:
    print("Hola, ingrese un número:")
    nombre = input()
    numero1 = 0

    try:
        numero1 = int(nombre)
        print("El número ingresado es: " + str(numero1))
    except ValueError:
        raise Exception("El valor ingresado no es válido")
except Exception as ex:
    print("Ocurrió un error al ejecutar el programa: " + str(ex))
    print("Por favor comuníquese con el área de TI")
finally:
    input("Presione ENTER para salir del programa...")