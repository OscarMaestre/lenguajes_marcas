#!/usr/bin/python3
#encoding=utf-8

import subprocess, time, sys, platform
import bs4

from generador_formularios import *

X_INICIAL=8
Y_INICIAL=130

X_FINAL=480
Y_FINAL=750

ANCHO=X_FINAL - X_INICIAL
ALTO =Y_FINAL - Y_INICIAL

GEOMETRIA="{0}x{1}+{2}+{3}".format(
    ANCHO, ALTO, X_INICIAL, Y_INICIAL, 
)


if platform.system()=="Windows":
    FIN_LINEA="\r\n"
else:
    FIN_LINEA="\n"
    
GENERAR_TABLA="tabla"
GENERAR_FORM ="formulario"
TEXTO="""

Anexo: ejercicios sobre formularios
=====================================
En los ejercicios siguientes se han muestra el diseño básico de algunos formularios junto con el HTML que los resuelve.


{0}

"""

INCLUSION="""
.. literalinclude:: {0}
	:language: html

    
"""

IMAGEN="""
.. image:: {0}
	:align: center
	:scale: 60%

    
"""
def capturar_pantalla(nombre_fichero_imagen):
    subprocess.call(["scrot", nombre_fichero_imagen])


def generar_ejercicio(archivo_html, archivo_png, foto_png):
    #subprocess.call(["./generador_formularios.py", archivo_html])
    subprocess.call(["abrowser", archivo_html])
    time.sleep(2)
    capturar_pantalla(archivo_png)
    recortar_imagen(archivo_png, foto_png)
    
def recortar_imagen(archivo, archivo_cortado):
    subprocess.call(["convert", archivo, "-crop", GEOMETRIA, archivo_cortado])
    
def generar_tablas():
    secciones=""
    g=GeneradorFormularios()
    for i in range(1, 21):
        print("Generando "+str(i))
        
        cad_numero=str(i)
        sufijo=cad_numero.zfill(2)
        archivo_html="formulario_"+sufijo+".html"
        html=g.generar_formulario()
        g.guardar(html, archivo_html)
        archivo_png="formulario_"+sufijo+".png"
        foto_png="foto_formulario_{0}.png".format(sufijo)
        secciones+="Formulario {0}".format(i) + FIN_LINEA
        secciones+="-"*60
        secciones+=FIN_LINEA
        secciones+=FIN_LINEA
        secciones+="Generar el formulario siguiente de acuerdo a los siguientes requisitos"
        secciones+=FIN_LINEA + FIN_LINEA
        secciones+=g.get_descripcion()
        secciones+=IMAGEN.format(foto_png)
        secciones+="Solución:"+FIN_LINEA
        secciones+=INCLUSION.format(archivo_html)
        
        generar_ejercicio(archivo_html, archivo_png, foto_png)
        
        # sopa=bs4.BeautifulSoup(html, "xml")
        # html_indentado=sopa.prettify(formatter=None)
        g.guardar(html, archivo_html, "utf-8")
    return secciones
    

with open("anexo_formularios.rst", "w") as fich:
    secciones=generar_tablas()
    fich.write(TEXTO.format(secciones) )