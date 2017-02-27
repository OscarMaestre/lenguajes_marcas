#!/usr/bin/env python3

from generador_esquemas import *


valores_numericos=["cantidad", "precio", "valor", "ancho", "alto", "profundidad"]
generador=GeneradorTiposSimplesNumericos()
if __name__ == '__main__':
    for i in range(0, 10):
        generador.generar(valores_numericos[i%6])
        descripcion=generador.get_descripcion()
        print (descripcion)
        esquema=generador.get_esquema()
        print (esquema)