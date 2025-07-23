# Calculadora simple con operaciones básicas, incluyendo potencias y números negativos

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def potencia(a, b):
    return a ** b

def main():
    print("Bienvenido a la calculadora extendida")
    
    while True:
        # Solicitar los dos números
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Error: Por favor, introduce un número válido (puede ser negativo o decimal).")
            continue

        # Mostrar menú
        print("\nSelecciona la operación:")
        print("1 - Sumar")
        print("2 - Restar")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Potencia (num1 elevado a num2)")
        print("6 - Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcion == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
        elif opcion == '5':
            resultado = potencia(num1, num2)
            print(f"Resultado: {num1} ** {num2} = {resultado}")
        elif opcion == '6':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

        print()  # Línea en blanco para mejorar la lectura

if __name__ == "__main__":
    main()
