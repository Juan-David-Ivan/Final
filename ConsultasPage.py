import flet as ft
from psycopg2._psycopg import cursor

import ddbb
from ddbb import consultar_usuarios_por_nombre


def main(page: ft.Page):
    page.title = "Consultas"

    def cargar_Tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))),
                ft.DataCell(ft.Text(str(fila[1]))),
                ft.DataCell(ft.Text(str(fila[2]))),
                ft.DataCell(ft.Text(str(fila[3]))),
                ft.DataCell(ft.Text(str(fila[4]))),

            ]))
    def consultar_usuarios_por_nombre():
        login = ddbb.consultar_usuarios_por_nombre()
        cargar_Tabla(login)
        page.update()


    def buscar_usuario(e):
        lista_login = ddbb.consultar_usuarios_por_nombre()
        cargar_Tabla(lista_login)
        page.update()


    def volver(e):
        page.go("/formulario")
        page.update()

    # OBJETOS
    nombre_tf = ft.TextField(label="Nombre", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", on_click=buscar_usuario, width=300)
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)
    tabla = ft.DataTable(bgcolor="blue",
                         columns=[
                             ft.DataColumn(ft.Text("ID")),
                             ft.DataColumn(ft.Text("Nombre")),
                             ft.DataColumn(ft.Text("Email")),
                             ft.DataColumn(ft.Text("Contraseña")),
                             ft.DataColumn(ft.Text("Fecha")),
                             ft.DataColumn(ft.Text("Ultimo Login")),
                         ]
                         )
    columna_datos = ft.Column(
        controls=[
            ft.Text("Consultas", size=40),
            nombre_tf,
            buscar_btn,
            volver_btn
        ]
    )
    consultar_usuarios_por_nombre()
    return  columna_datos