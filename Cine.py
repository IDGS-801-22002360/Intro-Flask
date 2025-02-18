from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cinepolis():
    error = None
    total = None
    txtNom = txtPer = txtBol = tarjeta = None

    if request.method == "POST":
        txtNom = request.form.get("txtNom")
        txtPer = int(request.form.get("txtPer"))
        txtBol = int(request.form.get("txtBol"))
        tarjeta = request.form.get("tarjeta")

        if txtBol > txtPer * 7:
            error = "No se pueden comprar más de 7 boletos por persona."
        else:
            total = txtBol * 12
            if txtBol > 5:
                total *= 0.85
            if tarjeta == "si":
                total *= 0.90

    return render_template("cinepolis.html", error=error, total=total, txtNom=txtNom, txtPer=txtPer, txtBol=txtBol, tarjeta=tarjeta)
if __name__ == '__main__':
    app.run(debug=True, port=2000)