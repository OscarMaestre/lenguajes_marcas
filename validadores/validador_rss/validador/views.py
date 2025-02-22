#coding=utf-8
from django.shortcuts import render
from django import forms
import feedparser
from lxml import etree
from lxml.etree import XMLSyntaxError


# Create your views here.
import os



class Formulario(forms.Form):
    rss= forms.CharField(max_length=16384, widget=forms.Textarea)
    
    

def cargar_esquema(fichero):
    with open(fichero, "r") as f:
        lineas=f.readlines();
        
    esquema="".join(lineas)
    return esquema

def validar(peticion):
    formulario=None
    contexto=dict()
    contexto["dato"]="R"
    if peticion.method=="POST":
        formulario=Formulario(peticion.POST)
        if formulario.is_valid():
            texto_rss=formulario.cleaned_data["rss"]
            esquema=cargar_esquema("validador/rss-2_0.xsd")
            schema = etree.XMLSchema(etree.XML(esquema))
            parser=etree.XMLParser(schema=schema)
            try:
                raiz=etree.fromstring(texto_rss, parser)
            except XMLSyntaxError as e:
                print(e)
                respuesta=str(e)
                contexto={
                    "respuesta":respuesta
                }
                return render(peticion, "validador/respuesta.html", contexto)
            contexto={
                    "respuesta":"Todo parece estar bien"
            }
            return render(peticion, "validador/respuesta.html", contexto)
            
        else:
            print("No es valido")
    else:
        fo=Formulario()
        contexto={
            "fo":fo,
            "dato":"R"
        }
        contexto["dd"]="DDD"
    print("Renderizando formulario")
    print(contexto)
    return render(peticion, "validador" + os.sep +"validar.html", contexto)