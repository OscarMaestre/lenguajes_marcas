#!/usr/bin/python3
import os, shutil

<<<<<<< HEAD
RUTA_DIRECTORIO_DESTINO ="docs"
RUTA_APUNTES = "_build" + os.sep + "html"
=======
RUTA_DIRECTORIO_DESTINO = "docs"
RUTA_APUNTES = "_build" + os.sep + "singlehtml"
>>>>>>> 30ca8fbb1ef84d894ffc3074d2f111f603f7f8f5
print ("Borrando " + RUTA_DIRECTORIO_DESTINO)
shutil.rmtree ( RUTA_DIRECTORIO_DESTINO , ignore_errors=True)

shutil.copytree(RUTA_APUNTES, RUTA_DIRECTORIO_DESTINO, ignore=None)
