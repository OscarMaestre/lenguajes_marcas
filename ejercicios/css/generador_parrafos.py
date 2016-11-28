#!/usr/bin/env python3
from random import randint, shuffle

class PropiedadCSS(object):
    def __init__(self, posibilidades):
        self.posibilidades=posibilidades
    def get_css(self):
        print (self.posibilidades)
        css=""
        cantidad=randint(0, len(self.posibilidades)-1)
        print (cantidad)
        css+="\t{0}\n".format(self.posibilidades[cantidad])
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
        super(PropiedadBorder, self).__init__(POSIBILIDADES)
    
class GeneradorCSS(object):
    CLASES=[PropiedadBorder, PropiedadFuente]
    def get_valor_booleano_aleatorio(self):
        num=randint(0, 1)
        if num==0:
            return True
        else:
            return False
    def generar(self):
        
        
class GeneradorParrafos(object):
    
    def generar_parrafos(self):
        border=PropiedadBorder()
        css=border.get_css()
        print (css)
        
g=GeneradorParrafos()
g.generar_parrafos()