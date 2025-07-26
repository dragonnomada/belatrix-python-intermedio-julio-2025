from flask import Flask
import pandas

app = Flask(__name__)

@app.route("/")
def ruta_principal():
    return """
        <h1>Bienvenido</h1>

        Descargar los datos de las personas:

        <a href="/personas/csv" download="Personas.csv">Personas.csv</a>
    """

@app.route("/personas/csv")
def ruta_personas_csv():
    personas = pandas.read_excel("Personas.xlsx")

    return personas.to_csv()

app.run(host="0.0.0.0", port=4000)