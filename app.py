from flask import Flask, jsonify, request
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
@app.route('/api/products/add',methods=["POST"])
def add_product():
   data = request.json
   if 'name' in data and 'price' in data:
      product = Product(name=data["name"],price=data["price"],description = data.get("description"," "))
      db.session.add(product)
      db.session.commit()
      return jsonify({"message":"Product added  successfully"})
   return jsonify({"message":"Invalid Product data"}), 400   
  

#Ruta para borrar un producto
@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
#Buscar el producto de la base de datos
#Verificar si el producto existe
#Si existe borrarlo
#Si no existe mandar codigo de error

def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
       db.session.delete(product)
       db.session.commit()
       return jsonify({"message":"Product deleted successfully"}),200
    return jsonify({"message":"Product not found"}),400


#Ruta para obtener todos los productos
@app.route('/api/products')
def get_products():
    all_products = Product.query.all()
    return  "All products"

#Ruta para obtener un producto por id
@app.route('/api/products/<int:product_id>')
def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
       return jsonify({
          "id": product.id,
          "name":product.name,
          "price":product.price,
          "description":product.description

       })
    return "Product not found" , 404


#Ruta para actualizar un producto utilizando PUT

#Colocar la ruta
@app.route('/api/products/update/<int:product_id>', methods = ['PUT'])

#Crear funcion upgrade_protuct
def upgrade_product(product_id):
   product = Product.query.get(product_id)
   if not product:
      return "product not found" , 404
   else:
      data = request.json
      return  jsonify({
          "id": product.id,
          "name":product.name,
          "price":product.price,
          "description":product.description

       })
   

  # Buscar el producto y verificar si existe por id
  # Si no existe devolver (return) not found producto no encontrado
  # Si existe recuperar la informacion que viene en el body del request
  # Pasar la info a la base de datos
  # Grabar en la base de datos con commit 
# Devolver (return) mensaje producto actualizado con exito y la nueva informacion, codigo 200.


#Ruta raiz (pagina inicial) es la funcion que se ejecutara el hacer request
@app.route('/')
def hello_world():
    return 'Hello world'



if __name__== "__main__":
 app.run(debug=True)

