# Calculadora de promedio de 3 números

# Solicitar los 3 números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Mostrar el resultado
print(f"El promedio de los números es: {promedio:.2f}")