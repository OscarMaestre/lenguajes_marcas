#!/usr/bin/python3
import os, shutil


RUTA_DIRECTORIO_DESTINO ="docs"
RUTA_APUNTES = "_build" + os.sep + "html"
print ("Borrando " + RUTA_DIRECTORIO_DESTINO)
shutil.rmtree ( RUTA_DIRECTORIO_DESTINO , ignore_errors=True)

shutil.copytree(RUTA_APUNTES, RUTA_DIRECTORIO_DESTINO, ignore=None)
os.mknod(RUTA_DIRECTORIO_DESTINO + os.sep+".nojekyll")