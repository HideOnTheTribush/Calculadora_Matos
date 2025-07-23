# calculadora.py

# Función que suma dos números
def sumar(a: float, b: float):
    return a + b

# Función que resta el segundo número al primero
def restar(a: float, b: float):
    return a - b

# Función que multiplica dos números
def multiplicar(a: float, b: float):
    return a * b

# Función que divide el primer número entre el segundo
# Si el divisor es cero, devuelve un mensaje de error
def dividir(a: float, b: float):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

# Diccionario que asocia opciones con sus nombres y funciones
# Clave = número del menú 
# Valor = tupla con el nombre de la operación y la función correspondiente
# Ejemplo: '1' -> ("Sumar", sumar)// Donde '1' es la opción del menú, es decir, la clave y ("Sumar", sumar) es el valor
operaciones = {
    '1': ("Sumar", sumar),
    '2': ("Restar", restar),
    '3': ("Multiplicar", multiplicar),
    '4': ("Dividir", dividir)
}

# Función para mostrar el menú de operaciones disponibles
def mostrar_menu():
    print("\nSelecciona la operación:")
    for clave, (nombre, _) in operaciones.items():
        print(f"{clave} - {nombre}")
    print("5 - Salir")  # Opción para salir del programa

# Función reutilizable para pedir un número al usuario
# Si el usuario escribe algo inválido, se repite hasta que introduzca un número correcto
def pedir_numero(texto: str) -> float:
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("⚠️  Valor no válido. Introduce un número.")

# Función principal del programa
def main():
    print("📟 Calculadora simple en Python")

    while True:
        # Mostrar menú en cada vuelta del bucle
        mostrar_menu()

        # Pedir opción al usuario
        opcion = input("Opción: ")

        # Salir del programa si elige 5
        if opcion == '5':
            print("👋 Gracias por usar la calculadora.")
            break  # Rompe el bucle y termina el programa

        # Si la opción no está en el diccionario de operaciones, mostrar mensaje de error
        if opcion not in operaciones:
            print("❌ Opción no válida.")
            continue  # Vuelve al principio del bucle

        # Pedir los dos números para operar
        num1 = pedir_numero("Introduce el primer número: ")
        num2 = pedir_numero("Introduce el segundo número: ")

        # Buscar en el diccionario el nombre y la función de la operación elegida
        nombre, funcion = operaciones[opcion]

        # Ejecutar la función con los números proporcionados
        resultado = funcion(num1, num2)

        # Mostrar el resultado
        print(f"✅ Resultado de {nombre.lower()}: {resultado}")

# Esta línea se asegura de que main() solo se ejecute si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
