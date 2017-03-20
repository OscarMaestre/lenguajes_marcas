#!/usr/bin/env python3
#coding=utf-8


from random import randint



def generar_rango (limite_inferior, limite_superior):
    """Devuelve un rango de valores al azar comprendido entre [limite_inferior
        y limite_superior]"""
    n1=randint(limite_inferior, limite_superior)
    n2=randint(limite_inferior, limite_superior)
    if n2<n1:
        return (n2, n1)
    return (n1, n2)

def boolean_al_azar():
    num=randint(0, 1)
    if (num==0):
        return True
    return False

class GeneradorTiposSimples(object):
    PLANTILLA_TIPOS="<xsd:element name=\"{0}\" type=\"xsd:{1}\" {2} />"
    PLANTILLA_ATRIBUTOS="<xsd:attribute name=\"{0}\" type=\"xsd:{1}\"/>"
    @staticmethod
    def get_elemento_simple(nombre_elemento, nombre_tipo, otros=""):
        resultado=GeneradorTiposSimples.PLANTILLA_TIPOS.format(nombre_elemento, nombre_tipo, otros)
        return resultado
    @staticmethod
    def get_atributo_simple(nombre_atributo, nombre_tipo):
        resultado=GeneradorTiposSimples.PLANTILLA_TIPOS.format(nombre_elemento, nombre_tipo)
        return resultado
    
class GeneradorTiposSimplesNumericos(object):
    TIPOS_ELEGIR=[ ("byte",             -128,           127         ),
                   ("short",            -32768,         32767       ),
                   #("int",             -2147483648,    2147483647  ),
                   ("int",              -1000000,       1000000     ),
                   ("long",             -1000000,       1000000     ),
                   ("unsignedByte",      0,             255         ),
                   ("unsignedShort",     0,             65535       ),
                   #("int",      -2147483648,    2147483647         ),
                   ("unsignedInt",       0,             10000000    ),
                   ("unsignedLong",      0,             1000000000  )
                ]
        
    
    def generar( self, nombre_elemento, nombre_tipo="ELEGIR"):
        
        pos=randint(0, len(GeneradorTiposSimplesNumericos.TIPOS_ELEGIR)-1)
        self.valor_minimo=GeneradorTiposSimplesNumericos.TIPOS_ELEGIR[pos][1]
        self.valor_maximo=GeneradorTiposSimplesNumericos.TIPOS_ELEGIR[pos][2]
        self.nombre_elemento=nombre_elemento
        if nombre_tipo=="ELEGIR":
            self.tipo=GeneradorTiposSimplesNumericos.TIPOS_ELEGIR[pos][0]
        else:
            self.tipo=nombre_tipo
        self.descripcion="* Elemento ``{0}`` de tipo ``{1}``.".format(
                                self.nombre_elemento, self.tipo)
        self.diccionario_atributos=dict()
        self.generar_rangos()
    
    def generar_limites_fraccionarios(self):
        usar_solo_limite_cantidad_decimales=boolean_al_azar()
        if usar_solo_limite_cantidad_decimales:
            pass
            
    def generar_rangos(self):
        usar_limite_inferior_y_superior_a_la_vez=boolean_al_azar()
        if (usar_limite_inferior_y_superior_a_la_vez):
            
            (limite_inf_elegido, limite_sup_elegido)=generar_rango(
                self.valor_minimo, self.valor_maximo)
            self.descripcion+="El valor minimo debe ser {0}".format(limite_inf_elegido)
            self.descripcion+=" y el valor maximo debe ser {0}\n".format(limite_sup_elegido)
            self.diccionario_atributos["minInclusive"]=str(limite_inf_elegido)
            self.diccionario_atributos["maxInclusive"]=str(limite_sup_elegido)
        else:
            usar_solo_limite_inferior=boolean_al_azar()
            if usar_solo_limite_inferior:
                limite_inf_elegido=randint(self.valor_minimo, self.valor_maximo)
                self.descripcion+="El valor minimo debe ser {0}\n".format(limite_inf_elegido)
                self.diccionario_atributos["minInclusive"]=str(limite_inf_elegido)
                return
            usar_solo_limite_superior=boolean_al_azar()
            if usar_solo_limite_superior:
                limite_sup_elegido=randint(self.valor_minimo, self.valor_maximo)
                self.descripcion+="El valor máximo debe ser {0}\n".format(limite_sup_elegido)
                self.diccionario_atributos["maxInclusive"]=str(limite_sup_elegido)
                return
            
    def get_descripcion(self):
        return self.descripcion
    
    def get_esquema(self):
        otros=""
        #print(self.diccionario_atributos)
        for (clave, valor) in self.diccionario_atributos.items():
            otros+=" {0}=\"{1}\"".format(clave, valor)
            
        esquema=GeneradorTiposSimples.get_elemento_simple(
            self.nombre_elemento, self.tipo, otros)
        return esquema
    
    
class Elemento(object):
    def __init__(self, nombre, tipo, minOccurs=None, maxOccurs=None):
        self.nombre     =       nombre
        self.tipo       =       tipo
        self.minOccurs  =       minOccurs
        self.maxOccurs  =       maxOccurs
        
    def __str__(self):
        plantilla="<xsd:element name=\"{0}\" type=\"{1}\" {2} />"
        apariciones=[]
        if self.minOccurs!=None:
            apariciones.append ( "minOccurs="+str(self.minOccurs) )
        if self.maxOccurs!=None:
            apariciones.append ( "maxOccurs="+str(self.maxOccurs) )
        resto=" ".join ( apariciones )
        cadena = plantilla.format (self.nombre, self.tipo, resto)
        return cadena
            
class Atributo(object):
    def __init__(self, nombre, tipo, requerido=False):
        self.nombre     =       nombre
        self.tipo       =       tipo
        self.requerido  =       requerido
        
    def __str__(self):
        plantilla="<xsd:attribute name=\"{0}\" type=\"{1}\" {2}/>"
        if self.requerido:
            requerido="use=\"required\""
        else:
            requerido=""
        cadena = plantilla.format (self.nombre, self.tipo, requerido)
        return cadena
    
class TipoConHijos(object):
    def __init__(self, nombre, secuencia=True, lista_elementos=None, lista_atributos=None ):
        self.nombre             =       nombre
        self.secuencia          =       secuencia
        self.lista_elementos    =       lista_elementos
        self.lista_atributos    =       lista_atributos
        
    
    def get_hijos(self):
        if self.secuencia==True:
            plantilla="""<xsd:sequence>
            {0}\r\n</xsd:sequence>"""
        else:
            plantilla="""<xsd:choice>
            {0}\r\n</xsd:choice>"""
            
        cad_hijos=[]
        for h in self.lista_elementos:
            cad_hijos.append(str(h))
        hijos= "\r\n".join(cad_hijos)
        return plantilla.format(hijos)
    
    def get_atributos(self):
        return "\r\n".join([str(atributo) for atributo in self.lista_atributos])
        
    def __str__(self):
        plantilla_cc="""
        <xsd:complexType name="{0}">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    {1}
                </xsd:restriction>
                {2}
            </xsd:complexContent>
        <xsd:complexType>
        """
        
        return plantilla_cc.format(self.nombre, self.get_hijos(), self.get_atributos())
        
class TipoConSoloAtributos(object):
    def __init__(self, nombre,  tipo, lista_atributos=None ):
        self.nombre             =       nombre
        self.tipo               =       tipo
        self.lista_atributos    =       lista_atributos
        
    
    
    def get_atributos(self):
        return "\r\n".join([str(atributo) for atributo in self.lista_atributos])
        
    def __str__(self):
        plantilla_cc="""
        <xsd:complexType name="{0}">
            <xsd:simpleContent>
                <xsd:extension base="{1}">
                    {2}
                </xsd:extension>
            </xsd:simpleContent>
        <xsd:complexType>
        """
        
        return plantilla_cc.format(self.nombre, self.tipo,  self.get_atributos())
    
        
class TipoSimpleCadenaConPatron(object):
    def __init__(self, nombre_tipo, patron):
        self.nombre_tipo    =   nombre_tipo
        self.patron         =   patron
        
    def __str__(self):
        plantilla="""
        <xsd:simpleType name="{0}">
            <xsd:restriction base="xsd:string">
                <xsd:pattern value="{1}"/>
            </xsd:restriction>
        </xsd:simpleType>
        """
        cadena=plantilla.format(self.nombre_tipo, self.patron)
        return cadena
    
class TipoSimpleCadenaConEnumeracion(object):
    def __init__(self, nombre_tipo, lista_valores):
        self.nombre_tipo    =   nombre_tipo
        self.lista_valores  =   lista_valores
        
    def __str__(self):
        plantilla_enumeracion="<xsd:enumeration value=\"{0}\"/>"
        enumeraciones=[]
        for v in self.lista_valores:
            enumeraciones.append(plantilla_enumeracion.format(v))
        plantilla="""
        <xsd:simpleType name="{0}">
            <xsd:restriction base="xsd:string">
                {1}
            </xsd:restriction>
        </xsd:simpleType>
        """
        cadena=plantilla.format(self.nombre_tipo, "\r\n".join(enumeraciones))
        return cadena

class TipoNumerico(object):
    def __init__(self, nombre, tipo, minimo=None, maximo=None,
                 digitos_totales=None, digitos_fraccionarios=None):
        self.nombre                 =       nombre
        self.tipo                   =       tipo
        self.minimo                 =       minimo
        self.maximo                 =       maximo
        self.digitos_totales        =       digitos_totales
        self.digitos_fraccionarios  =       digitos_fraccionarios
        
    def __str__(self):
        plantilla="""
        <xsd:simpleType name="{0}">
            <xsd:restriction base="{1}">
                {2}
            </xsd:restriction>
        </xsd:simpleType>
        """
        
        restricciones=[]
        if self.minimo!=None:
            restricciones.append("<xsd:minInclusive value=\"{0}\" />".format(self.minimo))
        if self.maximo!=None:
            restricciones.append("<xsd:maxInclusive value=\"{0}\" />".format(self.maximo))
        if self.digitos_totales!=None:
            restricciones.append("<xsd:totalDigits value=\"{0}\" />".format(self.digitos_totales))
        if self.digitos_fraccionarios!=None:
            restricciones.append("<xsd:fractionDigits value=\"{0}\" />".format(self.digitos_fraccionarios))
        cad="\r\n".join([str(r) for r in restricciones])
        return plantilla.format(self.nombre, self.tipo, cad)
    