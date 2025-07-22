estatura = float(input("Dame la estatura (m): "))
peso = float(input("Dame el peso (kg): "))

imc = peso / estatura ** 2

print(f"""

Estatura: {estatura:.2f}m
Peso    : {peso:.2f}kg

IMC     : {imc:.1f} kg/m^2  

""")