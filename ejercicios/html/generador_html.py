#!/usr/bin/python3
#encoding=utf-8
import random, platform, sys
from bs4 import BeautifulSoup
if platform.system()=="Windows":
    FIN_LINEA="\r\n"
else:
    FIN_LINEA="\n"
class GeneradorHTML(object):
    CON_TABLA=1
    CON_FORMULARIO=CON_TABLA + 1
    def __init__(self):
        random.seed()
        
    def get_pagina(self, opcion):
        cadena="""
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Ejercicio</title>
</head>
<body>
{0}</body>
</html>
        """
        if opcion==GeneradorHTML.CON_TABLA:
            html =cadena.format ( self.generar_tabla() )
            return html
        
    def get_items(self):
        resultado=""
        num=random.randint(2,5)
        for i in range(0, num):
            resultado += "<li>Opción " + str(i+1) + "</li>"+FIN_LINEA
        return resultado
        
    def generar_tabla(self, nivel_anidamiento=0):
        tabs=(nivel_anidamiento+1)*"\t"
        resultado=tabs+"<table border='1'>" + FIN_LINEA + tabs+"<tbody>" + FIN_LINEA
        filas=random.randint(2,4)
        columnas=random.randint(2,4)
        for f in range(0, filas):
            tabs_fila=(nivel_anidamiento+2)*"\t"
            resultado+=tabs_fila+"<tr>" + FIN_LINEA
            for c in range(0, columnas):
                tabs_celda=(nivel_anidamiento+3)*"\t"
                resultado+=tabs_celda
                #¿Se genera una subtabla?
                subtabla=random.randint(0, 6)
                if subtabla==0 and nivel_anidamiento==0:
                    resultado+= "<td>"+FIN_LINEA
                    resultado+=self.generar_tabla(nivel_anidamiento+2)
                    resultado+=tabs_celda+"</td>"
                else:
                    resultado+="<td> Celda </td>"
                resultado+=FIN_LINEA
            resultado+=tabs_fila+"</tr>" + FIN_LINEA
        resultado+=tabs+"</tbody>" + FIN_LINEA + tabs+"</table>" + FIN_LINEA
        return resultado
        
g=GeneradorHTML()

with open(sys.argv[1], "w") as fich:
    if sys.argv[2]=="tabla":
        html=g.get_pagina(GeneradorHTML.CON_TABLA)
        fich.write(html)
        fich.close()
