from flask import Flask

app = Flask(__name__)

@app.route("/")
def ruta_principal():
    return "Visita la ruta /json"

@app.route("/json")
def ruta_json():
    return {
        "nombre": "Coca Cola",
        "precio": 14.56,
        "existencias": 123,
        "dietetico": False,
        "colores": ["rojo", "negro"]
    }

app.run(host="0.0.0.0", port=4000)