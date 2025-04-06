import flet as ft

def main(page: ft.Page):
    page.title = "INFORMACION"

    columna = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("BIENVENIDO A MI PÁGINA WEB RAFA", color="white"),

        ]
    )

    fila = ft.Row(controls=[columna],
                    alignment=ft.MainAxisAlignment.CENTER,
                    )

    page.update()

    return columna











