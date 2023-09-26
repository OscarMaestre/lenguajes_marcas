#!/usr/bin/python3
#encoding=utf-8

import subprocess, time, sys, platform

X_INICIAL=8
Y_INICIAL=186

X_FINAL=X_INICIAL + 460
Y_FINAL=Y_INICIAL + 390

ANCHO=X_FINAL - X_INICIAL
ALTO =Y_FINAL - Y_INICIAL

GEOMETRIA="{0}x{1}+{2}+{3}".format(
    ANCHO, ALTO, X_INICIAL, Y_INICIAL, 
)

#Modifica esto para cambiar la cantidad de tablas que se generan
NUM_EJERCICIOS=25

if platform.system()=="Windows":
    FIN_LINEA="\r\n"
else:
    FIN_LINEA="\n"
    
GENERAR_TABLA="tabla"
GENERAR_FORM ="formulario"
TEXTO="""
Anexo: ejercicios sobre tablas
=================================

Las tablas HTML muestran cierta complejidad cuando se anidan. En los ejercicios
siguientes se muestran algunas tablas junto con su resolución en HTML. Los
ejercicios no se muestran con ningún orden de dificultad.

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
    subprocess.call(["./generador_html.py", archivo_html, GENERAR_TABLA])
    subprocess.call(["firefox", archivo_html])
    time.sleep(2)
    capturar_pantalla(archivo_png)
    recortar_imagen(archivo_png, foto_png)
    
def recortar_imagen(archivo, archivo_cortado):
    subprocess.call(["convert", archivo, "-crop", GEOMETRIA, archivo_cortado])
    
def generar_tablas():
    secciones=""
    for i in range(1, NUM_EJERCICIOS):
        
        cad_numero=str(i)
        sufijo=cad_numero.zfill(2)
        archivo_html="ejercicio_"+sufijo+".html"
        archivo_png="ejercicio_"+sufijo+".png"
        foto_png="foto_{0}.png".format(sufijo)
        secciones+="Tabla {0}".format(i) + FIN_LINEA
        secciones+="-"*60
        secciones+=FIN_LINEA
        secciones+=FIN_LINEA
        secciones+="Generar la tabla siguiente" + FIN_LINEA
        secciones+=IMAGEN.format(foto_png)
        secciones+="Solución:"+FIN_LINEA
        secciones+=INCLUSION.format(archivo_html)
        generar_ejercicio(archivo_html, archivo_png, foto_png)
    return secciones
    

with open("anexo_tablas.rst", "w") as fich:
    secciones=generar_tablas()
    fich.write(TEXTO.format(secciones) )