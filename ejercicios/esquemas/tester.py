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
    print ("--"*30)
    print ("Probando tipos")
    print ("--"*30)
    e1=Elemento("cantidad", "tipoCantidad", maxOccurs=3)
    print (e1)
    e1=Elemento("cantidad", "tipoCantidad")
    print (e1)
    e1=TipoSimpleCadenaConPatron("codigo", "[A-Z]{3,4}-[0-9]{3}")
    print(e1)