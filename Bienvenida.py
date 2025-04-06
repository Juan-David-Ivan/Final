import flet as ft

def main(page: ft.Page):
    page.title = "INFORMACION"

    def volver(e):
        page.go("/formulario")
        page.update()

    volver_btn = ft.ElevatedButton(text="VOLVER AL LOGIN...", on_click=volver)

    columna = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("BIENVENIDO A MI PÁGINA WEB, RAFA!!🍺🍺🍺🍺", color="white"),
            volver_btn

        ]
    )

    fila = ft.Row(controls=[columna],
                    alignment=ft.MainAxisAlignment.CENTER,
                    )

    page.update()

    return columna











