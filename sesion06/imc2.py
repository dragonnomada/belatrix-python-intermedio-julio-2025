# Responsabilidad: Capturar un valor decimal desde el usuario
# referente a la estatura y devolverlo
def capturarEstatura():
    respuesta = input("Dame la estatura (m): ")
    try:
        estatura = float(respuesta)
        return estatura
    except:
        print("No se pudo capturar la estatura")
    
# Responsabilidad: Capturar un valor decimal desde el usuario
# referente al peso y devolverlo
def capturarPeso():
    respuesta = input("Dame el peso (kg): ")
    try:
        peso = float(respuesta)
        return peso
    except:
        print("No se puedo capturar el peso")

# Responsabilidad: Determinar el IMC a partir de la estatura y el peso
def calcularIMC(estatura, peso):
    if estatura == 0:
        print("División por cero")
        return None
    return peso / estatura ** 2

# Responsabilidad: Generar un reporte a partir de la estatura, el peso y el IMC
def generarReporteIMC(estatura, peso, imc):
    print(f"""
        Estatura: {estatura:>12.2f} m
        Peso:     {peso:>12.2f} kg
        -----------------------------
        IMC:      {imc:>12.2f} kg/m^2
    """)