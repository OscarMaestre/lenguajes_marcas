#!/usr/bin/env python3
#encoding=utf-8
from random import randint

FICHERO_OPCIONES = "opciones.txt"

RADIO_SIN_ID        ="<input type='radio' name='{0}'> {1} "
CHECKBOX_SIN_ID     ="<input type='checkbox' name='{0}'> {1} "
RADIO_CON_ID        ="<input type='radio' name='{0}' id='{2}'> {1} "
CHECKBOX_CON_ID     ="<input type='checkbox' name='{0}' id='{2}'> {1} "
OPTION              ="<option value='{0}'>{1}</option>"
class GeneradorFormularios(object):
    def __init__(self):
        pass
    
    def get_lineas_fichero(self, nombre_fichero):
        lineas=[]
        f=open(nombre_fichero, "r", encoding="utf-8")
        lineas=f.readlines()
        lineas_sin_fin_de_linea=[]
        for l in lineas:
            lineas_sin_fin_de_linea.append ( l.strip() )
        return lineas_sin_fin_de_linea
    
    def get_linea_opciones(self):
        lineas=self.get_lineas_fichero(FICHERO_OPCIONES)
        num_azar=randint(0, len(lineas)-1)
        return lineas[num_azar]
    
    def generar_controles(self, cadena_control, con_fin_linea=True):
        html=""
        linea=self.get_linea_opciones()
        opciones=linea.split(":")
        for o in opciones[1:]:
            if con_fin_linea:
                html+=cadena_control.format(opciones[0], o) + "<br/>\n"
            else:
                html+=cadena_control.format(opciones[0], o)
        return html
    
    def generar_radios(self, con_fin_linea=True):
        resultado= self.generar_controles ( RADIO_SIN_ID, con_fin_linea )
        return resultado
    
    def generar_checkboxes(self, con_fin_linea=True):
        resultado= self.generar_controles ( CHECKBOX_SIN_ID, con_fin_linea )
        return resultado
    
    def generar_options(self, con_fin_linea=True):
        html=""
        linea=self.get_linea_opciones()
        opciones=linea.split(":")
        for o in opciones[1:]:
            if con_fin_linea:
                html+=OPTION.format(o.lower().replace(" ","_"), o) + "<br/>\n"
            else:
                html+=OPTION.format(o.lower(), o) 
        return html
            
    
g=GeneradorFormularios()

print (g.generar_radios())
print (g.generar_checkboxes())
print (g.generar_options())