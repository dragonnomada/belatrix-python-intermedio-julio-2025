# ! pip install flask
from flask import Flask

app = Flask(__name__)

# Acceso local: localhost -> 127.0.0.1
# Acceso a la red: 0.0.0.0

# Puerto:
#   22 -> SSH
#   21 -> FTP
#   80 -> HTTP
#   443 -> HTTPS
#   3306 -> MySQL
#   3000 -> React
#   8080 -> Apache

app.run(host="0.0.0.0", port=4000)