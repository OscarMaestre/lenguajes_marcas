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
    e2=TipoSimpleCadenaConEnumeracion("tipoEnumerado", ["usa", "espania", "alemania", "japon"])
    print(e2)
    at=Atributo("moneda", "xsd:decimal")
    print(at)
    at=Atributo("moneda", "xsd:decimal", requerido=True)
    print(at)
    e1=Elemento("cantidad", "tipoCantidad", maxOccurs=3)
    e2=Elemento("ccc", "tipoCC")
    hh=TipoConHijos("lista", secuencia=True, lista_elementos=[e1,e2], lista_atributos=[at, at])
    print (hh)
    hh=TipoConSoloAtributos("elementoconatributos", "xsd:unsignedInt",
                            lista_atributos=[at, at])
    print (hh)
    tn=TipoNumerico("cantidad", "xsd:decimal", minimo=2, maximo=100,
                    digitos_totales=5, digitos_fraccionarios=2)
    print(tn)