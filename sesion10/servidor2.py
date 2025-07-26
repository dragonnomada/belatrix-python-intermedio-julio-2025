from flask import Flask

app = Flask(__name__)

@app.route("/")
def ruta_principal():
    return "Hola mundo 🌎"

app.run(host="0.0.0.0", port=4000)