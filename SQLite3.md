# 🐍 SQLite con Python

Este tutorial cubre los conceptos esenciales para trabajar con SQLite usando Python: creación de tablas, tipos de datos, consultas CRUD, y ejemplos breves.

## 🔧 1. Conexión y cursor

```python
import sqlite3

conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()
```

## 🏗 2. Crear tablas

```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER DEFAULT 18,
    email TEXT UNIQUE
);
```

> 📌 Tipos de datos en SQLite

* INTEGER
* REAL → número flotante
* TEXT
* BLOB → datos binarios (como imágenes)
* NULL

> ⚙️ Opciones extras

* PRIMARY KEY
* AUTOINCREMENT
* NOT NULL
* DEFAULT `<valor>`
* UNIQUE

## 📝 3. Insertar datos

```python
cursor.execute("INSERT INTO usuarios (nombre, edad, email) VALUES (?, ?, ?)", 
               ("Ana", 25, "ana@example.com"))
conn.commit()
```

## 🔍 4. Consultar datos

```python
cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

for u in usuarios:
    print(u)
```

> Consulta con filtros:

```python
cursor.execute("SELECT nombre FROM usuarios WHERE edad > ?", (20,))
```

## ✏️ 5. Actualizar datos

```python
cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (30, "Ana"))
conn.commit()
```

## ❌ 6. Eliminar datos

```python
cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ("Ana",))
conn.commit()
```


## 🧹 7. Cerrar conexión

```python
conn.close()
```

## ✅ Resumen de operaciones SQL


Acción| Query SQL Ejemplo
---|---
Crear | `CREATE TABLE ...`
Insertar | `INSERT INTO tabla ...`
Consultar | `SELECT * FROM tabla`
Actualizar | `UPDATE tabla SET ...`
Eliminar | `DELETE FROM tabla WHERE ...`

## 🧪 Recomendaciones

* Siempre usar placeholders (?) para evitar inyecciones SQL.
* En producción, maneja errores con try-except y usa with para manejar conexiones.
