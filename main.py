from flask import Flask , render_template, request       # importamos la clase Flask del paquete flask
                                                # el render_template nos permite renderizar un archivo HTML
"""
    Better Comets
    * No nmms
    ! Urgente
    ? duda
    TODO: asd
"""



app = Flask(__name__)       # creamos una instancia de la clase Flask

@app.route('/')             # decorador que indica la ruta de la URL que se va a manejar, en este caso sera la raiz
def index():                # creamos una función que se ejecuta cuando se accede a la ruta indicada
    titulo="IDGS801"
    lista=["Juan","Pedro","Luis"]
    return render_template ('ejemplo1.html', titulo=titulo, lista=lista)

@app.route('/hola')        # ponemos una decoracion que indica la ruta de la URL que se va a manejar, en este caso sera /hola
def hola():                # creamos una función que se ejecuta cuando se accede a la ruta indicada
    
    return '<h1>Hola, Marco!</h1>'

@app.route('/user/<string:user>')    # creamos un decorador con una ruta en la que se espera un parametro definido por su tipo de dato
def user(user):             # creamos una función que recibe el parametro definido en la ruta para poder usarlo
    return f'<h1>Hola {user}</h1>'

@app.route('/numero/<int:num>')    # creamos un decorador con una ruta en la que se espera un parametro definido por su tipo de dato, en este caso un numero
def numero(num):                   # creamos una función que recibe el parametro definido en la ruta para poder usarlo
    return f'<h1>El numero es {num}</h1>'


@app.route('/usuario/<int:id>/<string:username>')   # creamos un decorador en el que se pueden ingresar diferentes tipos de datos
def usuario(id, username):                          # creamos una función que recibe los parametros definidos en la ruta para poder usarlos
    return f'<h1>Usuario: {username} con id: {id}</h1>'


@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1 + n2}</h1>'


@app.route('/default/<string:param>')
def default(param='Marco'):                         # se puede definir un valor por defecto para el parametro que siempre va a ser el mismo
    return f'<h1>El parametro es: {param}</h1>'


@app.route('/operas')
def operas():                                       # podemos poner un bloque de texto en el que se puede escribir HTML, mas no es lo ideal
    return  '''                                     
                <h1>Operaciones</h1>                
                <form>
                    <input type="text" name="name" id="name" placeholder="Name">
                    <input type="text" name="email" id="email" placeholder="Email">
                    <input type="text" name="phone" id="phone" placeholder="Phone">
                    <input type="text" name="message" id="message" placeholder="Message">
                    <button type="submit">Submit</button>
                </form>
            '''

@app.route('/html')
def html():
    return render_template('index.html')           # podemos renderizar un archivo HTML con el metodo render_template

@app.route("/OperasBas", methods=["GET", "POST"])
def operas1():
    resultado = None
    
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operacion = request.form.get("operacion")
        
        if operacion == "sum":
            resultado = int(n1) + int(n2)
        elif operacion == "res":
            resultado = int(n1) - int(n2)
        elif operacion == "mul":
            resultado = int(n1) * int(n2)
        elif operacion == "div":
            resultado = int(n1) / int(n2)
        else:
            resultado = "Operación no válida"
    
    return render_template("OperasBas.html", resultado=resultado)


@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    txtNom = txtApePa = txtApeMa = txtNomCom = rbSex = None
    txtDia = txtMes = txtAnio = txtEdad = txtZodiaco = txtImg = None
    
    if request.method == "POST":
        txtNom = request.form.get("txtNom")
        txtApePa = request.form.get("txtApePa")
        txtApeMa = request.form.get("txtApeMa")
        txtNomCom = f"{txtNom} {txtApePa} {txtApeMa}"
        
        rbSex = request.form.get("rbSex")
        
        txtDia = int(request.form.get("txtDia"))
        txtMes = int(request.form.get("txtMes"))
        txtAnio = int(request.form.get("txtAnio"))
        txtEdad = 2025 - txtAnio
        
        
        """
        No
        1. Rata
        2. Buey
        3. Tigre
            
        """
        
        
        zodiaco = {
            0: ("Mono", "Mono.png"),
            1: ("Gallo", "Gallo.png"),
            2: ("Perro", "Perro.png"),
            3: ("Cerdo", "Cerdo.png"),
            4: ("Rata", "Rata.png"),
            5: ("Buey", "Buey.png"),
            6: ("Tigre", "Tigre.png"),
            7: ("Liebre", "Liebre.png"),
            8: ("Dragón", "Dragon.png"),
            9: ("Serpiente", "Serpiente.png"),
            10: ("Caballo", "Caballo.png"),
            11: ("Cabra", "Cabra.png")
        }
        
        signo = txtAnio % 12
        txtZodiaco, txtImg = zodiaco[signo]
    
    return render_template("zodiaco.html", txtNomCom=txtNomCom, txtEdad=txtEdad, txtZodiaco=txtZodiaco, txtImg=txtImg)

@app.route("/cine", methods=["GET", "POST"])
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
    app.run(debug=True, port=3000)     # ejecutamos la aplicación en modo debug, ademas de que se indica el puerto


