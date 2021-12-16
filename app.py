from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "2"


@app.route("/")
def index():
    return render_template("base.html.j2", a=12, b=3.14)


@app.route("/abc/", methods=["GET"])
def abc():
    try:
        x = request.args.get("x") 
        y = request.args.get("y")
        soucet = int(x) + int(y)
    except TypeError:
        soucet = None
    except ValueError:
        soucet = "Nedělej si srandu!!!"

    return render_template("abc.html.j2", soucet=soucet)


@app.route("/abc/", methods=["POST"])
def abc_post():

    jmeno = request.form.get("jmeno")
    heslo = request.form.get("heslo")
    print("POST:", jmeno, heslo)

    return redirect(url_for("abc"))


@app.route("/banany/")
def banany():
    return render_template("banany.html.j2")


@app.route("/kvetak/")
def kvetak():
    return render_template("kvetak.html.j2")

@app.route("/count/")
def count():
    session["user"] = "Karel"
    try:
        x = request.args.get("x") 
        y = request.args.get("y")
        podil = int(x) / int(y)
    except TypeError:
        podil = None
    except ValueError:
        podil = "Nedělej si srandu!!!"
    except ZeroDivisionError:
        podil = None


    slovo = request.args.get("slovo")
    if slovo:
        session["slovo"] = slovo

    return render_template("count.html.j2", podil=podil)