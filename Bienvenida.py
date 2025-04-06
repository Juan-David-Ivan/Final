import flet as ft

def main(page: ft.Page):
    page.title = "INFORMACION"

    columna = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Aqui estaria el proyecto final"),

        ]
    )

    fila = ft.Row(controls=[columna],
                    alignment=ft.MainAxisAlignment.CENTER,
                    )

    page.update()

    return columna











