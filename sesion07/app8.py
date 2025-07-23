# APP -> Contador MVC

from PySide6.QtCore import (
    QObject,
    Signal
)

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

app = QApplication()

# MODELO
class ContadorModelo(QObject):

    # Input
    signalIncrementar = None # Signal()
    signalDecrementar = None # Signal()
    # Output
    signalNotificarConteo = None # Signal(int)
    
    conteo = 0

    def __init__(self, signalIncrementar, signalDecrementar, signalNotificarConteo):
        super().__init__()

        self.signalIncrementar = signalIncrementar
        self.signalDecrementar = signalDecrementar
        self.signalNotificarConteo = signalNotificarConteo

        self.signalIncrementar.connect(self.incrementar)
        self.signalDecrementar.connect(self.decrementar)

    def incrementar(self):
        self.conteo += 1
        self.signalNotificarConteo.emit(self.conteo)
    
    def decrementar(self):
        self.conteo -= 1
        self.signalNotificarConteo.emit(self.conteo)

# VISTA
class ContadorVista(QObject):

    # Input
    signalNotificarConteo = None # Signal(int)
    # Output
    signalIncrementar = None # Signal()
    signalDecrementar = None # Signal()

    window = QWidget()
    layout = QVBoxLayout()
    labelConteo = QLabel("Conteo: 0")
    buttonIncrementar = QPushButton("Incrementar")
    buttonDecrementar = QPushButton("Decrementar")

    def __init__(self, signalIncrementar, signalDecrementar, signalNotificarConteo):
        super().__init__()

        self.signalIncrementar = signalIncrementar
        self.signalDecrementar = signalDecrementar
        self.signalNotificarConteo = signalNotificarConteo

        self.window.setWindowTitle("Contador Vista")

        self.layout.addWidget(self.labelConteo)
        self.layout.addWidget(self.buttonIncrementar)
        self.layout.addWidget(self.buttonDecrementar)

        self.buttonIncrementar.clicked.connect(self.onIncrementar)
        self.buttonDecrementar.clicked.connect(self.onDecrementar)

        self.signalNotificarConteo.connect(self.actualizarConteo)

        self.window.setLayout(self.layout)

        self.window.show()

    def onIncrementar(self):
        print("Vista Incrementar:")
        self.signalIncrementar.emit()
    
    def onDecrementar(self):
        self.signalDecrementar.emit()

    def actualizarConteo(self, conteo):
        self.labelConteo.setText(f"Conteo: {conteo}")
        
# CONTRALOR
class ContadorControlador(QObject):

    signalIncrementar = Signal()
    signalDecrementar = Signal()
    signalNotificarConteo = Signal(int)

    modelo = None
    vista = None

    def __init__(self):
        super().__init__()
        self.modelo = ContadorModelo(self.signalIncrementar, self.signalDecrementar, self.signalNotificarConteo)
        self.vista = ContadorVista(self.signalIncrementar, self.signalDecrementar, self.signalNotificarConteo)

controlador = ContadorControlador()

app.exec()