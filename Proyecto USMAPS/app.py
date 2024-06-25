from flask import Flask, request, render_template
from ruta.funciones import algruta

app = Flask(__name__)
@app.route('/home')
def index():
    return render_template('index.html')
@app.route('/mapa')
def mapa():
    return render_template('mapa.html')
@app.route('/home')
def about():
    return render_template('abour.html')
@app.route('/mapa')
def gallery():
    return render_template('mapa.html')
@app.route('/home')
def product():
    return render_template('product.html')
@app.route('/mapa')
def service():
    return render_template('service.html')
if __name__ == '__main__':
    app.run(debug=True)