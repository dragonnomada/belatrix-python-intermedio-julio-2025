from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import Signal, QObject
import sys

class TodoModel(QObject):

    state = {}
    updateSignal = Signal(dict)

    def __init__(self):
        super().__init__()

    def update(self, state):
        self.state = state
        self.updateSignal.emit(self.state)
    
class TodoView(QWidget):
    
    completeSignal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo Todo")
        self.layout = QVBoxLayout()

        self.input_titulo = QLineEdit()
        self.button_completar = QPushButton("Completar")

        self.layout.addWidget(QLabel("Nombre:"))
        self.layout.addWidget(self.input_titulo)
        
        self.layout.addWidget(self.button_completar)

        self.setLayout(self.layout)
        
        self.button_completar.clicked.connect(self.onComplete)

    def onComplete(self):
        state = {
            "titulo": self.input_titulo.text()
        }
        self.completeSignal.emit(state)

class TodoController:

    def __init__(self):
        self.todoModel = TodoModel()

        self.todoView = TodoView()

        self.todoView.completeSignal.connect(self.completar)

        self.todoView.show()

    def completar(self, todo):
        print(todo)

app = QApplication(sys.argv)

todoController = TodoController()

sys.exit(app.exec())