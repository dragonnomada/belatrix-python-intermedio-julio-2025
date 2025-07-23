from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QMessageBox,
    QPushButton,
)

app = QApplication()

win1 = QWidget()
win1.setWindowTitle("App 5 - Botón con mensaje")

layout1 = QVBoxLayout()

button1 = QPushButton("Pulsame")

def saludar():
    QMessageBox().information(win1, "Hola", "Haz pulsado el botón")

button1.clicked.connect(saludar)

layout1.addWidget(button1)

win1.setLayout(layout1)

win1.show()

app.exec()