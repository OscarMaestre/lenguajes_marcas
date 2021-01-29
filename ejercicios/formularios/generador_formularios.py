#!/usr/bin/python3
#encoding=utf-8
from random import randint, shuffle
import sys
import codecs

FICHERO_OPCIONES    = "opciones.txt"
FICHERO_LEYENDAS    = "legends.txt"
FICHERO_TEXTAREAS   = "textareas.txt"
FICHERO_INPUTS      = "input_texts.txt"

RADIO_SIN_ID        ="  <input type='radio' name='{0}' value='{2}'> {1} "
CHECKBOX_SIN_ID     ="  <input type='checkbox' name='{0}' value='{2}'> {1} "
RADIO_CON_ID        ="  <input type='radio' name='{0}' id='{2}' value='{3}'> {1} "
CHECKBOX_CON_ID     ="  <input type='checkbox' name='{0}' id='{2} value='{2}''> {1} "
OPTION              ="    <option value='{0}'>{1}</option>"
SELECT              ="  <select name='{0}' {1}>"
INPUT               ="  {0}<input type='text' name='{1}'>"
TEXTAREA            ="  <textarea rows='{0}' cols='{1}'>{2}</textarea>"
LETRAS_PROHIBIDAS_EN_IDS                ="ÁÉÍÓÚáéíóúÑñ "
LETRAS_SUSTITUTAS_DE_PROHIBIDAS_EN_IDS  ="AEIOUaeiouNn_"
DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS=dict()


class GeneradorFormularios(object):
    def __init__(self):
        self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS=dict()
        for pos in range(0, len(LETRAS_PROHIBIDAS_EN_IDS)):
            letra_prohibida=LETRAS_PROHIBIDAS_EN_IDS[pos]
            letra_sustituta=LETRAS_SUSTITUTAS_DE_PROHIBIDAS_EN_IDS[pos]
            self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS[ord(letra_prohibida)]=letra_sustituta
        #print (self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS)
        
    
    
    def get_boolean_aleatorio(self):
        valores=[True, False]
        pos_azar=randint(0, 1)
        return valores[pos_azar]
    
    
    def get_trozo_formulario(self, con_fieldset=True):
        #Algunas funciones aparecen dos veces para aumentar la posibilidad de que aparezcan
        funciones=[self.generar_checkboxes, self.generar_radios,
                   self.generar_options, self.generar_textarea,
                   self.generar_inputs, self.generar_control_fichero, self.generar_control_color,
                   self.generar_fecha, self.generar_hora]
        self.html=""

        shuffle(funciones)
        nuevo_vector=funciones
        nueva_longitud=randint(3, len(nuevo_vector))
        #cantidad_elementos=randint(2,5)
        vector_final=nuevo_vector[0:nueva_longitud]
        #for i in range(1, cantidad_elementos):
        for f in vector_final:
            
            self.html+=f(self.get_boolean_aleatorio())
            self.html+="  <br/>\n"
        if con_fieldset:
            leyenda=self.get_linea_aleatoria(fichero=FICHERO_LEYENDAS)
            leyenda="  <legend>{0}</legend>\n".format(leyenda)
            self.html="<fieldset>\n" + leyenda + self.html + "</fieldset>\n"
        print (self.html)
        return self.html
    
    def get_lineas_fichero(self, nombre_fichero):
        lineas=[]
        f=open(nombre_fichero, "r", encoding="utf-8")
        lineas=f.readlines()
        lineas_sin_fin_de_linea=[]
        for l in lineas:
            lineas_sin_fin_de_linea.append ( l.strip() )
        return lineas_sin_fin_de_linea
    
    def get_linea_aleatoria(self, fichero=FICHERO_OPCIONES):
        lineas=self.get_lineas_fichero(fichero)
        num_azar=randint(0, len(lineas)-1)
        return lineas[num_azar]
    
    def generar_controles(self, cadena_control, con_fin_linea=True):
        html=""
        if cadena_control==RADIO_SIN_ID or cadena_control==RADIO_CON_ID:
            self.descripcion+="* Contiene los siguientes ``radiobuttons``:"
            nombre_control="radio"
        if cadena_control==CHECKBOX_CON_ID or cadena_control==CHECKBOX_SIN_ID:
            self.descripcion+="* Contiene los siguientes ``checkboxes``:"
            nombre_control="checkbox"
        linea=self.get_linea_aleatoria()
        opciones=linea.split(":")
        descripciones=[]
        for o in opciones[1:]:
            valor=o.lower()
            valor=valor.translate(self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS)
            valor=opciones[0]+valor
            descripciones.append(nombre_control+" con el ``name``  \"{0}\" , ``value``  \"{1}\"  y el texto \"{2}\"".format(opciones[0], valor, o))
            if con_fin_linea:
                html+=cadena_control.format(opciones[0], o, valor) + "  <br/>\n"
            else:
                html+=cadena_control.format(opciones[0], o, valor) +"\n"
        self.descripcion+=", ".join(descripciones)
        self.descripcion+=".\n"
        return html
    
    def generar_radios(self, con_fin_linea=True):
        resultado= self.generar_controles ( RADIO_SIN_ID, con_fin_linea )
        return resultado
    
    def generar_checkboxes(self, con_fin_linea=True):
        resultado= self.generar_controles ( CHECKBOX_SIN_ID, con_fin_linea )
        return resultado
    
    def generar_textarea(self, con_fin_linea=True):
        linea=self.get_linea_aleatoria(FICHERO_TEXTAREAS)
        filas=randint(4,8)
        columnas=randint(45,60)
        area=TEXTAREA.format(filas, columnas, linea)
        self.descripcion+="* Hay un ``textarea`` que mide {0} filas y {1} columnas que lleva dentro el texto \"{2}\"\n".format(
            filas, columnas, linea
        )
        return area
    
    def generar_inputs(self, con_fin_linea=True):
        html=""
        linea=self.get_linea_aleatoria(FICHERO_INPUTS)
        self.descripcion+="* Hay los siguientes cuadros de texto:"
        trozos=linea.split("-")
        descripciones=[]
        for t in trozos:
            (nombre, texto)=t.split(":")
            descripciones.append("cuadro de texto con el texto \"{0}\" y el ``name`` {1}".format(
                texto, nombre)
            )
            if con_fin_linea:
                
                html+=INPUT.format(texto, nombre) + " <br/>\n"
            else:
                html+=INPUT.format(texto, nombre) + "\n"
        
        self.descripcion+=", ".join(descripciones)
        self.descripcion+="\n"
        return html
            
        
    def generar_formulario(self):
        self.html=""
        self.descripcion=""
        formulario="<form>\n"
        for i in range(1, randint(2,3)):
            formulario+=self.get_trozo_formulario(con_fieldset=True)
        formulario+="</form>\n"
        return formulario
    
    def get_descripcion(self):
        return self.descripcion

    def generar_control_fichero(self, con_fin_linea=True):
        self.descripcion+="* Hay un control para elegir ficheros.\n"
        html="  Elija un fichero:<input type=\"file\">"
        return html

    def generar_control_color(self, con_fin_linea=True):
        self.descripcion+="* Hay un control para elegir el color.\n"
        html="  Elija un color:<input type=\"color\">"
        return html
    
    def generar_fecha(self, con_fin_linea=True):
        self.descripcion+="* Hay un control para indicar la fecha.\n"
        html="  Elija una fecha:<input type=\"date\">"
        return html

    def generar_hora(self, con_fin_linea=True):
        self.descripcion+="* Hay un control para indicar la hora.\n"
        html="  Elija una hora:<input type=\"time\">"
        return html

    def generar_options(self,  multiple=True):
        linea=self.get_linea_aleatoria()
        opciones=linea.split(":")
        
        if multiple:
            html=SELECT.format(opciones[0], "multiple='multiple'")
            self.descripcion+="* Hay una lista desplegable múltiple con el ``name`` \"{0}\" y con las siguientes opciones: ".format(opciones[0])
        else:
            html=SELECT.format(opciones[0], "")
            self.descripcion+="* Hay una lista desplegable con el ``name`` \"{0}\" y con las siguientes opciones: ".format(opciones[0])
        html+="\n"
        descripcion_opciones=[]
        for o in opciones[1:]:
            valor=opciones[0]+"_"+o
            id=o.lower()
            id=id.translate(self.DICCIONARIO_REEMPLAZOS_LETRAS_PROHIBIDAS)
            descripcion_opciones.append(
                "opción \"{0}\" con el ``value`` {1}".format(o, id))
            html+=OPTION.format(id, o, id)  + "\n"
        self.descripcion+=", ".join(descripcion_opciones)
        self.descripcion+=".\n"
        html+="  </select>\n"
        return html     
    

    def convertir_cad_unicode_a_codificacion(self, cad, nueva_codificacion):
        bytes_cad=bytes(cad, nueva_codificacion)
        cad_nueva=bytes_cad.decode(nueva_codificacion)
        return cad_nueva
    
    def guardar(self, html, nombre_archivo, codificacion_a_usar="latin-1"):
        html=self.convertir_cad_unicode_a_codificacion(html, codificacion_a_usar)
        fichero=open(nombre_archivo, "w", encoding=codificacion_a_usar)
        fichero.write ( html )
        fichero.close()
    

if __name__ == '__main__':
    g=GeneradorFormularios()
    nombre=sys.argv[1]
    
    codificacion_a_usar="latin-1"
    html=g.generar_formulario()
    g.guardar(html, nombre)
    print (g.get_descripcion())
#print(html)

