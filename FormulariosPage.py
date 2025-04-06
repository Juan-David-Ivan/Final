
import flet as ft
def main(page : ft.Page):
    page.title = 'Login'

    def bienvenida(e):
        page.go("/Bienvenida")
        page.update()

    def registro(e):
        page.go("/Registros")
        page.update()


    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    nombre_tf = ft.TextField(label='Usuario' , width=300)

    passwd_tf = ft.TextField(label='Contraseña...', width=300)

    inicio_btn = ft.ElevatedButton(text="Acceder", on_click=bienvenida)

    registro_btn = ft.ElevatedButton(text="Registro", on_click=registro)


    columna_datos = ft.Column(
        controls=[ ft.Text("Logeate...", size=40),
                   nombre_tf,
                   passwd_tf,
                   registro_btn,
                   inicio_btn

                ]
    )
    return columna_datos