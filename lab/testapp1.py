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
)

import sqlite3

class TodoModel(QObject):

    conn: sqlite3.Connection

    def conectar(self):
        self.conn = sqlite3.connect("todo.db")
        print("Conectado a la base de datos todo.db")

    def desconectar(self):
        self.conn.close()
        print("Desconectado de la base de datos todo.db")

class TodoController(QObject):

    todoModel = TodoModel()

    def inicializar(self):
        app = QApplication()

        self.todoModel.conectar()

        app.aboutToQuit.connect(self.todoModel.desconectar)

        app.exec()

todoController = TodoController()

todoController.inicializar()