from flask import Flask, request, render_template
from clases.clases import Boligrafo, Lapiz, Rotulador
app = Flask(__name__,template_folder='html')

@app.route("/")
def instrumentos():
    return render_template("start_instrumentos.html")

@app.route("/instrumentos", methods=['POST'])
def mostrar_instrumentos():
    # Insertar el código aquí
    # Obtener el instrumento seleccionado por el usuario
    instrument = request.form["instrumento"]
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    color = request.form["color"]
    if instrument == "boligrafo":
        tinta = request.form["tinta"]
        punta = request.form["punta"]
        instrumento_ingresado = Boligrafo(nombre=instrument, marca=marca, modelo=modelo, color=color, tinta=tinta, punta=punta)
    elif instrument == "lápiz":
        dureza = request.form["dureza"]
        instrumento_ingresado = Lapiz(nombre=instrument,marca=marca, modelo=modelo, color=color, dureza=dureza)
    else:
        punta = request.form["punta"]
        instrumento_ingresado = Rotulador(nombre=instrument, marca=marca, modelo=modelo, color=color, punta=punta)
    
    # Renderizar la página de instrumentos con el instrumento seleccionado
    return render_template("instrumentos.html", instrumento=instrumento_ingresado)


if __name__ == '__main__':
   app.run(debug=True)