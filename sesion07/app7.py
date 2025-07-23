# pip install PySide6
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QMessageBox,
    QLabel,
    QPushButton,
)

class VentanaSaludar:

    win = None
    layout = None
    labelSaludar = None
    buttonSaludar = None

    def __init__(self):
        self.win = QWidget()
        self.win.setWindowTitle("App 7 - Ventana encapsulada")

        self.layout = QVBoxLayout()

        self.labelSaludar = QLabel("Hola, pulsa el botón:")
        self.buttonSaludar = QPushButton("Pulsame")

        self.buttonSaludar.clicked.connect(self.saludar)

        self.layout.addWidget(self.labelSaludar)
        self.layout.addWidget(self.buttonSaludar)

        self.win.setLayout(self.layout)

        self.win.show()

    def saludar(self):
        print("Se ha pulsado el botón")
        QMessageBox.information(self.win, "Hola", "Has pulsado el botón")

app = QApplication()

ventana1 = VentanaSaludar()
ventana2 = VentanaSaludar()

app.exec()