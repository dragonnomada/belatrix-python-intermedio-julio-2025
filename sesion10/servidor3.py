from flask import Flask

app = Flask(__name__)

@app.route("/")
def ruta_principal():
    return """
        <DOCTYPE html>
        <html>
            <head>
                <title>Servidor 3</title>
            </head>
            <body>
                <h1>Bienvenido</h1>

                <input placeholder="Escrite tu nombre" >

                <img src="https://placehold.co/400">
            </body>
        </html>
    """

app.run(host="0.0.0.0", port=4000)