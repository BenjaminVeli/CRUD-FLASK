from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM estudiante")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)


@app.route('/user', methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    carrera = request.form['carrera']
    pais = request.form['pais']

    if nombre  and apellido and telefono and carrera and pais:
        cursor = db.database.cursor()
        sql = "INSERT INTO estudiante (nombre, apellido, telefono, carrera, pais) VALUES (%s, %s , %s , %s , %s)"
        data = (nombre, apellido, telefono, carrera, pais)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM estudiante WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    carrera = request.form['carrera']
    pais = request.form['pais']

    if nombre  and apellido and telefono and carrera and pais:
        cursor = db.database.cursor()
        sql = "UPDATE estudiante SET nombre = %s, apellido = %s , telefono = %s, carrera = %s , pais = %s WHERE id = %s"
        data = (nombre, apellido, telefono, carrera, pais, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)