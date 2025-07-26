from flask import Flask

import numpy
import pandas

import matplotlib.pyplot as pyplot
import seaborn

from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

estudiantes = pandas.read_csv("student_habits_performance.csv")

g1 = BytesIO()

pyplot.clf()
estudiantes["gender"].value_counts().plot.pie(autopct="%.2f%%")
pyplot.title("Proporción del género de los estudiantes")
pyplot.savefig(g1)

g2 = BytesIO()

pyplot.clf()
seaborn.jointplot(estudiantes, x="study_hours_per_day", y="netflix_hours", hue=estudiantes["exam_score"] >= 70)
pyplot.title("Contraste de los hábitos de los estudiantes\n entre las horas de estudio y las horas viendo netflix\n por aprobados y reprobados", y=1.2)
pyplot.savefig(g2)

@app.route("/")
def ruta_principal():
    g1.seek(0)
    data1 = b64encode(g1.read()).decode("utf8")
    g2.seek(0)
    data2 = b64encode(g2.read()).decode("utf8")

    return f"""
        <h1>Reporte de los hábitos de los estudiantes</h1>

        <img src="data:image/png;base64,{data1}" >
        {pandas.DataFrame(estudiantes["gender"].value_counts()).to_html()}

        <img src="data:image/png;base64,{data2}" >

        {estudiantes[["age", "gender", "study_hours_per_day", "netflix_hours", "exam_score"]].to_html()}
    """

app.run(host="0.0.0.0", port=4000)