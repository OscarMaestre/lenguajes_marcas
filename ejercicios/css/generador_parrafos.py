#!/usr/bin/env python3
from random import randint, shuffle

class PropiedadCSS(object):
    def __init__(self, posibilidades):
        self.posibilidades=posibilidades
    def get_css(self):
        #print (self.posibilidades)
        css=""
        cantidad=randint(0, len(self.posibilidades)-1)
        #print (cantidad)
        css+="\t{0};\n".format(self.posibilidades[cantidad])
        return css

class PropiedadBorder(PropiedadCSS):
    def __init__(self):
        POSIBILIDADES=[
            "border: solid black 1px",
            "border: double black 1px",
            "border: dashed black 1px",
            "border: dotted black 1px",
            ]
        super(PropiedadBorder, self).__init__(POSIBILIDADES)
        
class PropiedadFuente(PropiedadCSS):
    def __init__(self):
        POSIBILIDADES=[
            "font-family: Arial Black",
            "font-family: courier",
            "font-family: script",
            ]
        super(PropiedadFuente, self).__init__(POSIBILIDADES)
        
class PropiedadAlineacion(PropiedadCSS):
    def __init__(self):
        POSIBILIDADES=[
            "text-align:right",
            "text-align: justify",
            ]
        super(PropiedadAlineacion, self).__init__(POSIBILIDADES)
    
class GeneradorCSS(object):
    CLASES=[PropiedadBorder, PropiedadFuente, PropiedadAlineacion]
    def get_valor_booleano_aleatorio(self):
        MAX=7
        num=randint(0, MAX)
        if num<MAX:
            return True
        else:
            return False
    def generar(self):
        css=""
        for CLASE in self.CLASES:
            c=CLASE()
            if self.get_valor_booleano_aleatorio():
                css+=c.get_css()
        return css
        
class GeneradorParrafos(object):
    
    def generar_parrafos(self):
        g=GeneradorCSS()
        css=g.generar()
        print (css)
        
g=GeneradorParrafos()
g.generar_parrafos()