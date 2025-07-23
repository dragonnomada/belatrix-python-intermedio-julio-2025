from PySide6.QtCore import (
    QObject,
    Signal
)

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget
)

import sqlite3

class TodoModel(QObject):

    signalActualizarTodos = Signal(object)

    conn: sqlite3.Connection

    def conectar(self):
        self.conn = sqlite3.connect("todo.db")
        print("Conectado a la base de datos todo.db")

    def desconectar(self):
        self.conn.close()
        print("Desconectado de la base de datos todo.db")

    def crearTablaTodo(self):
        cursor = self.conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS todos (" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "titulo TEXT NOT NULL," \
        "verificado INTEGER DEFAULT 0" \
        ")")

        self.conn.commit()

        cursor.close()

        print("Se creó la tabla <todos>")

    def consultarTodos(self):
        print("Consultado todos...")

        cursor = self.conn.cursor()

        cursor.execute("SELECT id, titulo, verificado FROM todos")

        todos = cursor.fetchall()

        print(todos)

        self.signalActualizarTodos.emit(todos)

        cursor.close()

class TodoView(QObject):

    signalConsultarTodos = Signal()
    
    window: QWidget
    layout: QVBoxLayout
    buttonActualizarTodos: QPushButton

    def iniciar(self):
        self.window = QWidget()
        self.window.setWindowTitle("Todo App")

        self.layout = QVBoxLayout()
        
        self.buttonActualizarTodos = QPushButton("Actualizar Todos")

        self.layout.addWidget(self.buttonActualizarTodos)

        self.buttonActualizarTodos.clicked.connect(self.signalConsultarTodos)

        self.window.setLayout(self.layout)

    def mostrar(self):
        self.window.show()

    def actualizarTodos(self, todos):
        print("Visualizar todos:", todos)


class TodoController(QObject):

    todoModel = TodoModel()
    todoView = TodoView()

    def inicializar(self):
        app = QApplication()

        self.todoView.signalConsultarTodos.connect(self.todoModel.consultarTodos)
        self.todoModel.signalActualizarTodos.connect(self.todoView.actualizarTodos)

        self.todoModel.conectar()
        self.todoModel.crearTablaTodo()

        app.aboutToQuit.connect(self.todoModel.desconectar)

        self.todoView.iniciar()
        self.todoView.mostrar()

        app.exec()

todoController = TodoController()

todoController.inicializar()