from contador import Contador
import os

c1 = Contador()

while True:
    os.system("clear")

    print(f"""
          Contador: {c1.conteo}

          Selecciona una opción:
          1. Incrementar
          ---------------------------------
          0. Salir
          """)
    
    opcion = input("Opción: ")

    if opcion == "1":
        c1.incrementar()
    elif opcion == "0":
        break
    else:
        print("La opción no es válida")

    input("[Presione ENTER para continuar]")

print("Fin del programa.")