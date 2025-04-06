import flet as ft

import Bienvenida
import FormulariosPage
import Regitros


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
        elif page.route == "/Registros":
            page.views.append(
                ft.View(
                    route = "/Registros",
                    controls = [Regitros.main(page)]
                )
            )
        elif page.route == "/Bienvenida":
            page.views.append(
                ft.View(
                    route = "/Bienvenida",
                    controls = [Bienvenida.main(page)]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/formulario")


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=30021)
