from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel
)

app = QApplication()

win1 = QWidget()

win1.setWindowTitle("App 4 - Botón y Etiqueta (Horizontal)")

layout1 = QHBoxLayout()

button1 = QPushButton("Hola 1")
label1 = QLabel("Pulsa el botón:")

layout1.addWidget(label1)
layout1.addWidget(button1)

win1.setLayout(layout1)

win1.show()

app.exec()