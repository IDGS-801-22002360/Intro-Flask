from flask import Flask , render_template       # importamos la clase Flask del paquete flask
                                                # el render_template nos permite renderizar un archivo HTML

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


@app.route('/default/')
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


if __name__ == '__main__':
    app.run(debug=True, port=3000)     # ejecutamos la aplicación en modo debug, ademas de que se indica el puerto




