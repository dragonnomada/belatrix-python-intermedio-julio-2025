from flask import Flask
import pandas

app = Flask(__name__)

@app.route("/")
def ruta_principal():
    return """
        <h1>Bienvenido</h1>

        <p>
            Descargar los datos de las personas:
            <a href="/personas/csv" download="Personas.csv">Personas.csv</a>
        </p>
        
        <p>
            Consultar la tabla de personas:
            <a href="/personas/html">Ver tabla</a>
        </p>
    """

@app.route("/personas/csv")
def ruta_personas_csv():
    personas = pandas.read_excel("Personas.xlsx")

    return personas.to_csv()

@app.route("/personas/html")
def ruta_personas_html():
    personas = pandas.read_excel("Personas.xlsx")

    return personas.to_html()

app.run(host="0.0.0.0", port=4000)