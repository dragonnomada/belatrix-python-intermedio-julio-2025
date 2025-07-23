from PySide6.QtWidgets import (
    QApplication,
    QWidget
)

app = QApplication()

win1 = QWidget()

win1.setWindowTitle("App 1 - Hola PySide")

#win1.move(0, 0)
win1.setGeometry(0, 0, 1280, 800)
win1.show()

app.exec()