from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

# conexion
import mysql.connector

midb = mysql.connector.connect(
    host="localhost", user="root", password="", database="data"
)

# vacio para tuplas, dictionary para regresar con indices
cursor = midb.cursor(dictionary=True)


@app.route("/modelo")
def home():
    cursor.execute("SELECT * FROM enfermedades")
    enfermedades = cursor.fetchall()
    cursor.execute("SELECT * FROM sintoma")
    sintomas = cursor.fetchall()
    cursor.execute("SELECT * FROM intensidad")
    intensidad = cursor.fetchall()
    return render_template(
        "index.html",
        enfermedades=enfermedades,
        sintomas=sintomas,
        intensidad=intensidad,
    )
