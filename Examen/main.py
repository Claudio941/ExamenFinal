from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    calcular = False  

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        precio_unitario = 9000
        total_sin_descuento = tarros_pintura * precio_unitario
        total_con_descuento = total_sin_descuento * (1 - descuento)
        total_descuento = total_sin_descuento * descuento

        calcular = True

        return render_template('ejercicio1.html',calcular=calcular, nombre=nombre,total_sin_descuento=total_sin_descuento,total_con_descuento=total_con_descuento, total_descuento=total_descuento)

    return render_template('ejercicio1.html')


usuarios_registrados = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje1 = ""
    mensaje2 = ""
    mensaje3 = ""
    mensaje4 = ""

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena:
            if usuario == 'juan':
                mensaje1 = f"Bienvenido administrador {usuario}"
            elif usuario == 'pepe':
                mensaje2 = f"Bienvenido usuario {usuario}"
            else:
                mensaje3 = "Usuario no reconocido"
        else:
            mensaje4 = "Usuario o Contraseñas incorrectas"

    return render_template('ejercicio2.html', mensaje1=mensaje1, mensaje2=mensaje2, mensaje3=mensaje3, mensaje4=mensaje4)
@app.route('/')
def inicio():
    return render_template('index.html',
                           url_ejercicio1=url_for('ejercicio1'),
                           url_ejercicio2=url_for('ejercicio2'))
if __name__ == '__main__':
    app.run(debug=True)