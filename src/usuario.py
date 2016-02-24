

__author__ = "rjuncverd"
__date__ = "$16-feb-2016 15:27:03$"

from conexion import bd

def grabarUsuario(nombre,password):
    cursor = bd.cursor()
    registro =(nombre,password)
    if nombre!="" and password!="":
        cursor.executemany("""INSERT INTO usuarios(Usuario,Password) VALUES(?,?)""",registro)