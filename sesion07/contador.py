# class <Modelo>:
#    <atributos>
#    <métodos>

# self -> Estado de la clase/objeto (instancia)

class Contador:

    # Estado
    conteo = 0

    # Funcionalidad / Modificar el Estado
    def incrementar(self):
        self.conteo += 1