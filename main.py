import flet as ft
import FormulariosPage
import ConsultasPage

def main(page: ft.Page):
    page.title = "Login"

    def route_change(e):
        page.views.clear()

        if(page.route == "/formulario"):
            page.views.append(
                ft.View(
                    route = "/formulario",
                    controls = [FormulariosPage.main(page)]
                )
            )
        elif page.route == "/consultas":
            page.views.append(
                ft.View(
                    route = "/consultas",
                    controls = [ConsultasPage.main(page)]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/formulario")


if __name__ == '__main__':
    ft.app(target=main)
