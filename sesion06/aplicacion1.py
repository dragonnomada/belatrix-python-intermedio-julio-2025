from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)

class Venta1(QMainWindow):

    def __init__(self):
        super().__init__()

        # TODO: Configurar la venta

        self.setWindowTitle("Hola PySide (Qt)")

app = QApplication()

venta1 = Venta1()
venta1.show()

app.exec()