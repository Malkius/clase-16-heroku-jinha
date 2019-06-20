from flask import Flask, render_template
import datetime
import locale

app = Flask(__name__)


@app.route("/")
def index():
    texto_hora = "La fecha y hora actual es:"
    # Idioma "es-ES" (código para el español de España)
    locale.setlocale(locale.LC_ALL, 'es-ES')
    fecha = datetime.datetime.now()
    # Formato 24 hr
    fecha.strftime("%A %d de %B del %Y - %H:%M")

    return render_template("index.html", texto_hora=texto_hora, fecha=str(fecha.strftime("%A %d de %B del %Y - %H:%M")))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")


@app.route("/portfolio/bugle")
def bugle():
    return render_template("bugle.html")


@app.route("/portfolio/login")
def bugle_login():
    return render_template("login.html")


@app.route("/portfolio/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")


if __name__ == '__main__':
    app.run()
