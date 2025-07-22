from imc2 import (
    capturarEstatura, 
    capturarPeso, 
    calcularIMC, 
    generarReporteIMC
)

estatura = capturarEstatura()
peso = capturarPeso()

if not estatura is None and not peso is None:
    imc = calcularIMC(estatura, peso)

    if not imc is None:
        generarReporteIMC(estatura, peso, imc)
    else:
        print("No se pudo calcular el índice de masa corporal")
else:
    print("El programa no puede continuar")

print("Fin del programa.")