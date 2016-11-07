#!/usr/bin/python3
#encoding=utf-8

import subprocess, time

X_INICIAL=8
Y_INICIAL=130

X_FINAL=390
Y_FINAL=350

ANCHO=X_FINAL - X_INICIAL
ALTO =Y_FINAL - Y_INICIAL

GEOMETRIA="{0}x{1}+{2}+{3}".format(
    X_INICIAL, Y_INICIAL, ANCHO, ALTO
)
def capturar_pantalla(nombre_fichero_imagen):
    subprocess.call(["scrot", nombre_fichero_imagen])


def generar_ejercicio(numero):
    cad_numero=str(numero)
    sufijo=cad_numero.zfill(2)
    archivo_html="ejercicio_"+sufijo+".html"
    archivo_png="ejercicio_"+sufijo+".png"
    foto_png="foto_{0}.png".format(sufijo)
    subprocess.call(["./generador_html.py", archivo_html])
    subprocess.call(["abrowser", archivo_html])
    time.sleep(3)
    capturar_pantalla(archivo_png)
    recortar_imagen(archivo_png, foto_png)
    
def recortar_imagen(archivo, archivo_cortado):
    subprocess.call(["convert", archivo, "-crop", GEOMETRIA, archivo_cortado])
    
for i in range(0, 10):
    generar_ejercicio(i)