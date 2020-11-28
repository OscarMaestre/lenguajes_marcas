#!/usr/bin/env python3
import os
from texttable import Texttable
from random import randint
from utilidades.genericas.Utilidades import Utilidades
from utilidades.ficheros.GestorFicheros import GestorFicheros


PLANTILLA_ANEXO="""
Anexo: ejercicios sobre "grids"
=====================================

{0}
"""

PLANTILLA_HTML="""
<!DOCTYPE html>
<html>
<head>
<title>{0}</title>
<meta charset="utf-8">
<style>
{1}
</style>
</head>  
<body>
Este ejercicio muestra una disposición de rejilla como esta ({4} filas y {5} columnas)
<pre>
{3}
</pre>
{2}  
</body>
</html>
"""

class PropiedadCSS(object):
    def __init__(self, nombre_propiedad, lista_posibles_valores, 
                        texto_nombre, textos_valores):
        self.nombre_propiedad=nombre_propiedad
        self.lista_posibles_valores=lista_posibles_valores
        self.texto_nombre=texto_nombre
        self.textos_valores=textos_valores

        self.valor_azar=self.set_propiedad_azar()
        self.texto=self.texto_nombre.format(self.valor_azar_txt)

    def set_propiedad_azar(self):
        pos_azar=randint(0, len(self.lista_posibles_valores)-1)
        self.valor_azar=self.lista_posibles_valores[pos_azar]
        self.valor_azar_txt=self.textos_valores[pos_azar]

    @staticmethod
    def get_lista_propiedades():
        lista_posibilidades=[]
        lista_posibilidades.append(
            PropiedadCSS("text-align", ["left", "right", "center", "justify"],
            "El texto está {0}.", ["alineado a la izquierda", "alineado a la derecha",
            "centrado", "justificado"])
        )
        lista_posibilidades.append(
            PropiedadCSS("background-image", ["fondo1.jpg", "imagen.png", "imagen2.jpg", "fondo2.jpg"],
            "Se usa una imagen de fondo con el nombre {0}.",
             ["fondo1.jpg", "imagen.png", "imagen2.jpg", "fondo2.jpg"] 
            )
        )

        return lista_posibilidades



class Region:
    def __init__(self, x0,xf, y0, yf):
        self.x0=x0
        self.xf=xf
        self.y0=y0
        self.yf=yf
        self.subregiones=[]

    def set_nombre(self, nombre):
        self.nombre=nombre
    def set_texto_asociado(self, texto):
        self.texto_asociado=texto

    #Dados dos valores, este método escoge un valor más o menos en el centro del
    #intervalo (con una desviación de entre +1 y -1)
    def get_valor_intermedio(self, n1, n2):
        
        #La doble barra es "division entera, no usar decimales"
        #asi que 5//2 es 2 y no 2.5
        intermedio=(n2-n1)//2
        return n1+intermedio
        
    def get_informacion_corte(self, reg1, reg2, mensaje):
        print("Hacemos el corte en "+mensaje)
        print("La region con estas coordenadas")
        print(self.get_coordenadas())
        print("Se divide en dos")
        print("--------Region 1-------")
        print(reg1.get_coordenadas())
        print("--------Fin reg 1-------")
        print("--------Region 2-------")
        print(reg2.get_coordenadas())
        print("--------Fin reg 2-------")
        return

    def dividir_en_dos_partes(self):
        #Es más cómodo usar estas variables
        x0=self.x0
        y0=self.y0
        xf=self.xf
        yf=self.yf
        if randint(0,1)==0:
            #Dividimos en horizontal
            #Primero escogemos una fila por donde cortar asegurándonos
            #de que no elegimos la primera fila o la última (no se 
            #haría ningún corte)
            
            fila_por_donde_cortamos=self.get_valor_intermedio(y0, yf)
            #print("Fila pivote:"+str(fila_por_donde_cortamos))
            subregion_superior=Region(x0,xf,y0,fila_por_donde_cortamos)
            subregion_inferior=Region(x0,xf,fila_por_donde_cortamos, yf)
            #self.get_informacion_corte(subregion_superior, subregion_inferior, "horizontal")
            return (subregion_inferior, subregion_superior)
            pass
        else:
            columna_por_donde_cortamos=self.get_valor_intermedio(x0, xf)
            #print("Columna pivote:"+str(columna_por_donde_cortamos))
            subregion_izquierda=Region(x0,columna_por_donde_cortamos, y0,yf)
            subregion_derecha  =Region(columna_por_donde_cortamos,xf, y0,yf)
            #self.get_informacion_corte(subregion_derecha, subregion_izquierda, "vertical")
            return (subregion_izquierda, subregion_derecha)
            #Dividimos en vertical

    def dividir_en_regiones(self, num_regiones):
        #Partimos de esta misma region
        self.subregiones=[self]
        num_paso=0
        while len(self.subregiones)<num_regiones:
            num_paso=num_paso+1
            # print("**********Paso {0}*************".format(num_paso))
            # print(self)
            # print("**********Fin paso {0}*************".format(num_paso))
            #Escogemos una región al azar
            pos_al_azar=randint(0, len(self.subregiones)-1)
            #Dividimos esa región en dos y obtenemos dos trozos
            region_a_dividir=self.subregiones[pos_al_azar]
            (trozo1, trozo2)=region_a_dividir.dividir_en_dos_partes()
            #Quitamos la región y añadimos los dos trozos en que se ha dividido
            self.subregiones.remove(region_a_dividir)
            self.subregiones.append(trozo1)
            self.subregiones.append(trozo2)
        return self.subregiones

    def get_coordenadas(self):
        cadena="x0:{0}, xf:{1}, y0:{2}, yf:{3}".format(self.x0, self.xf, self.y0, self.yf)
        return cadena
    def get_informacion_depuracion(self):
        cadena=self.get_coordenadas()
        return cadena+"\n"+self.__str__()

    def get_como_matriz(self):
        texto_region=[["X" for x in range(self.x0, self.xf)] for y in range(self.y0, self.yf)]
        numero=0
        for reg in self.subregiones:
            cadena="x0:{0}, xf:{1}, y0:{2}, yf:{3}".format(reg.x0, reg.xf, reg.y0, reg.yf)
            #print(cadena)
            numero=numero+1
            #print ("Region:"+str(numero))
            for x in range(reg.x0, reg.xf):
                #print()
                for y in range(reg.y0, reg.yf):
                    formato="x0:{0}, y0:{1}"
                    #print (formato.format(x,y))
                    texto_region[y][x]=str(numero)
        return texto_region

    def __str__(self):
        texto_region=self.get_como_matriz()
        filas=["".join(fila) for fila in texto_region]
        texto_tabla="\n".join(filas)
        return texto_tabla

    def get_txt_como_tabla_sphinx(self):
        print(str(self))
        cadena="x0:{0}, xf:{1}, y0:{2}, yf:{3}".format(self.x0, self.xf, self.y0, self.yf)
        print(cadena)
        tabla=Texttable()
        matriz=self.get_como_matriz()
        pos_x=0
        fila_encabezado=["X"]
        ANCHO_COLUMNAS=8
        anchuras=[ANCHO_COLUMNAS]
        for x in range(self.x0, self.xf):
            pos_x=pos_x+1
            texto_encabezado_columna=" **C{0}** ".format(pos_x)
            fila_encabezado.append(texto_encabezado_columna)
            anchuras.append(len(texto_encabezado_columna))
        tabla.set_cols_width(anchuras)
        print(fila_encabezado)
        tabla.add_row(fila_encabezado)

        num_fila=0
        for y in range(self.y0, self.yf):
            fila=[]
            num_fila=num_fila+1
            texto_num_fila=" **F{0}** ".format(num_fila)
            fila.append(texto_num_fila)
            for x in range(self.x0,self.xf):
                fila.append(matriz[y][x])
            print(fila)
            tabla.add_row(fila)
        return tabla.draw()

        



class GridHTML(object):

    def __init__(self,  min_filas=9, max_filas=12, 
                        min_columnas=9, max_columnas=12, 
                        min_regiones=3, max_regiones=6):

        self.filas          =randint(min_filas, max_filas)
        self.columnas       =randint(min_filas, max_columnas)
        self.num_regiones   =randint(min_regiones, max_regiones
        )
        self.region         =Region(0, self.columnas, 0, self.filas)
        self.regiones       =self.region.dividir_en_regiones(self.num_regiones)
        self.rellenar_regiones()

    def generar_enunciado(self, nombre_ejercicio):

        html=self.get_html()
        css=self.get_css_grid()
        rejilla=str(self.region)
        contenido_sin_solucion=PLANTILLA_HTML.format(nombre_ejercicio, "", html, rejilla, self.filas, self.columnas)

        contenido_con_solucion=PLANTILLA_HTML.format(nombre_ejercicio, css, html, rejilla, self.filas, self.columnas)

        tabla_sphinx=self.region.get_txt_como_tabla_sphinx()

        diccionario=dict()
        diccionario["titulo"]       =nombre_ejercicio
        diccionario["num_divs"]     =self.num_regiones
        diccionario["html"]         =Utilidades.anadir_tabuladores(contenido_sin_solucion)
        diccionario["num_filas"]    =self.filas
        diccionario["num_columnas"] =self.columnas
        diccionario["solucion_html"]=Utilidades.anadir_tabuladores(contenido_con_solucion)
        diccionario["tabla_sphinx"] =tabla_sphinx

        gf=GestorFicheros()
        resultado=gf.rellenar_fichero_plantilla("plantilla_ejercicio_grids.txt", diccionario)
        return resultado

    def rellenar_regiones (self):
        lista_identificadores=["caja", "columna", "bloque"]
        pos_azar_id=randint(0, len(lista_identificadores)-1)
        identificador=lista_identificadores[pos_azar_id]
        num_region=0
        trozos_html=[]
        for r in self.regiones:
            num_region+=1
            identificador_div=identificador+str(num_region)
            r.set_nombre(identificador_div)

            num_repeticiones_texto=randint(10,20)
            texto=("Texto "+str(num_region)+" ")*num_repeticiones_texto
            num_columnas=26
            trozos_texto_ajustado= ["\t"+texto[i:i+num_columnas] for i in range(0, len(texto), num_columnas)]
            texto_ajustado="\n".join(trozos_texto_ajustado)
            r.set_texto_asociado(texto_ajustado)

    def get_html(self):
        num_region=0
        trozos_html=[]
        for r in self.regiones:
            identificador_div=r.nombre
            texto_region=r.texto_asociado
            html="<div id='{0}'>\n{1}\n</div>".format(identificador_div, texto_region)
            trozos_html.append(html)
        html_interno="\n".join(trozos_html)
        lista_identificadores_globales=["contenedorglobal", "container", "contenedor"]
        pos_azar_id=randint(0, len(lista_identificadores_globales)-1)
        identificador=lista_identificadores_globales[pos_azar_id]
        self.identificador_contenedor=identificador;
        html="<div id='{0}'>\n{1}\n</div>".format(identificador, html_interno)
        html_alineado=Utilidades.embellecer_html(html)
        return html_alineado

    def get_css_grid(self):
        #Primero indicamos los datos del contenedor global
        filas_global= "1fr "*self.filas
        cols_global = "1fr "*self.columnas
        css_filas_global="\tgrid-template-rows:   {0};".format(filas_global)
        css_cols_global ="\tgrid-template-columns:{0};".format(cols_global)
        datos_coords="\n".join([css_filas_global, css_cols_global])
        css_global="#{0}{{\n\tdisplay:grid;\n{1}\n}}\n".format(self.identificador_contenedor, datos_coords)

        #Ahora indicamos el CSS de los trozos
        lista_css=[css_global]
        fila="\tgrid-row:     {0}/{1};"
        col ="\tgrid-column:  {0}/{1};"
        borde="\tborder    :  solid 1px black;"
        margen="\tmargin   :  3px;"
        css="#{0}{{\n{1}\n}}"
        for r in self.regiones:
            fila_region=fila.format(1+r.y0, r.yf+1)
            col_region = col.format(1+r.x0, r.xf+1)
            coordenadas="\n".join([fila_region, col_region, borde, margen])
            css_region=css.format(r.nombre, coordenadas)
            lista_css.append(css_region)
        return "\n".join(lista_css)
        
    def get_html_con_solucion(self, nombre_ejercicio):
        html=self.get_html()
        css=self.get_css_grid()
        rejilla=str(self.region)
        contenido=PLANTILLA_HTML.format(nombre_ejercicio, css, html, rejilla, self.filas, self.columnas)
        return Utilidades.embellecer_html(contenido)

    def get_html_sin_solucion(self, nombre_ejercicio):
        html=self.get_html()
        rejilla=str(self.region)
        contenido=PLANTILLA_HTML.format(nombre_ejercicio, "", html, rejilla, self.filas, self.columnas)
        return Utilidades.embellecer_html(contenido)
        
    

    def generar_archivo_solucion(self, nombre_ejercicio, nombre_archivo):
        contenido_archivo=self.get_html_con_solucion(nombre_ejercicio)
        with open(nombre_archivo, "w") as fichero:
            fichero.write(contenido_archivo)
    


if __name__ == "__main__":
    enunciados=[]
    DIRECTORIO_SOLUCIONES="enunciados"
    for num_ejercicio in range(1, 20):
        
        nombre_formateado="{0:02}".format(num_ejercicio)
        grid=GridHTML()
        nombre_archivo="Ejercicio-{0}.html".format(nombre_formateado)
        #ruta_archivo=os.path.join(DIRECTORIO_SOLUCIONES, nombre_archivo)
        nombre_ejercicio="Ejercicio {0}".format(nombre_formateado)
        #grid.generar_archivo_solucion(nombre_ejercicio, ruta_archivo)
        enunciado=grid.generar_enunciado(nombre_ejercicio)
        enunciados.append(enunciado)
        #print(grid.region.get_txt_como_tabla_sphinx())
    
    texto_enunciados="\n".join(enunciados)
    texto_anexo=PLANTILLA_ANEXO.format(texto_enunciados)
    ruta_anexo="anexo.rst"
    with open(ruta_anexo, "w") as fich:
        fich.write(texto_anexo)

