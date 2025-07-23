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

class TodoView(QObject):

    window: QWidget

    def iniciar(self):
        self.window = QWidget()
        self.window.setWindowTitle("Todo App")

    def mostrar(self):
        self.window.show()


class TodoController(QObject):

    todoModel = TodoModel()
    todoView = TodoView()

    def inicializar(self):
        app = QApplication()

        self.todoModel.conectar()
        self.todoModel.crearTablaTodo()

        app.aboutToQuit.connect(self.todoModel.desconectar)

        self.todoView.iniciar()
        self.todoView.mostrar()

        app.exec()

todoController = TodoController()

todoController.inicializar()