import datetime

from flet.core import date_picker

import ddbb
import flet as ft
def main(page : ft.Page):
    page.title = 'Control Login'

    def abrir_selector(e):
        date_picker.open = True
        page.update()

    def seleccionar_fecha(e):
        fecha_txt.value = f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}"
        page.update()

    def crear_usuario(e):
        nombre = nombre_tf.value
        email = email_tf.value
        passwd = passwd_tf.value
        fecha = date_picker.value
        ultima_conexion = datetime.date.today()

        ddbb.insertar_usuario(nombre,email,passwd,fecha,ultima_conexion)

    def volver(e):
        page.go("/consultas")
        page.update()

    nombre_tf = ft.TextField(label='Usuario o correo electrónico...', width=300)

    email_tf = ft.TextField(label='Email...', width=300)

    passwd_tf = ft.TextField(label='Contraseña...', width=300)

    date_picker = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())

    fecha_txt = ft.Text(f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}")

    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)


    columna_datos = ft.Column(
        controls=[ ft.Text("Login Juan...", size=40),
                   nombre_tf,
                   email_tf,
                   passwd_tf,
                   fecha_txt,
                   ft.FilledButton("Seleccionar fecha", on_click=abrir_selector),
                   ft.FilledButton("Crear usuario", on_click=crear_usuario),
                   volver_btn,
                ]
    )
    page.overlay.append(date_picker)
    return columna_datos