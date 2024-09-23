#!/usr/bin/python3

import os,sys

txt_ejemplos="""
Ficheros de ejemplo usados en clase
========================================

"""
directorio=sys.argv[1]
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in sorted(os.walk(directorio)):
    path = root.split(os.sep)
    #print((len(path) - 1) * '---', os.path.basename(root))
    txt_ejemplos+=f'\n{root}\n'
    txt_ejemplos+="----------------------------------------------------------------\n"
    for file in sorted(files):
        fichero=file
        ruta_absoluta=os.path.join(root, file)
        
        txt_ejemplos+=f"* :download:`{fichero} <{ruta_absoluta}>`.\n"
        #print(len(path) * '---', os.path.join(root, file))

print (txt_ejemplos)