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
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)

import sqlite3

import random

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
        print("Consultado Todos...")

        cursor = self.conn.cursor()

        cursor.execute("SELECT id, titulo, verificado FROM todos")

        todos = cursor.fetchall()

        print(todos)

        self.signalActualizarTodos.emit(todos)

        cursor.close()

    def insertarTodoPrueba(self):
        print("Insertando Todo de prueba...")

        cursor = self.conn.cursor()

        i = random.randint(0, 10_000)
        verificado = random.choice([0, 1])

        cursor.execute("INSERT INTO todos (titulo, verificado) VALUES (?, ?)", (f"Prueba {i}", verificado))

        self.conn.commit()

        cursor.close()

        self.consultarTodos()

class TodoView(QObject):

    signalConsultarTodos = Signal()
    signalInsertarTodoPrueba = Signal()
    
    window: QWidget
    layout: QVBoxLayout
    buttonActualizarTodos: QPushButton
    buttonInsertarTodoPrueba: QPushButton
    table: QTableWidget

    celdaActiva = None
    celdaValor = None

    def iniciar(self):
        self.window = QWidget()
        self.window.setWindowTitle("Todo App")

        self.window.resize(800, 600)

        self.layout = QVBoxLayout()
        
        self.buttonActualizarTodos = QPushButton("Actualizar Todos")
        self.buttonInsertarTodoPrueba = QPushButton("Insertar Todo de Prueba")

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Título", "Verificado"])

        self.layout.addWidget(self.buttonActualizarTodos)
        self.layout.addWidget(self.buttonInsertarTodoPrueba)
        self.layout.addWidget(self.table)

        self.buttonActualizarTodos.clicked.connect(self.signalConsultarTodos)
        self.buttonInsertarTodoPrueba.clicked.connect(self.signalInsertarTodoPrueba)

        self.table.cellClicked.connect(self.activarCelda)
        self.table.itemChanged.connect(self.actualizarTodoItem)

        self.window.setLayout(self.layout)

    def mostrar(self):
        self.window.show()

    def actualizarTodos(self, todos):
        print("Visualizar todos:", todos)

        self.table.clearContents()               # Limpia los datos pero no los headers
        self.table.setRowCount(len(todos))

        for index, (id, titulo, verificado) in enumerate(todos):
            self.table.setItem(index, 0, QTableWidgetItem(f"{id:04d}"))
            self.table.setItem(index, 1, QTableWidgetItem(titulo))
            self.table.setItem(index, 2, QTableWidgetItem("✅" if verificado != 0 else "❌"))

    def activarCelda(self, row, column):
        print("Celda activa", row, column)
        self.celdaActiva = (row, column)
        self.celdaValor = self.table.item(row, column).text()

    def actualizarTodoItem(self, todoItem):

        if self.celdaActiva is None:
            return

        indexRow = todoItem.row()
        indexColumn = todoItem.column()
        value = todoItem.text()

        print(f"Se intenta actualizar la fila {indexRow} en la columna {indexColumn}: {value}")

        if indexColumn != 1:
            print("Cambio no permitido. Restaurando valor original...")

            # Desconectamos la señal para evitar bucle
            self.table.blockSignals(True)

            todoItem.setText(self.celdaValor)

            self.table.blockSignals(False)

            QMessageBox.critical(self.window, "Error", "No se puede actualizar esta columna")

            return
        
        todoId = self.table.item(indexRow, 0).text()
        todoTitulo = self.table.item(indexRow, 1).text()
        todoVerificado = self.table.item(indexRow, 2).text()

        print(f"Los valores son: {todoId}, {todoTitulo}, {todoVerificado}")
        
        print("Celda modificada")


class TodoController(QObject):

    todoModel = TodoModel()
    todoView = TodoView()

    def inicializar(self):
        app = QApplication()

        self.todoView.signalConsultarTodos.connect(self.todoModel.consultarTodos)
        self.todoView.signalInsertarTodoPrueba.connect(self.todoModel.insertarTodoPrueba)

        self.todoModel.signalActualizarTodos.connect(self.todoView.actualizarTodos)

        self.todoModel.conectar()
        self.todoModel.crearTablaTodo()

        app.aboutToQuit.connect(self.todoModel.desconectar)

        self.todoView.iniciar()

        self.todoModel.consultarTodos()

        self.todoView.mostrar()

        app.exec()

todoController = TodoController()

todoController.inicializar()