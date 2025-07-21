from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QLabel, QLineEdit, QPushButton, QCheckBox,
    QMessageBox
)
from PySide6.QtCore import Signal, QObject
import sys

class Todo:

    titulo = "<no definido>"
    verificado = False

    def __str__(self):
        return f"{self.titulo:20} [{['No', 'Si'][self.verificado]}]"

class TodoModel(QObject):

    state = Todo()
    updateSignal = Signal(Todo)

    def __init__(self):
        super().__init__()

    def update(self, state):
        self.state = state
        self.updateSignal.emit(self.state)
    
class TodoView(QWidget):
    
    todoTemporal = Todo()
    completeSignal = Signal(Todo)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuevo Todo")
        self.layout = QVBoxLayout()

        self.input_titulo = QLineEdit()
        self.input_titulo.setPlaceholderText("Escribe algo por hacer...")

        self.input_verificado = QCheckBox("¿Verificado?")

        self.button_completar = QPushButton("Completar")

        self.layout.addWidget(QLabel("Nombre:"))
        self.layout.addWidget(self.input_titulo)
        self.layout.addWidget(self.input_verificado)
        
        self.layout.addWidget(self.button_completar)

        self.setLayout(self.layout)
        
        self.input_titulo.textChanged.connect(self.updateTitulo)
        self.input_verificado.toggled.connect(self.toggleVerificado)
        self.input_titulo.returnPressed.connect(self.onComplete)
        self.button_completar.clicked.connect(self.onComplete)

    def updateTitulo(self, titulo):
        self.todoTemporal.titulo = self.input_titulo.text()

    def toggleVerificado(self, verificado):
        self.todoTemporal.verificado = verificado

    def onComplete(self):
        self.completeSignal.emit(self.todoTemporal)

class TodoController:

    def __init__(self):
        self.todoModel = TodoModel()

        self.todoView = TodoView()

        self.todoView.completeSignal.connect(self.completar)

        self.todoView.show()

    def completar(self, todo):
        QMessageBox.warning(self.todoView, "Se creó un nuevo Todo", str(todo))

app = QApplication(sys.argv)

todoController = TodoController()

sys.exit(app.exec())