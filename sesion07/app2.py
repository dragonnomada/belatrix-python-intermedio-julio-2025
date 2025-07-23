from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)

app = QApplication()

win1 = QWidget()

win1.setWindowTitle("App 2 - Botón")

layout1 = QVBoxLayout()

button1 = QPushButton("Hola 1")

layout1.addWidget(button1)

win1.setLayout(layout1)

win1.show()

app.exec()