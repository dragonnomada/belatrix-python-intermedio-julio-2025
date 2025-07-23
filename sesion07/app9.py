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
    signalIncrementar = Signal()
    signalDecrementar = Signal()
    # Output
    signalNotificarConteo = Signal(int)
    
    conteo = 0

    def __init__(self):
        super().__init__()

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
    signalNotificarConteo = Signal(int)
    # Output
    signalIncrementar = Signal()
    signalDecrementar = Signal()

    window = QWidget()
    layout = QVBoxLayout()
    labelConteo = QLabel("Conteo: 0")
    buttonIncrementar = QPushButton("Incrementar")
    buttonDecrementar = QPushButton("Decrementar")

    def __init__(self):
        super().__init__()

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

    modelo = ContadorModelo()
    vista = ContadorVista()

    def __init__(self):
        super().__init__()
        self.modelo.signalIncrementar.connect(self.vista.signalIncrementar)
        self.modelo.signalDecrementar.connect(self.vista.signalDecrementar)
        self.vista.signalNotificarConteo.connect(self.modelo.signalNotificarConteo)

controlador = ContadorControlador()

app.exec()