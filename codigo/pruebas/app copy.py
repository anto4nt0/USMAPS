from funciones import algruta

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')
@app.route('/submit', methods=['POST'])
def submit():
    ubicacion_actual = request.form['ubi']
    ubicacion_destino = request.form['des']
    algruta(ubicacion_actual,ubicacion_destino)
    # Aquí puedes procesar los datos, guardarlos en una base de datos, etc.
    return render_template('edificioC.html')

if __name__ == '__main__':
    app.run(debug=True)
