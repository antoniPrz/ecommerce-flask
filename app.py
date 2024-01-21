from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instancia de flask en una variable que por convancion se llama app
app = Flask(__name__)

#Definir la ruta y el nombre de archivo para la accesar a la base de datos sqlite
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ecommerce.db'


#Se inicia la coneccion de la base de datos creando una variable db usando SQLAlchemy usando como parametro la aplicacion flask
db = SQLAlchemy(app)

#Modelado de tabla de producto con las columnas id, name, price, description
class Product(db.Model):
   id = db.Column(db.Integer,primary_key= True)
   name = db.Column(db.String(120), nullable = False)
   price = db.Column(db.Float, nullable = False)
   description = db.Column(db.Text, nullable = True)


#Ruta para agregar un producto
@app.route('/api/products/add')





#Ruta raiz (pagina inicial) es la funcion que se ejecutara el hacer request
@app.route('/')
def hello_world():
    return 'Hello world'



if __name__== "__main__":
 app.run(debug=True)

