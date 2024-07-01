from flask import Flask, request, render_template
from funciones import algruta

app = Flask(__name__)
@app.route('/home')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/lugares')
def lugares():
    return render_template('product.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/mapa')
def mapa():
    return render_template('mapa.html')
@app.route('/submit', methods=['POST'])
def submit():
    ubicacion_actual = request.form['ubi']
    ubicacion_destino = request.form['des']
    algruta(ubicacion_actual,ubicacion_destino)
    # Aquí puedes procesar los datos, guardarlos en una base de datos, etc.
    return render_template('edificioC.html')
@app.route('/muestramapa')
def muestramapa():
    return render_template('muestramapa.html')

if __name__ == '__main__':
    app.run(debug=True)