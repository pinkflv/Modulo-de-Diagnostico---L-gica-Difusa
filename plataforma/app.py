from flask import Flask, request, url_for, redirect, abort, render_template
import numpy as np

app = Flask(__name__)

# Conexion
import mysql.connector

midb = mysql.connector.connect(
    host="localhost", user="root", password="", database="data"
)

# vacio para tuplas, dictionary para regresar con indices
cursor = midb.cursor(dictionary=True)


@app.route("/")
def index():
    return render_template("saludo.html")


@app.route("/eleccion")
def eleccion():
    return render_template("eleccion.html")


@app.route("/eleccionSintomas", methods=["GET", "POST"])
def eleccionSintomas():
    cursor.execute("SELECT * FROM enfermedades")
    enf = cursor.fetchall()
    if request.method == "POST":
        sql = "UPDATE enfermedades SET indicadas='no';"
        cursor.execute(sql)
        selected = request.form.getlist("enfermedad1")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=1;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad2")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=2;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad3")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=3;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad4")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=4;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad5")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=5;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad6")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=6;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad7")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=7;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad8")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=8;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad9")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=9;"
            cursor.execute(sql)
        selected = request.form.getlist("enfermedad10")
        any_selected = bool(selected)
        if any_selected:
            sql = "UPDATE enfermedades SET indicadas='entro' WHERE idEnfermedades=10;"
            cursor.execute(sql)

        midb.commit()

        return redirect(url_for("llenadoEspecifico"))
    else:
        return render_template("eleccionSintomas.html", enf=enf)
    return render_template("eleccionSintomas.html", enf=enf)


@app.route("/llenado", methods=["GET", "POST"])
def llenado():
    cursor.execute("SELECT * FROM cuadro")
    cuadro = cursor.fetchall()
    cursor.execute("SELECT * FROM intensidad")
    intensidad = cursor.fetchall()
    if request.method == "POST":
        # o1
        o1 = request.form["o1"]
        sql = "UPDATE cuadro SET registro=" + o1 + " WHERE idCuadro=1;"
        cursor.execute(sql)
        # o2
        o2 = request.form["o2"]
        sql = "UPDATE cuadro SET registro=" + o2 + " WHERE idCuadro=2;"
        cursor.execute(sql)
        # o3
        o3 = request.form["o3"]
        sql = "UPDATE cuadro SET registro=" + o3 + " WHERE idCuadro=3;"
        cursor.execute(sql)
        # o4
        o4 = request.form["o4"]
        sql = "UPDATE cuadro SET registro=" + o4 + " WHERE idCuadro=4;"
        cursor.execute(sql)
        # o5
        o5 = request.form["o5"]
        sql = "UPDATE cuadro SET registro=" + o5 + " WHERE idCuadro=5;"
        cursor.execute(sql)
        # o6
        o6 = request.form["o6"]
        sql = "UPDATE cuadro SET registro=" + o6 + " WHERE idCuadro=6;"
        cursor.execute(sql)
        # o7
        o7 = request.form["o7"]
        sql = "UPDATE cuadro SET registro=" + o7 + " WHERE idCuadro=7;"
        cursor.execute(sql)
        # o8
        o8 = request.form["o8"]
        sql = "UPDATE cuadro SET registro=" + o8 + " WHERE idCuadro=8;"
        cursor.execute(sql)
        # o9
        o9 = request.form["o9"]
        sql = "UPDATE cuadro SET registro=" + o9 + " WHERE idCuadro=9;"
        cursor.execute(sql)
        # o10
        o10 = request.form["o10"]
        sql = "UPDATE cuadro SET registro=" + o10 + " WHERE idCuadro=10;"
        cursor.execute(sql)
        # o11
        o11 = request.form["o11"]
        sql = "UPDATE cuadro SET registro=" + o11 + " WHERE idCuadro=11;"
        cursor.execute(sql)
        # o12
        o12 = request.form["o12"]
        sql = "UPDATE cuadro SET registro=" + o12 + " WHERE idCuadro=12;"
        cursor.execute(sql)
        # o13
        o13 = request.form["o13"]
        sql = "UPDATE cuadro SET registro=" + o13 + " WHERE idCuadro=13;"
        cursor.execute(sql)
        # o14
        o14 = request.form["o14"]
        sql = "UPDATE cuadro SET registro=" + o14 + " WHERE idCuadro=14;"
        cursor.execute(sql)
        # o15
        o15 = request.form["o15"]
        sql = "UPDATE cuadro SET registro=" + o15 + " WHERE idCuadro=15;"
        cursor.execute(sql)
        # o16
        o16 = request.form["o16"]
        sql = "UPDATE cuadro SET registro=" + o16 + " WHERE idCuadro=16;"
        cursor.execute(sql)
        # o17
        o17 = request.form["o17"]
        sql = "UPDATE cuadro SET registro=" + o17 + " WHERE idCuadro=17;"
        cursor.execute(sql)
        # o18
        o18 = request.form["o18"]
        sql = "UPDATE cuadro SET registro=" + o18 + " WHERE idCuadro=18;"
        cursor.execute(sql)
        # Guardamos cambios
        midb.commit()
        return redirect(url_for("muestraGeneral"))
    return render_template("llenado.html", cuadro=cuadro)


@app.route("/llenadoEspecifico", methods=["GET", "POST"])
def llenadoEspecifico():
    cursor.execute("SELECT * FROM cuadro")
    cuadro = cursor.fetchall()
    cursor.execute("SELECT * FROM intensidad")
    intensidad = cursor.fetchall()
    if request.method == "POST":
        # o1
        o1 = request.form["o1"]
        sql = "UPDATE cuadro SET registro=" + o1 + " WHERE idCuadro=1;"
        cursor.execute(sql)
        # o2
        o2 = request.form["o2"]
        sql = "UPDATE cuadro SET registro=" + o2 + " WHERE idCuadro=2;"
        cursor.execute(sql)
        # o3
        o3 = request.form["o3"]
        sql = "UPDATE cuadro SET registro=" + o3 + " WHERE idCuadro=3;"
        cursor.execute(sql)
        # o4
        o4 = request.form["o4"]
        sql = "UPDATE cuadro SET registro=" + o4 + " WHERE idCuadro=4;"
        cursor.execute(sql)
        # o5
        o5 = request.form["o5"]
        sql = "UPDATE cuadro SET registro=" + o5 + " WHERE idCuadro=5;"
        cursor.execute(sql)
        # o6
        o6 = request.form["o6"]
        sql = "UPDATE cuadro SET registro=" + o6 + " WHERE idCuadro=6;"
        cursor.execute(sql)
        # o7
        o7 = request.form["o7"]
        sql = "UPDATE cuadro SET registro=" + o7 + " WHERE idCuadro=7;"
        cursor.execute(sql)
        # o8
        o8 = request.form["o8"]
        sql = "UPDATE cuadro SET registro=" + o8 + " WHERE idCuadro=8;"
        cursor.execute(sql)
        # o9
        o9 = request.form["o9"]
        sql = "UPDATE cuadro SET registro=" + o9 + " WHERE idCuadro=9;"
        cursor.execute(sql)
        # o10
        o10 = request.form["o10"]
        sql = "UPDATE cuadro SET registro=" + o10 + " WHERE idCuadro=10;"
        cursor.execute(sql)
        # o11
        o11 = request.form["o11"]
        sql = "UPDATE cuadro SET registro=" + o11 + " WHERE idCuadro=11;"
        cursor.execute(sql)
        # o12
        o12 = request.form["o12"]
        sql = "UPDATE cuadro SET registro=" + o12 + " WHERE idCuadro=12;"
        cursor.execute(sql)
        # o13
        o13 = request.form["o13"]
        sql = "UPDATE cuadro SET registro=" + o13 + " WHERE idCuadro=13;"
        cursor.execute(sql)
        # o14
        o14 = request.form["o14"]
        sql = "UPDATE cuadro SET registro=" + o14 + " WHERE idCuadro=14;"
        cursor.execute(sql)
        # o15
        o15 = request.form["o15"]
        sql = "UPDATE cuadro SET registro=" + o15 + " WHERE idCuadro=15;"
        cursor.execute(sql)
        # o16
        o16 = request.form["o16"]
        sql = "UPDATE cuadro SET registro=" + o16 + " WHERE idCuadro=16;"
        cursor.execute(sql)
        # o17
        o17 = request.form["o17"]
        sql = "UPDATE cuadro SET registro=" + o17 + " WHERE idCuadro=17;"
        cursor.execute(sql)
        # o18
        o18 = request.form["o18"]
        sql = "UPDATE cuadro SET registro=" + o18 + " WHERE idCuadro=18;"
        cursor.execute(sql)
        # Guardamos cambios
        midb.commit()
        return redirect(url_for("muestraEspecifica"))
    return render_template("llenadoEspecifico.html", cuadro=cuadro)


@app.route("/muestraGeneral")
def muestraGeneral():
    cursor.execute(
        "SELECT I.enfermedadId, I.intensidad, C.registro FROM intensidad I JOIN cuadro C ON C.idCuadro = I.sintomaId"
    )
    E1 = cursor.fetchall()
    cursor.execute("SELECT * FROM enfermedades")
    enfermedades = cursor.fetchall()
    cursor.execute("SELECT * FROM cuadro")
    cuadro = cursor.fetchall()

    # Datos = []
    comparado = np.zeros((10, 18))
    s = np.zeros(10)

    # Enfermedad 1
    c = 0
    l1 = []
    l2 = []
    for x in range(10):
        l1 = []
        l2 = []
        for n in E1:
            if n["enfermedadId"] == x + 1:
                l1.append(float(n["registro"]))
        for n in E1:
            if n["enfermedadId"] == x + 1:
                l2.append(float(n["intensidad"]))

        for i in range(18):
            var = min(l1[i], l2[i])
            comparado[x][i] = float(var)
            s[x] += np.around(float(comparado[x][i]), 2)

    print(s)
    print(max(s))

    for x in range(10):
        diagnostico = max(s)
        if diagnostico == s[x]:
            vef = enfermedades[x]["idEnfermedades"]
            ef = enfermedades[x]["nombre"]

    contador = 0
    for val in cuadro:
        if val["registro"] == 0:
            contador += 1

    return render_template(
        "muestraGeneral.html",
        cuadro=cuadro,
        s=s,
        ef=ef,
        vef=vef,
        comparado=comparado,
        contador=contador,
    )


@app.route("/muestraEspecifica")
def muestraEspecifica():
    cursor.execute(
        "SELECT I.enfermedadId, I.intensidad, C.registro FROM intensidad I JOIN cuadro C ON C.idCuadro = I.sintomaId"
    )
    E1 = cursor.fetchall()
    cursor.execute("SELECT * FROM enfermedades WHERE indicadas LIKE 'entro';")
    enfermedades = cursor.fetchall()
    cursor.execute("SELECT * FROM cuadro")
    cuadro = cursor.fetchall()

    # Datos = []
    comparado = np.zeros((10, 18))
    s = np.zeros(10)

    # Enfermedad 1
    c = 0
    l1 = []
    l2 = []
    for x in range(len(enfermedades)):
        l1 = []
        l2 = []
        for n in E1:
            if n["enfermedadId"] == x + 1:
                l1.append(float(n["registro"]))
        for n in E1:
            if n["enfermedadId"] == x + 1:
                l2.append(float(n["intensidad"]))

        for i in range(18):
            var = min(l1[i], l2[i])
            comparado[x][i] = float(var)
            s[x] += np.around(float(comparado[x][i]), 2)

    mostrables = []
    for x in range(len(enfermedades)):
        diagnostico = max(s)
        if diagnostico == s[x]:
            vef = enfermedades[x]["idEnfermedades"]
            mostrables.append(vef)
            ef = enfermedades[x]["nombre"]

    contador = 0
    for val in cuadro:
        if val["registro"] == 0:
            contador += 1

    return render_template(
        "muestraEspecifica.html",
        cuadro=cuadro,
        s=s,
        ef=ef,
        vef=vef,
        comparado=comparado,
        contador=contador,
        mostrables=mostrables,
    )


@app.route("/modelo")
def modelo():
    cursor.execute("SELECT * FROM enfermedades")
    enfermedades = cursor.fetchall()
    cursor.execute("SELECT * FROM sintoma")
    sintomas = cursor.fetchall()
    cursor.execute("SELECT * FROM intensidad")
    intensidad = cursor.fetchall()
    return render_template(
        "modelo.html",
        enfermedades=enfermedades,
        sintomas=sintomas,
        intensidad=intensidad,
    )


if __name__ == "__main__":
    app.run(debug=True)