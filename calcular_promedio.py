def calcular_promedio():
    try:
        numeros = input("Ingrese una serie de numeros separados por coma: ")
        lista_numeros = [float(num) for num in numeros.split(",")]
        promedio = sum(lista_numeros) / len(lista_numeros)
        print(f"El promedio de los numeros ingresados es: {promedio:.2f}")
    except ValueError:
        print("Error: Ingrese solo numeros separados por coma. ")
    except ZeroDivisionError:
        print("Error: No se ingresaron numeros para calcular el promedio. ")


calcular_promedio()
