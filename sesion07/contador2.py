class Contador:

    conteo = None # -> 40

    # Método especial: Contructor (__init__)
    def __init__(self, conteo_inicial):
        self.conteo = conteo_inicial

    def incrementar(self):
        self.conteo += 1

    def decrementar(self):
        self.conteo -= 1
