# Definimos la función para sumar dos números
def sumar(a, b):
    return a + b

# Definimos la función para restar dos números
def restar(a, b):
    return a - b

# Definimos la función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Definimos la función para dividir dos números
def dividir(a, b):
    # Comprobamos que el divisor no sea cero para evitar errores
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

# Función principal de la calculadora
def calculadora():
    print("Calculadora simple en Python")
    print("Operaciones disponibles: +, -, *, /")

    # Bucle principal que se repite hasta que el usuario escriba "salir"
    while True:
        op = input("\nIntroduce la operación (+, -, *, /) o 'salir' para terminar: ")

        # Si el usuario escribe "salir", termina el programa
        if op.lower() == "salir":
            print("¡Hasta luego!")
            break  # Salimos del bucle

        # Si la operación no es válida, mostramos un mensaje y volvemos al inicio del bucle
        if op not in ['+', '-', '*', '/']:
            print("Operación no válida. Intenta de nuevo.")
            continue

        try:
            # Pedimos los dos números al usuario y los convertimos a float
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            # Si el usuario introduce texto en lugar de un número, mostramos un error
            print("Error: Debes introducir números válidos.")
            continue

        # Ejecutamos la operación correspondiente según la opción seleccionada
        if op == '+':
            resultado = sumar(num1, num2)
        elif op == '-':
            resultado = restar(num1, num2)
        elif op == '*':
            resultado = multiplicar(num1, num2)
        elif op == '/':
            resultado = dividir(num1, num2)

        # Mostramos el resultado
        print(f"Resultado: {resultado}")

# Llamamos a la función principal para iniciar la calculadora
calculadora()
