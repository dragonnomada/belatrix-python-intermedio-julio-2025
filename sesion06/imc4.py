# Una clase puede definir un modelo:
#  -> Posee un estado estado interno (compuesto de variables de la clase / atributos)
#  -> Posee métodos internos (compuesto de funciones de la clase / métodos)

# Sintaxis: Para definir una clase sería

# class NOMBRE(SUPERIOR / BASE):
#   <atributos>
#   <métodos>

# <atributo>: <variable> = <valor por defecto>
# <método>:   def <función>(self, <parámetros>): [BLOQUE]

class IMC:

    # Atributos (de la clase/objeto -> self)
    estatura = None
    peso = None
    imc = None

    def capturarEstatura(self):
        # Variables locales como `estatura`
        estatura = float(input("Dame la estatura (m): "))
        # Variables de la clase/objeto como `self.estatura`
        self.estatura = estatura

    def capturarPeso(self):
        # Variable local `peso`
        peso = float(input("Dame el peso (kg): "))
        # Variable de la clase/objeto -> estado `self`
        self.peso = peso

    def calcularIMC(self):
        if self.estatura is None:
            print("No se puede calcular el índice de masa corporal")
            print("La estatura no ha sido capturada")
            return
        
        if self.peso is None:
            print("No se puede calcular el índice de masa corporal")
            print("El peso no ha sido capturado")
            return

        # Variable local `imc`
        imc = self.peso / self.estatura ** 2
        # Variable de la clase/objeto -> estado `self`
        self.imc = imc

    def generarReporte(self):
        if self.estatura is None:
            print("No se puede generar el reporte")
            print("La estatura es nula")
            return
        
        if self.peso is None:
            print("No se puede generar el reporte")
            print("El peso es nulo")
            return
        
        if self.imc is None:
            print("No se puede generar el reporte")
            print("El índice de masa corporal no ha sido calculado")
            return

        print(f"""
        Estatura: {self.estatura:>12.2f} m
        Peso:     {self.peso:>12.2f} kg
        ---------------------------------------
        IMC:      {self.imc:>12.2f} kg/m^2
        """)

    def __str__(self):
        estatura = "???"
        peso = "???"
        imc = "???"
        if not self.estatura is None: estatura = f"{self.estatura:.2f}"
        if not self.peso is None: peso = f"{self.peso:.2f}"
        if not self.imc is None: imc = f"{self.imc:.2f}"
        return f"Estatura: {estatura} | Peso: {peso} | IMC: {imc}"