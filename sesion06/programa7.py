from imc4 import IMC
import os

obj = IMC()

while True:

    os.system("clear")

    print(obj)

    print(f"""
          Selecciona una opción:
          1. Capturar la estatura
          2. Capturar el peso
          3. Calcular el índice de masa corporal
          4. Generar el reporte del índice de masa corporal
          ------------------------------------------------------
          5. Salir
          """)
    
    try:
        opcion = int(input("Opción: "))
    except:
        opcion = 0

    if opcion == 1:
        obj.capturarEstatura()
    elif opcion == 2:
        obj.capturarPeso()
    elif opcion == 3:
        obj.calcularIMC()
    elif opcion == 4:
        obj.generarReporte()
    elif opcion == 5:
        break
    else:
        print("La opción no es válida")

    input("[Presiona ENTER para continuar...]")
    
print("Fin del programa.")