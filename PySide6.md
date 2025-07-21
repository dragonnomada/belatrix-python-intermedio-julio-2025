
# 📚 Documentación de Widgets de PySide6

---

## 📝 Índice

- [📚 Documentación de Widgets de PySide6](#-documentación-de-widgets-de-pyside6)
  - [📝 Índice](#-índice)
  - [QWidget](#qwidget)
  - [QMainWindow](#qmainwindow)
  - [QPushButton](#qpushbutton)
  - [QLineEdit](#qlineedit)
  - [QLabel](#qlabel)
  - [QTextEdit](#qtextedit)
  - [QComboBox](#qcombobox)
  - [QCheckBox](#qcheckbox)
  - [QRadioButton](#qradiobutton)
  - [QTableWidget](#qtablewidget)
  - [QListWidget](#qlistwidget)
  - [QMessageBox](#qmessagebox)
  - [QVBoxLayout / QHBoxLayout](#qvboxlayout--qhboxlayout)

---

## QWidget

| Método           | Parámetros esperados                      | Descripción                     |
|------------------|-------------------------------------------|---------------------------------|
| show()           | ()                                        | Muestra el widget               |
| hide()           | ()                                        | Oculta el widget                |
| setWindowTitle() | (str)                                     | Establece el título de ventana |
| setGeometry()    | (int x, int y, int w, int h)              | Define posición y tamaño       |
| resize()         | (int w, int h)                            | Cambia el tamaño               |
| move()           | (int x, int y)                            | Mueve el widget                |
| close()          | ()                                        | Cierra el widget               |

---

## QMainWindow

| Método            | Parámetros esperados  | Descripción                        |
|-------------------|-----------------------|------------------------------------|
| setCentralWidget()| (QWidget)             | Establece el widget central        |
| menuBar()         | ()                    | Devuelve barra de menú             |
| statusBar()       | ()                    | Devuelve barra de estado           |
| setStatusBar()    | (QStatusBar)          | Establece barra de estado          |

---

## QPushButton

| Método             | Parámetros esperados | Descripción                      |
|--------------------|----------------------|----------------------------------|
| setText()          | (str)                | Establece el texto del botón     |
| text()             | ()                   | Devuelve el texto del botón      |
| setEnabled()       | (bool)               | Habilita o deshabilita el botón  |
| clicked.connect()  | (func)               | Conecta la señal de clic         |

---

## QLineEdit

| Método                  | Parámetros esperados | Descripción                              |
|-------------------------|----------------------|------------------------------------------|
| setText()               | (str)                | Establece el texto                       |
| text()                  | ()                   | Devuelve el texto                        |
| clear()                 | ()                   | Limpia el contenido                      |
| setPlaceholderText()    | (str)                | Texto guía (placeholder)                 |
| textChanged.connect()   | (func)               | Señal de cambio de texto                 |
| editingFinished.connect()| (func)              | Señal al terminar edición                |

---

## QLabel

| Método           | Parámetros esperados   | Descripción                         |
|------------------|------------------------|-------------------------------------|
| setText()        | (str)                  | Establece el texto                  |
| text()           | ()                     | Obtiene el texto                    |
| setPixmap()      | (QPixmap)              | Establece una imagen                |
| setAlignment()   | (Qt.AlignmentFlag)     | Alineación del texto o imagen       |

---

## QTextEdit

| Método          | Parámetros esperados | Descripción                       |
|-----------------|----------------------|-----------------------------------|
| setPlainText()  | (str)                | Establece texto plano             |
| toPlainText()   | ()                   | Obtiene texto plano               |
| clear()         | ()                   | Limpia el contenido               |
| append()        | (str)                | Añade texto                       |

---

## QComboBox

| Método                    | Parámetros esperados   | Descripción                         |
|---------------------------|------------------------|-------------------------------------|
| addItem()                 | (str)                  | Añade un ítem                       |
| addItems()                | (list[str])            | Añade múltiples ítems               |
| currentText()             | ()                     | Texto del ítem seleccionado         |
| setCurrentIndex()         | (int)                  | Cambia el índice seleccionado       |
| currentIndexChanged.connect() | (func)           | Señal al cambiar el índice          |

---

## QCheckBox

| Método               | Parámetros esperados | Descripción                          |
|----------------------|----------------------|--------------------------------------|
| setChecked()         | (bool)               | Marca o desmarca                     |
| isChecked()          | ()                   | Verifica si está marcado             |
| stateChanged.connect()| (func)              | Señal de cambio de estado            |

---

## QRadioButton

| Método            | Parámetros esperados | Descripción                     |
|-------------------|----------------------|---------------------------------|
| setChecked()      | (bool)               | Activa o desactiva              |
| isChecked()       | ()                   | Devuelve estado                 |
| toggled.connect() | (func)               | Señal de cambio de estado       |

---

## QTableWidget

| Método                    | Parámetros esperados                           | Descripción                       |
|---------------------------|------------------------------------------------|-----------------------------------|
| setRowCount()             | (int)                                          | Establece el número de filas     |
| setColumnCount()          | (int)                                          | Establece el número de columnas  |
| setHorizontalHeaderLabels()| (list[str])                                   | Etiquetas para las columnas      |
| setItem()                 | (int fila, int col, QTableWidgetItem)         | Establece celda específica        |
| item()                    | (int fila, int col)                            | Devuelve el contenido de celda   |
| clearContents()           | ()                                             | Limpia celdas pero mantiene estructura |

---

## QListWidget

| Método         | Parámetros esperados | Descripción                         |
|----------------|----------------------|-------------------------------------|
| addItem()      | (str)                | Añade un ítem                       |
| addItems()     | (list[str])          | Añade múltiples ítems               |
| takeItem()     | (int)                | Elimina ítem                        |
| count()        | ()                   | Número de ítems                     |
| currentItem()  | ()                   | Ítem seleccionado                   |

---

## QMessageBox

| Método         | Parámetros esperados                              | Descripción                       |
|----------------|---------------------------------------------------|-----------------------------------|
| information()  | (QWidget, str title, str text)                    | Muestra mensaje de información    |
| warning()      | (QWidget, str title, str text)                    | Muestra advertencia               |
| critical()     | (QWidget, str title, str text)                    | Muestra error                     |
| question()     | (QWidget, str title, str text, buttons)          | Muestra pregunta con botones      |
| setIcon()      | (QMessageBox.Icon)                                | Cambia el ícono                   |

---

## QVBoxLayout / QHBoxLayout

| Método               | Parámetros esperados     | Descripción                          |
|----------------------|--------------------------|--------------------------------------|
| addWidget()          | (QWidget)                | Añade widget al layout               |
| addLayout()          | (QLayout)                | Añade otro layout                    |
| setSpacing()         | (int)                    | Define espacio entre elementos       |
| setContentsMargins() | (int, int, int, int)     | Márgenes alrededor del layout        |
