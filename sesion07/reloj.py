class Reloj:

    horas = 0
    minutos = 0
    segudos = 0

    def tic(self):
        self.segudos += 1
        if self.segudos == 60:
            self.segudos = 0
            self.tac()

    def tac(self):
        self.minutos += 1
        if self.minutos == 60:
            self.minutos = 0
            self.toc()

    def toc(self):
        self.horas += 1
        if self.horas == 100:
            self.horas = 0

    # Método especial: __str__() -> str
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segudos:02d}"
        # 1:1:1 -> 01:01:01
