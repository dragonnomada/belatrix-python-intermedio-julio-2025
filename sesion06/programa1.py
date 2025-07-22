from imc2 import capturarEstatura, capturarPeso, calcularIMC

estatura = capturarEstatura()
peso = capturarPeso()

if not estatura is None and not peso is None:
    print(estatura)
    print(peso)

    imc = calcularIMC(estatura, peso)

    if not imc is None:
        print(imc)
    else:
        print("No se pudo calcular el índice de masa corporal")
else:
    print("El programa no puede continuar")

print("Fin del programa.")