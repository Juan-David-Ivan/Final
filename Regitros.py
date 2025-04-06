import datetime

from flet.core import date_picker

import ddbb
import flet as ft
def main(page : ft.Page):
    page.title = 'REGISTRO'

    def abrir_selector(e):
        date_picker.open = True
        page.update()

    def seleccionar_fecha(e):
        fecha_txt.value = f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}"
        page.update()

    def crear_usuario(e):
        nombre = nombre_tf.value
        passwd = passwd_tf.value
        email = email_tf.value
        fecha = date_picker.value
        ultima_conexion = datetime.date.today()

        ddbb.insertar_usuario(nombre,passwd,email,fecha,ultima_conexion)

    def adelante(e):
        page.go("/formulario")
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nombre_tf = ft.TextField(label='Usuario' , width=300)

    passwd_tf = ft.TextField(label='Contraseña...', width=300)

    date_picker = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())

    email_tf = ft.TextField(label='Email', width=300)

    fecha_txt = ft.Text(f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}")

    adelante_btn = ft.ElevatedButton(text="Adelante", on_click=adelante)


    columna_datos = ft.Column(
        controls=[ ft.Text("Registrate...", size=40),
                   nombre_tf,
                   passwd_tf,
                   email_tf,
                   fecha_txt,
                   ft.FilledButton("Seleccionar fecha", on_click=abrir_selector),
                   ft.FilledButton("Crear usuario", on_click=crear_usuario),
                   adelante_btn,
                ]
    )
    page.overlay.append(date_picker)
    return columna_datos