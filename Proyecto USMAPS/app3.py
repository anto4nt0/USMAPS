from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/home')
def index():
    return render_template(open('index.html'))
# Ruta para servir el formulario
@app.route('/mapa', methods=['POST'])
def mapa():
    ubi = request.form['ubi']  # Obtiene el valor del campo 'name'
    des = request.form['des']  # Obtiene el valor del campo 'email'
    return render_template(open('mapa.html'))
@app.route('/galeria')
def galeria():
    return render_template(open('gallery.html'))
@app.route('/about')
def nosotros():
    return render_template(open('about.html'))
@app.route('/service')
def service():
    return render_template(open('service.html'))
@app.route('/lugares')
def lugares():
    return render_template(open('product.html'))
if __name__ == '__main__':
    app.run(debug=True)

