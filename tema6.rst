===========================================
Recuperación de información
===========================================


Introducción
===========================================
En este tema veremos que podemos recuperar información de archivos XML *igual* que si fuesen bases de datos. Para ello podemos usar dos cosas:

* Un lenguaje de programación de propósito general, como es Java.
* O un lenguaje de programación especializado como es XQuery.

En líneas generales hay dos grandes formas de usar un lenguaje de programación como Java para leer o escribir archivos XML.

* DOM: significa Document Object Model (o Modelo del objeto documento). DOM en general almacena los archivos en memoria lo que es mucho más rápido y eficiente.
* SAX: en algunos casos, los archivos muy grandes, pueden no caber en memoria. SAX proporciona otras clases y métodos distintos para ir procesando un archivo por partes. SAX significa Simple Access for XML, pero en general es un poco más complicado. En este módulo, no lo veremos.

DOM es un estándar y sus clases y métodos existen en muchos otros lenguajes.


XQuery
=============

Para empezar **XQuery es un superconjunto de XPath** por lo que las expresiones básicas de XQuery también servirán en XQuery. La primera diferencia es que en XQuery tendremos que usar la función ``doc`` para cargar un archivo y luego navegar por él. Supongamos que tenemos un archivo de ejemplo como este:

.. code-block:: xml

    <datos>
        <proveedores>
            <proveedor numprov="v1">
                <nombreprov>Smith</nombreprov>
                <estado>20</estado>
                <ciudad>Londres</ciudad>
            </proveedor>
            <proveedor numprov="v2">
                <nombreprov>Jones</nombreprov>
                <estado>10</estado>
                <ciudad>Paris</ciudad>
            </proveedor>
            <proveedor numprov="v3">
                <nombreprov>Blake</nombreprov>
                <estado>30</estado>
                <ciudad>Paris</ciudad>
            </proveedor>
            <proveedor numprov="v4">
                <nombreprov>Clarke</nombreprov>
                <estado>20</estado>
                <ciudad>Londres</ciudad>
            </proveedor>
            <proveedor numprov="v5">
                <nombreprov>Adams</nombreprov>
                <estado>30</estado>
                <ciudad>Atenas</ciudad>
            </proveedor>       
        </proveedores>
        <partes>
            <parte numparte="p1">
                <nombreparte>Tuerca</nombreparte>
                <color>Rojo</color>
                <peso>12</peso>
                <ciudad>Londres</ciudad>
            </parte>
            <parte numparte="p2">
                <nombreparte>Perno</nombreparte>
                <color>Verde</color>
                <peso>17</peso>
                <ciudad>Paris</ciudad>
            </parte>
            <parte numparte="p3">
                <nombreparte>Tornillo</nombreparte>
                <color>Azul</color>
                <peso>17</peso>
                <ciudad>Roma</ciudad>
            </parte>
            <parte numparte="p4">
                <nombreparte>Tornillo</nombreparte>
                <color>Rojo</color>
                <peso>14</peso>
                <ciudad>Londres</ciudad>
            </parte>
            <parte numparte="p5">
                <nombreparte>Leva</nombreparte>
                <color>Azul</color>
                <peso>12</peso>
                <ciudad>Paris</ciudad>
            </parte>
            <parte numparte="p6">
                <nombreparte>Engranaje</nombreparte>
                <color>Rojo</color>
                <peso>19</peso>
                <ciudad>Londres</ciudad>
            </parte>
        </partes>
        <proyectos>
            <proyecto numproyecto="y1">
                <nombreproyecto>Clasificador</nombreproyecto>
                <ciudad>Paris</ciudad>
            </proyecto>
            <proyecto numproyecto="y2">
                <nombreproyecto>Monitor</nombreproyecto>
                <ciudad>Roma</ciudad>
            </proyecto>
            <proyecto numproyecto="y3">
                <nombreproyecto>OCR</nombreproyecto>
                <ciudad>Atenas</ciudad>
            </proyecto>
            <proyecto numproyecto="y4">
                <nombreproyecto>Consola</nombreproyecto>
                <ciudad>Atenas</ciudad>
            </proyecto>
            <proyecto numproyecto="y5">
                <nombreproyecto>RAID</nombreproyecto>
                <ciudad>Londres</ciudad>
            </proyecto>
            <proyecto numproyecto="y6">
                <nombreproyecto>EDS</nombreproyecto>
                <ciudad>Oslo</ciudad>
            </proyecto>
            <proyecto numproyecto="y7">
                <nombreproyecto>Cinta</nombreproyecto>
                <ciudad>Londres</ciudad>
            </proyecto>
        </proyectos>
        <suministros>
            <suministra>
                <numprov>v1</numprov>
                <numparte>p1</numparte>
                <numproyecto>y1</numproyecto>
                <cantidad>200</cantidad>
            </suministra>
            <suministra>
                <numprov>v1</numprov>
                <numparte>p1</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>700</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p3</numparte>
                <numproyecto>y1</numproyecto>
                <cantidad>400</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p3</numparte>
                <numproyecto>y2</numproyecto>
                <cantidad>200</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p3</numparte>
                <numproyecto>y3</numproyecto>
                <cantidad>300</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p3</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>500</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p3</numparte>
                <numproyecto>y5</numproyecto>
                <cantidad>600</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p3</numparte>
                <numproyecto>y6</numproyecto>
                <cantidad>400</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p3</numparte>
                <numproyecto>y7</numproyecto>
                <cantidad>600</cantidad>
            </suministra>
            <suministra>
                <numprov>v2</numprov>
                <numparte>p5</numparte>
                <numproyecto>y2</numproyecto>
                <cantidad>100</cantidad>
            </suministra>
            <suministra>
                <numprov>v3</numprov>
                <numparte>p3</numparte>
                <numproyecto>y1</numproyecto>
                <cantidad>200</cantidad>
            </suministra>
            <suministra>
                <numprov>v3</numprov>
                <numparte>p4</numparte>
                <numproyecto>y2</numproyecto>
                <cantidad>500</cantidad>
            </suministra>
            <suministra>
                <numprov>v4</numprov>
                <numparte>p6</numparte>
                <numproyecto>y3</numproyecto>
                <cantidad>300</cantidad>
            </suministra>
            <suministra>
                <numprov>v4</numprov>
                <numparte>p6</numparte>
                <numproyecto>y7</numproyecto>
                <cantidad>300</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p2</numparte>
                <numproyecto>y2</numproyecto>
                <cantidad>200</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p2</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>100</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p5</numparte>
                <numproyecto>y5</numproyecto>
                <cantidad>500</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p6</numparte>
                <numproyecto>y2</numproyecto>
                <cantidad>200</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p1</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>100</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p3</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>200</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p4</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>800</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p5</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>400</cantidad>
            </suministra>
            <suministra>
                <numprov>v5</numprov>
                <numparte>p6</numparte>
                <numproyecto>y4</numproyecto>
                <cantidad>500</cantidad>
            </suministra>
        </suministros>
    </datos>

En él podríamos ejecutar consultas como estas:
* Recuperar todos los proveedores con ``doc("datos.xml")/datos/proveedores``
* Recuperar todos los datos con ``doc("datos.xml")/datos/``
* Recuperar todas las partes con ``doc("datos.xml")/datos/partes``.

De hecho, podemos usar las mismas consultas con predicados XPath y así por ejemplo extraer los datos del proveedor cuyo numprov es 'v1' con la consulta siguiente::

    doc("datos.xml")/datos/proveedores/proveedor[@numprov='v1']
    
Que devuelve este resultado:

.. code-block:: xml

    <proveedor numprov="v1">
        <nombreprov>Smith</nombreprov>
        <estado>20</estado>
        <ciudad>Londres</ciudad>
    </proveedor>
    
Extraer los datos de partes cuyo color sea 'Rojo'. La consulta XQuery sería::

    doc("datos.xml")/datos/partes/parte[color='Rojo']

Y el resultado sería:

.. code-block:: xml

    <parte numparte="p1">
        <nombreparte>Tuerca</nombreparte>
        <color>Rojo</color>
        <peso>12</peso>
        <ciudad>Londres</ciudad>
    </parte>
    <parte numparte="p4">
        <nombreparte>Tornillo</nombreparte>
        <color>Rojo</color>
        <peso>14</peso>
        <ciudad>Londres</ciudad>
    </parte>
    <parte numparte="p6">
        <nombreparte>Engranaje</nombreparte>
        <color>Rojo</color>
        <peso>19</peso>
        <ciudad>Londres</ciudad>
    </parte>
        
En XQuery se pueden mezclar las marcas con el programa. Sin embargo, para poder distinguir lo que se tiene que ejecutar de lo que no, tendremos que encerrar nuestras sentencias XQuery entre llaves y dejar las marcas fuera de las llaves.

Así, esta consulta consigue generarnos un XML valido añadiendo un elemento raíz al conjunto de partes::

    <partesrojas>
    {
        doc("datos.xml")/datos/partes/parte[color='Rojo']
    }
    </partesrojas>

El resultado devuelto es este:

.. code-block:: xml

    <partesrojas>
        <parte numparte="p1">
            <nombreparte>Tuerca</nombreparte>
            <color>Rojo</color>
            <peso>12</peso>
            <ciudad>Londres</ciudad>
        </parte><parte numparte="p4">
            <nombreparte>Tornillo</nombreparte>
            <color>Rojo</color>
            <peso>14</peso>
            <ciudad>Londres</ciudad>
        </parte><parte numparte="p6">
            <nombreparte>Engranaje</nombreparte>
            <color>Rojo</color>
            <peso>19</peso>
            <ciudad>Londres</ciudad>
        </parte>
    </partesrojas>
    
Antes se ha mencionado que se puede usar ``WHERE`` para crear condiciones. ¿Como cambiar entonces la consulta anterior para poner la condición en un ``WHERE`` y no meterla entre corchetes?

Si queremos usar un ``where`` es porque queremos filtrar un conjunto de elementos, y si queremos un conjunto de elementos necesitaremos un bucle ``for``. Y a su vez, si recorremos un conjunto de elementos tendremos que hacer algún procesamiento con ellos o al menos devolverlos de la manera normal.

Bucles ``for`` en XQuery
---------------------------

Los bucles de XQuery son parecidos a los de Java. Hay una variable de bucle que iremos procesando de alguna manera. Dicha variable llevará siempre el simbolo del dolar ($). Así, un bucle que recupera todas las partes sería:

.. code-block:: php

    for $p in doc("datos.xml")/datos/partes/parte
    return $p

Si ahora queremos filtrar las partes rojas haremos esto:

.. code-block:: php

    for $p in doc("datos.xml")/datos/partes/parte
    where $p/color='Rojo'
    return $p

Y si ahora queremos un nuevo elemento raíz podremos hacer esto:

.. code-block:: xml

    <partesrojas>
    {
        for $p in doc("datos.xml")/datos/partes/parte
        where $p/color='Rojo'
        return $p
    }
    </partesrojas>
    
.. code-block:: xml
    
    <suministrosgrandes>
    {
        for $suministra
        in doc("datos.xml")/datos/suministros/suministra
        where $suministra/cantidad > 450
        return $suministra
    }
    </suministrosgrandes>
    
Ordenación en XQuery
-------------------------

Si se desea ordenar un conjunto de datos puede usarse la clásula ``order by`` poniendo despues uno o varios elementos o atributos y usando ``ascending`` o ``descending``, de manera similar a SQL.

Así, por ejemplo, para ordenar la consulta anterior por cantidad usaríamos esto:

.. code-block:: xml
    
    <suministrosgrandes>
    {
        for $suministra
        in doc("datos.xml")/datos/suministros/suministra
        where $suministra/cantidad > 450
        order by $suministra/cantidad descending
        return $suministra
    }
    </suministrosgrandes>

Igual que en SQL se pueden combinar varios campos. Si por ejemplo quisiéramos ordenar por proveedor ascendente y luego por parte descendiente haríamos esto.
.. code-block:: xml
    
    <suministrosgrandes>
    {
        for $suministra
        in doc("datos.xml")/datos/suministros/suministra
        where $suministra/cantidad > 450
        order by $suministra/proveedor ascending,
                $suministra/parte descending
        return $suministra
    }
    </suministrosgrandes>



Fundamentos de DOM con Java
===========================================

En primer lugar va a ser necesario importar las clases correctas para poder usar DOM. La línea correcta es

.. code-block:: java

	import javax.xml.parsers.*;
	import org.w3c.dom.*;


Un parser es un programa que analiza la sintaxis de un fichero, en nuestro caso un fichero XML. En castellano se debería decir analizador o analizador gramatical.


	
Ejemplo de base
===========================================

.. code-block:: java

	package com.ies;
	import javax.xml.parsers.*;
	import java.io.File;
	import org.w3c.dom.*;

	public class ProcesadorXML {
		public void procesarArchivo(String nombreArchivo){
			DocumentBuilderFactory fabrica;
			DocumentBuilder constructor;
			Document documentoXML;
			File fichero=new File(nombreArchivo);
			fabrica= 
				DocumentBuilderFactory.newInstance();
			System.out.println("Procesando "+nombreArchivo);
			try {
				constructor=
				  fabrica.newDocumentBuilder();
				documentoXML=constructor.parse(fichero);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			
			
		}
		public static void main (String[] argumentos){
			System.out.println("Probando...");
			ProcesadorXML proc=new ProcesadorXML();
			proc.procesarArchivo("bolsas.xml");
		}
	}
	
	
La clase Document
===========================================

La clase Document es una representación Java que almacena en memoria un archivo XML.Mediante esta clase y otras clases compañeras podremos recorrer cualquier punto del archivo XML.

Este recorrido se basa siempre en la visita de nodos hijo o nodos hermano. No todos los nodos son iguales y se debe tener presente que en un nodo podríamos encontrar que los saltos de línea pueden ser un problema a la hora de recorrer el árbol DOM.

Por ejemplo, dado un documento, se debe empezar obteniendo la raíz. Este elemento se llama también el “elemento documento” y podemos obtenerlo así:


.. code-block:: java

	documento=constructor.parse(archivoXML);
	Element raiz=documento.getDocumentElement();
	System.out.println(raiz.getNodeName());

La clase principal que nos interesa es la clase ``Node``, siendo ``Document`` su clase Hija. Algunos métodos de interés son estos:

* ``getDocumentElement()`` obtiene el elemento raíz, a partir del cual podremos empezar a "navegar" a través de los elementos.
* ``getFirstChild()`` obtiene el primer elemento hijo del nodo que estemos visitando.
* ``getParentNode()`` nos permite obtener el nodo padre de un cierto nodo.
* ``getChildNodes()`` obtiene todos los nodos hijo.
* ``getNextSibling()`` obtiene el siguiente nodo hermano.
* ``getChildNodes()`` devuelve un ``NodeList`` con todos los hijos de un elemento. Esta ``NodeList`` se puede recorrer con un ``for``, obteniendo el tamaño de la lista con ``getLength()`` y extrayendo los elementos con el método ``item(posicion)``
* ``getNodeType()`` es un método que nos indica el tipo de nodo (devuelve un ``short``). Podemos comparar con ``Node.ELEMENT_NODE`` para ver si el nodo es realmente un elemento.
* Otro método de utilidad es ``getElementsByTagName`` que extrae todos los subelementos que tengan un cierto nombre de etiqueta.


.. HINT::

	En general, hay muchas clases que proporcionan más métodos de utilidad, como por ejemplo la clase ``Element``. En muchas ocasiones, podremos hacer un ``cast`` y aprovecharnos de ellos.

Cuando se procesan archivos, se debe tener especial importancia a los espacios en blanco que pueda haber. Estos dos archivos no son iguales:

.. code-block:: xml

	El primer hijo de listado es <futuro>
	<listado><futuro>...</futuro></listado>
	
.. code-block:: xml

	Aquí el primer hijo de listado es \n
	<listado>
		<futuro>...</futuro>
	</listado>


Ejercicios
===========================================

Ejercicio
------------------------------------------------------
Dado el siguiente archivo XML crear un programa que muestre todos los nombres:

.. code-block:: xml
	
	<listaempleados>
		<empleado edad="27">
			<nombre>Pepe Perez</nombre>
			<categoria>Empleado</categoria>
		</empleado>
		<empleado edad="34">
			<nombre>Juan Sanchez</nombre>
			<categoria>Gerente</categoria>
		</empleado>
	</listaempleados>

La solución podría ser algo así:

.. code-block:: java

	public class ProcesadorXML {
		String ruta;
		public ProcesadorXML(String ruta){
			this.ruta=ruta;
		}
		public Element getRaiz() 
				throws ParserConfigurationException, SAXException, IOException{
			DocumentBuilderFactory fabrica;
			fabrica=
			DocumentBuilderFactory.newInstance();
			/* A partir de un fichero XML
			 * crea el objeto documento en memoria*/
			DocumentBuilder creadorObjDocumento;
			creadorObjDocumento=
				fabrica.newDocumentBuilder();
			FileInputStream fich;
			fich=new FileInputStream(this.ruta);
			
			/* Analiza el XML y 
			 * lo carga en memoria */
			Document documento;
			documento=
				creadorObjDocumento.parse(fich);
			Element raiz;
			raiz=documento.getDocumentElement();
			return raiz;
		}
		/* Este método imprime todos los nombres*/
		public void todosNombres() 
				throws ParserConfigurationException, 
					SAXException, IOException
		{
			Element raiz=getRaiz();
			Node hijo=raiz.getFirstChild();
			while (hijo!=null){
				String nombreElemento;
				nombreElemento=hijo.getNodeName();
				if (nombreElemento.equals("empleado")){
					Node hijoFinLinea=hijo.getFirstChild();
					Element hijoNombre=(Element) hijoFinLinea.getNextSibling();
					String contenido=hijoNombre.getTextContent();
					System.out.println("Empleado "+contenido);
				}
				hijo=hijo.getNextSibling();
			}
		}
		public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException {
			ProcesadorXML procesador;
			procesador=new ProcesadorXML(
				"D:/oscar/empleados.xml");
			procesador.todosNombres();
		}
	}
	
Ampliaciones:

* Añadir uno que devuelva todas las edades. 
* Añadir uno que devuelva los nombres de los empleados mayores de 30 (mostrando los nombres pero no las edades).
* Añadir un método que diga cuantos empleados hay. El método debe ser capaz de tolerar que haya muchas líneas en blanco seguidas.
	
El siguiente código resuelve el problema de mostrar los mayores de cierta edad:

.. code-block:: java

	public void mostrarMayoresDe(int edadMinima) 
			throws ParserConfigurationException, 
			SAXException, IOException
	{
		Element raiz=getRaiz();
		Node finLinea=raiz.getFirstChild();
		Element empleado=(Element) finLinea.getNextSibling();
		while (empleado!=null){
			String edad=empleado.getAttribute("edad");
			int iEdad=Integer.parseInt(edad);
			if (iEdad>edadMinima){
				finLinea=empleado.getFirstChild();
				Element elemNombre=(Element) 
						finLinea.getNextSibling();
				String nombreEmpleado=
						elemNombre.getTextContent();
				System.out.println(nombreEmpleado +
						" es mayor de "+iEdad);
			} //Fin del if
			finLinea=empleado.getNextSibling();
			empleado=(Element) finLinea.getNextSibling();
		}	//Fin del while
	} //Fin del método


El método ``getElementsByTagName`` puede facilitar mucho el resolver ciertas tareas. Por ejemplo, supongamos que queremos resolver el problema de contar cuantos empleados hay:

.. code-block:: java

	public int contarEmpleados() 
			throws ParserConfigurationException, SAXException, IOException{
		int numEmpleados=0;
		Element raiz=getRaiz();
		NodeList lista=raiz.getElementsByTagName("empleado");
		numEmpleados=lista.getLength();
		return numEmpleados;
	}	
	

Ejercicio
----------------------------------------------

Extraer la raíz de un archivo XML

.. code-block:: java

	public Node extraerRaiz(String nombreArchivo){
		DocumentBuilderFactory fabrica;
		DocumentBuilder constructor;
		Document documentoXML=null;
		File fichero=new File(nombreArchivo);
		fabrica= 
			DocumentBuilderFactory.newInstance();
		System.out.println("Procesando "+nombreArchivo);
		try {
			constructor=
			  fabrica.newDocumentBuilder();
			documentoXML=constructor.parse(fichero);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return documentoXML.getDocumentElement();
		
	}
	
Ejercicio
---------

Imprimir todos los elementos hijo del archivo XML.


Una posibilidad es la siguiente:

* Usar ``getNextSibling`` para ir recorriendo hermano a hermano hasta que se encuentre un ``null``
* Para evitar los nodos texto, solo imprimiremos cosas cuando el ``getNodeType()`` nos devuelva un tipo ``Node.ELEMENT_NODE``

.. code-block:: java

	public void imprimirHijos(Node nodoRaiz){
			if (nodoRaiz==null){
				System.out.println("Imposible procesar raiz null");
				return ;
			}
			Node nodo=nodoRaiz.getFirstChild();
			while (nodo!=null){
				short tipo=nodo.getNodeType();
				if (tipo==nodo.ELEMENT_NODE){
					System.out.println("Nodo hijo:"+nodo.getNodeName());
				}
				nodo=nodo.getNextSibling();				
			}
		}

Otra posibilidad sería usar el ``getChildNodes`` que nos devuelve un vector con todos los hijos. Sin embargo ocurrirá lo mismo, deberemos evitar el visitar nodos texto, solo nos interesan los nodos Elemento.


.. code-block:: java

	public void imprimirHijos2(Node nodoRaiz){
		if (nodoRaiz==null){
			System.out.println("Imposible procesar raíz nula");
			return;
		} //Fin del if null
		NodeList lista=nodoRaiz.getChildNodes();
		for (int i=0; i<lista.getLength();i++){
			Node nodo=lista.item(i);
			short tipo=nodo.getNodeType();
			if (tipo==Node.ELEMENT_NODE){
				System.out.println("Hijo:"+nodo.getNodeName());
			} //Fin del if
		} //Fin del for
	} //Fin del método

Ejercicio: extracción de información financiera
--------------------------------------------------

Dado el archivo XML siguiente...

.. code-block:: xml

  <listado>
          <futuro precio="11.28">
                  <producto>Cafe</producto>
                  <mercado>América Latina</mercado>
                  <ciudad_procedencia>
                          <frankfurt/>
                  </ciudad_procedencia>
          </futuro>
          <divisa precio="183">
                  <nombre_divisa>Libra esterlina</nombre_divisa>
                  <tipo_de_cambio>2.7:1 euros</tipo_de_cambio>
                  <tipo_de_cambio>1:0.87 dólares</tipo_de_cambio>
                  <ciudad_procedencia>
                          <madrid/>
                  </ciudad_procedencia>
          </divisa>
          <bono precio="10000" estable="si">
                  <pais_de_procedencia>
                          Islandia
                  </pais_de_procedencia>
                  <valor_deseado>9980</valor_deseado>
                  <valor_minimo>9950</valor_minimo>
                  <valor_maximo>10020</valor_maximo>
                  <ciudad_procedencia>
                          <tokio/>
                  </ciudad_procedencia>
          </bono>
          <letra precio="45020">
                  <tipo_de_interes>4.54%</tipo_de_interes>
                  <pais_emisor>
                          <espania/>
                  </pais_emisor>
                  <ciudad_procedencia>
                          <madrid/>
                  </ciudad_procedencia>
          </letra>
  </listado>

...crear un programa XML que:

* Busque todos los elementos cuya ciudad de procedencia sea "Madrid".
* Si el elemento es un futuro mostrará el contenido de la etiqueta "producto".
* Si el elemento es una divisa se mostrará el contenido de la etiqueta "nombre".
* Si el elemento es una letra  se mostrará el contenido de la etiqueta "pais_emisor".
* Si el elemento es un bono  se mostrará el contenido de la etiqueta "pais_de_procedencia".


Una posibilidad (incompleta) sería esta:

.. code-block:: java

  public class ProcesadorFinanzas {
    
    public static Element getRaiz (String rutaFichero){
  
      Element raiz=null;
      DocumentBuilderFactory fabrica;
      fabrica=DocumentBuilderFactory.newInstance();
      DocumentBuilder constructor;
      try {
        constructor=fabrica.newDocumentBuilder();
        FileInputStream fichero;
        fichero=new FileInputStream(rutaFichero);
        Document documento;
        documento=constructor.parse(fichero);
        raiz=documento.getDocumentElement();
      } catch (ParserConfigurationException e) {
        e.printStackTrace();
      } catch (FileNotFoundException e) {
        e.printStackTrace();
      } catch (SAXException e) {
        // TODO Auto-generated catch block
      } catch (IOException e) {
        e.printStackTrace();
      }
      return raiz;
    }
    public static void mostrarMadrid(Element raiz){
      NodeList hijos=raiz.getChildNodes();
      for (int i=0; i<hijos.getLength(); i++){
        Node nodoVisitado=hijos.item(i);
        if (nodoVisitado.getNodeType()
            == Node.ELEMENT_NODE) {
          //El nodo sí es un elemento y no
          //un nodo con texto \n
          Element elemVisitado;
          elemVisitado=(Element) nodoVisitado;
          if (elemVisitado.getTagName().equals("futuro")){
            procesarFuturo(elemVisitado);
          }
          if (elemVisitado.getTagName().equals("bono")){
            procesarBono(elemVisitado);
          }
          if (elemVisitado.getTagName().equals("letra")){
            procesarLetra(elemVisitado);
          }
          if (elemVisitado.getTagName().equals("divisa")){
            procesarDivisa(elemVisitado);
          }
        }
      }
    }
    private static void procesarDivisa(Element elemVisitado) {
      // TODO Auto-generated method stub
      
    }
    private static void procesarLetra(Element elemVisitado) {
      // TODO Auto-generated method stub
      
    }
    private static void procesarBono(Element elemVisitado) {
      // TODO Auto-generated method stub
      
    }
    private static void procesarFuturo(Element elemVisitado) {		
      NodeList hijosCiudad;
      hijosCiudad=elemVisitado.getElementsByTagName(
          "ciudad_procedencia");
      Node unicaCiudad=hijosCiudad.item(0);
      NodeList ciudades=unicaCiudad.getChildNodes();
      Node ciudadProcedencia=ciudades.item(1);
      Element elemCiudad=(Element) ciudadProcedencia;
      if (elemCiudad.getTagName().equals("madrid")){
        NodeList productos;
        productos=elemVisitado.getElementsByTagName(
            "producto");
        Element elemProducto;
        elemProducto=(Element) productos.item(0);
        System.out.println(
            elemProducto.getTextContent() );
        
      }
    }
    public static void main(String[] args) {
      Element raiz=getRaiz(
        "c:/users/ogomez/documents/finanzas.xml");
      mostrarMadrid(raiz);
    }
 }


		
Ejercicio
---------

Ampliar el programa para que nos diga cuantos elementos "divisa" hay en el archivo.

Para practicar esto y de paso practicar programación genérica, fabricaremos un método al que le pasaremos el nombre del elemento a buscar y el método nos dirá cuantos elementos con ese nombre hay.

.. code-block:: java

	public int contadorElementos(Node raiz,String nombreElemento){
		int contador=0;
		NodeList nodosHijo=raiz.getChildNodes();
		for (int i=0; i<nodosHijo.getLength();i++){
			Node nodo=nodosHijo.item(i);
			short tipo=nodo.getNodeType();
			if (tipo==Node.ELEMENT_NODE){
				String nombre=nodo.getNodeName();
				if (nombre==nombreElemento){
					contador++;
				} //Fin del if interno
			} //Fin del if externo
		} //Fin del for
		return contador;
	} //Fin del método
	
	
Ejercicio
----------------------------------------------

Nos interesa conocer el precio de todos los bonos. Crear un programa que ejecute esta tarea.


.. code-block:: java

	private void comprobarSiEsBono(Node n){
		String nombre=n.getNodeName();
		if (nombre=="bono"){
			System.out.println("Encontrado un bono");
		}
	}
	public void imprimirPrecioBonos(Node raiz){
		if (raiz==null){
			System.out.println("Imposible procesar null");
			return;
		}
		NodeList nodos=raiz.getChildNodes();
		for (int i=0; i<nodos.getLength(); i++){
			Node nodo=nodos.item(i);
			short tipo=nodo.getNodeType();
			if (tipo==Node.ELEMENT_NODE){
				this.comprobarSiEsBono(nodo);
			}
		}
	}



Ejercicio
----------------------------------------------

Crear un programa que nos diga cuantos productos financieros del listado no son estables. Es decir, que tengan el atributo estable y lo tengan a ``false``.


En su momento, en la DTD se permitió que el atributo ``estable`` fuera ``#IMPLIED``, es decir **optativo**. Al ser la DTD como un contrato, esto nos obliga a preparar nuestro código para manejar la posibilidad de que el atributo no esté presente.

.. code-block:: java

	public int cuantosInestables (Node raiz){
		int cuantos=0;
		NodeList lista=raiz.getChildNodes();
		for (int i=0; i<lista.getLength(); i++){
			Node n=lista.item(i);
			if (n.getNodeType()!=Node.ELEMENT_NODE) continue;
			Element e=(Element) lista.item(i);
			if (e.getNodeName()=="divisa" || 
					e.getNodeName()=="bono"){
				String atEstable=e.getAttribute("estable");
				if (atEstable!=null){
					System.out.println("Atributo:"+atEstable);
					if (atEstable.equals("no")){
						cuantos+=1;
					} //Fin del if interno
				} //Fin del if atEstable
			} //Fin de if nodo es divisa o bono
		} //Fin del for que recorre los nodos
		return cuantos;
	} //Fin del método cuantosInestables



	
Ejercicio
----------------------------------------------

Sumar los precios de todos los productos financieros.



.. code-block:: java

	public float sumarAtributosPrecio(Node raiz){
		float precioTotal=0;
		NodeList hijos=raiz.getChildNodes();
		for (int i=0; i<hijos.getLength(); i++){
			Node hijo=hijos.item(i);
			if (hijo.getNodeType()!=Node.ELEMENT_NODE) continue;
			Element e=(Element) hijo;
			String precio=e.getAttribute("precio");
			Float f=Float.parseFloat(precio);
			precioTotal+=f;
		}
		return precioTotal;
	} //Fin del método sumarAtributosPrecio


	
Ejercicio
----------------------------------------------

Contar cuantos productos financieros tienen algo que ver con el país "Islandia"

Se deben tener presentes varias cosas:

* Si no se tiene claro lo que nos piden, preguntar.
* En cualquier caso, si se tiene DTD, hay una buena pista.

	* Aparece un elemento llamado ``<pais_de_procedencia>``, que puede contener cualquier cosa (incluido Islandia)
	
	* La ciudad de procedencia no incluye la capital o ninguna ciudad de dicho país, así que podemos ignorar eso.
	
	* También aparece un elemento llamado ``<pais_emisor>``, pero tampoco incluye Islandia, en principio también podemos saltarlo.
	
Análisis del problema
~~~~~~~~~~~~~~~~~~~~~

Despues de haber examinado la DTD se llega a la conclusión de que el único elemento que puede transportar alguna clase de información relacionada con "Islandia" es el nodo ``país_de_procedencia``, que es un elemento hijo del elemento ``bono``.

Solución
~~~~~~~~

* La clase ``Element`` tiene un método llamado ``getElementsByTagName`` que nos permite recuperar de una sola vez todos los elementos con el nombre ``bono``.

* Se debe tener en cuenta que para llegar al elemento que nos interesa podemos seguir usando los métodos ``getFirstChild`` o ``getNextSibling`` para ir al primer hijo o para ir al siguiente hermano.

* El contenido textual de un nodo se puede extraer con ``getTextContent``

* Al procesar un contenido textual, podríamos encontrar muchos espacios en blanco, tabuladores u otros elementos que alteren las comparaciones entre cadenas, por lo que deberemos usar métodos como ``trim()`` que limpian los espacios en blanco.


.. code-block:: java


	public int algoQueVerCon(Node raiz, String nombrePais){
		int cuantos=0;
		Element elementoRaiz=(Element) raiz;
		NodeList lista=elementoRaiz.getElementsByTagName("bono");
		for (int i=0; i<lista.getLength(); i++){
			Node nodoBono=lista.item(i);
			Node primerHijoTexto=nodoBono.getFirstChild();
			Node segHijoPais=primerHijoTexto.getNextSibling();
			String paisExtraido=segHijoPais.getTextContent();
			//Limpiamos espacios
			paisExtraido=paisExtraido.trim();
			System.out.println("Pais extraido:"+paisExtraido);
			if (paisExtraido.equals(nombrePais)){
				cuantos++;
			}
		}
		return cuantos;
	}


Ejercicio
----------------------------------------------

Se desea crear un método que indique cuantos elementos tienen relación de alguna forma con "España".


Análisis
~~~~~~~~

* Se dispone del método anterior ``algoQueVerCon`` que nos permite contabilizar cuantos bonos tienen el país "España".

* Al analizar la DTD, se ha encontrado que la ciudad de procedencia de un elemento ``futuro`` puede ser Madrid.

* Al analizar la DTD también se ha encontrado que elemento ``pais_emisor`` de un elemento ``letra`` puede ser ``espania``

* Al analizar las divisas se debe comprobar si el elemento ``ciudad_procedencia`` es el elemento ``madrid``


Diseño
~~~~~~
Crearemos dos métodos extra, uno para calcular la solución para el segundo punto (ver cuantos elementos ``futuro`` tienen como ``ciudad_procedencia`` el valor Madrid y otro método para el tercer punto.


.. code-block:: java

	public int cuantosFuturosTienenCiudadProcedencia(
			Node raiz, String ciudad)
	{
		int cuantos=0;
		Element nodoRaiz=(Element) raiz;
		NodeList lista=nodoRaiz.getElementsByTagName("futuro");
		for (int i=0; i<lista.getLength(); i++){
			Element e=(Element)lista.item(i);
			NodeList listaHijos=e.getChildNodes();
			//El elemento ciudad procedencia es el quinto hijo
			Node nodoCiudad=listaHijos.item(5);
			NodeList hijosCiudad=nodoCiudad.getChildNodes();
			Node nodoElemCiudad=hijosCiudad.item(1);
			String nombreCiudad=nodoElemCiudad.getNodeName();
			if (nombreCiudad.equals(ciudad)){
				cuantos++;
			} //Fin del if
		} //Fin del for
		return cuantos;
	}

Para resolver el último punto nos bastaría un método como este:

.. code-block:: java

	public int letrasConPaisEmisor(Node raiz, String nombrePais){
		int cuantos=0;
		Element eRaiz=(Element) raiz;
		NodeList listaLetras=eRaiz.getElementsByTagName("letra");
		for (int i=0; i<listaLetras.getLength();i++){
			Node nodo=listaLetras.item(i);
			Element eNodo=(Element) nodo; //Devuelve elemento letra
			NodeList hijosLetra=eNodo.getChildNodes();
			Node nodoPaisEmisor=hijosLetra.item(3);
			NodeList hijosPais=nodoPaisEmisor.getChildNodes();
			Node nodoPais=hijosPais.item(1);
			String nombreNodoPais=nodoPais.getNodeName();
			if (nombreNodoPais.equals(nombrePais)){
				cuantos++;
			}
		} //Fin del for
		return cuantos;
	}

Ahora el método que resuelve este ejercicio es tan simple como esto:


.. code-block:: java

	public int algoQueVerConEspania(Node raiz){
		int cuantasLetras=this.letrasConPaisEmisor(raiz, "espania");
		int cuantosFuturos=this.cuantosFuturosTienenCiudadProcedencia(raiz, 
				"madrid");
		int cuantosBonos=this.algoQueVerCon(raiz, "España");
		return cuantasLetras+cuantosFuturos+cuantosBonos;
	}

	

Ejercicio
----------------------------------------------

Crear un programa que indique el país de procedencia de todos aquellos bonos en los que el precio deseado tenga un valor comprendido entre el precio mínimo y el máximo.


Una posible solución sería esta:

.. code-block:: java

	public void imprimirBonos(Node raiz){
		
		Element eRaiz=(Element) raiz;
		NodeList listaBonos=eRaiz.getElementsByTagName("bono");
		for (int i=0; i<listaBonos.getLength(); i++){
			Node bono=listaBonos.item(i);
			Element eBono=(Element) bono;
			// Element eBono=(Element) listaBonos.item(i);
			NodeList listaParaValorDeseado=
					eBono.getElementsByTagName("valor_deseado");
			NodeList listaParaValorMinimo=
					eBono.getElementsByTagName("valor_minimo");
			NodeList listaParaValorMaximo=
					eBono.getElementsByTagName("valor_maximo");
			Node nodoValorDeseado=listaParaValorDeseado.item(0);
			Node nodoValorMinimo=listaParaValorMinimo.item(0);
			Node nodoValorMaximo=listaParaValorMaximo.item(0);
			
			Element eValorDeseado=(Element) nodoValorDeseado;
			Element eValorMinimo=(Element) nodoValorMinimo;
			Element eValorMaximo=(Element) nodoValorMaximo;
			
			String cadValorDeseado=eValorDeseado.getTextContent();
			String cadValorMinimo=eValorMinimo.getTextContent();
			String cadValorMaximo=eValorMaximo.getTextContent();
			
			int valorDeseado=Integer.parseInt(cadValorDeseado);
			int valorMinimo=Integer.parseInt(cadValorMinimo);
			int valorMaximo=Integer.parseInt(cadValorMaximo);
			
			if ((valorDeseado>valorMinimo) &&
				(valorDeseado<valorMaximo) ){
				System.out.println("Encontrado un bono!");
			}
			//Element eValorDeseado=(Element) 
			//		listaParaValorDeseado.item(0);
			
		}
		
	}

Una solución mejor sería esta:

.. code-block:: java

	public int extraerHijoNumero (Element padre, 
			String nombreHijo){
		int valor=0;
		//Esta lista tiene solo un elemento
		NodeList listaHijos=
				padre.getElementsByTagName(nombreHijo);
		Element hijoNumerico=(Element) listaHijos.item(0);
		String contenidoTextual=hijoNumerico.getTextContent();
		valor=Integer.parseInt(contenidoTextual);
		return valor;
	}
	public void imprimirBonos(Node raiz){
		
		Element eRaiz=(Element) raiz;
		NodeList listaBonos=eRaiz.getElementsByTagName("bono");
		for (int i=0; i<listaBonos.getLength(); i++){
			Node bono=listaBonos.item(i);
			Element eBono=(Element) listaBonos.item(i);
			
			int valorDeseado=this.extraerHijoNumero(
					eBono, "valor_deseado");					
			int valorMinimo=this.extraerHijoNumero(
					eBono, "valor_minimo");
			int valorMaximo=this.extraerHijoNumero(
					eBono, "valor_maximo");
			
			if ((valorDeseado>valorMinimo) &&
				(valorDeseado<valorMaximo) ){
				System.out.println("Encontrado un bono!");
			}
			//Element eValorDeseado=(Element) 
			//		listaParaValorDeseado.item(0);
			
		}
		
	}





Ejercicio
----------------------------------------------
Imprimir, los productos financieros con la misma ciudad de procedencia.



Análisis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
En general, todos los problemas donde nos piden algo como *comprobar todos los elementos que tengan las mismas características* implican hacer una comprobación de *todos con todos*.

Diseño
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Todos los elementos tienen un elemento ``ciudad_de_procedencia``, por lo cual, probablemente sea útil crear algún pequeño método de utilidad que dado un elemento nos devuelva un string con la ciudad de procedencia.

Por otro lado, comparar *todos con todos* suele implicar un doble bucle, donde el primer irá extrayendo elementos y el otro irá extrayendo todos los demás.

Implementación
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

	public String getCiudadProcedencia(Element e){
		NodeList listaHijos=
				e.getElementsByTagName("ciudad_procedencia");
		Element eCiudad=(Element) listaHijos.item(0);
		NodeList listaHijosCiudad=eCiudad.getChildNodes();
		Element eCiudadConcreto=
				(Element) listaHijosCiudad.item(1);
		String nombre=eCiudadConcreto.getNodeName();
		return nombre;		
	}


.. code-block:: java

	public void imprimirMismaCiudad(Node raiz){
		NodeList hijos=raiz.getChildNodes();
		for (int i=0; i<hijos.getLength(); i++){
			Node hijo=hijos.item(i);
			if (hijo.getNodeType()!=Node.ELEMENT_NODE){
				continue;
			}
			for (int j=0; j<hijos.getLength(); j++){
				Node otroHijo=hijos.item(j);
				if (otroHijo.getNodeType()!=Node.ELEMENT_NODE){
					continue;
				}
				String ciudadHijo=
						this.getCiudadProcedencia((Element)hijo);
				String ciudadOtro=
						this.getCiudadProcedencia((Element)otroHijo);
				if (ciudadHijo.equals(ciudadOtro)){
					System.out.println(
							"Encontré dos elementos con la ciudad "+ciudadHijo);
				
				} //Fin del if ciudadHijo
			} //Fin del for interno
		} //Fin del for externo
	} //Fin del método

	public void imprimirMismaCiudad(Node raiz){
		NodeList hijos=raiz.getChildNodes();
		for (int i=0; i<hijos.getLength(); i++){
			Node hijo=hijos.item(i);
			if (hijo.getNodeType()!=Node.ELEMENT_NODE){
				continue;
			}
			String ciudadHijo=
					this.getCiudadProcedencia((Element)hijo);
			for (int j=i+1; j<hijos.getLength(); j++){
				Node otroHijo=hijos.item(j);
				if (otroHijo.getNodeType()!=Node.ELEMENT_NODE){
					continue;
				}
				
				String ciudadOtro=
						this.getCiudadProcedencia((Element)otroHijo);
				if (ciudadHijo.equals(ciudadOtro)){
					System.out.println(
							"Encontré dos elementos con la ciudad "+ciudadHijo);
				
				} //Fin del if ciudadHijo
			} //Fin del for interno
		} //Fin del for externo
	} //Fin del método	


Ejercicio
----------------------------------------------

Contar cuantos productos que no sean estables tienen como ciudad de procedencia Tokio. Si hay más de 2, devolver los precios en un vector y si no devolver un vector vacío.


Análisis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El atributo ``estable``, solo lo tienen los productos ``bono``. Ese atributo es optativo, puede que esté o puede que no. Si existe, debemos comprobar si tiene un "no".

Por otro lado, no sabemos a priori si habrá más de 2 o no.

* Podríamos hacer la cuenta, y si da más de 2 repetir operaciones y meter los bonos correctos en un vector.

* Podríamos ir haciendo las operaciones y a la vez las inserciones en un vector y ahorrarnos operaciones.


Optaremos por la segunda.


Diseño
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Aprovecharemos los métodos que nos permiten extraer el elemento raíz de un fichero.

* Necesitaremos crear vectores que tengan un cierto tamaño. Crearemos vectores muy grandes y los dejaremos con la inicialización que hace Java por defecto llenándolo con valores ``null``.

* Podemos aprovechar métodos ofrecidos por Java como ``getElementsByTagName``.

* Después recorreremos los elementos, comprobaremos si sus atributos cumplen las condiciones y si las cumplen almacenaremos en el vector a devolver la ciudad de ese bono.


* Nuestro método devolverá siempre algo como String[], ese vector puede que vaya lleno o no.



Solución 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: java

	public class ProcesadorXML {
		public Element getRaiz(String nombreFichero) 
				throws ParserConfigurationException, SAXException, IOException{
			DocumentBuilderFactory
				fabrica = DocumentBuilderFactory.newInstance();
			DocumentBuilder constructor=
					fabrica.newDocumentBuilder();
			FileInputStream fichero=
					new FileInputStream(nombreFichero);
			Document documento=
					constructor.parse(fichero);
			Element raiz=documento.getDocumentElement();
			return raiz;
		}
		public int[] getPreciosInestables() 
				throws ParserConfigurationException, SAXException, IOException{
			int[] vPrecios=null;
			int contador=0;
			Element raiz=
					getRaiz("d:/oscar/productos.xml");
			Element hijo=(Element) 
					raiz.getFirstChild();
			/* Mientras le queden hijos a la raíz...*/
			while (hijo!=null){
				String atrEstable=
						hijo.getAttribute("estable");
				if (atrEstable.equals("no")){
					NodeList vector=
							hijo.getElementsByTagName(
								"tokio");
					if (vector.getLength()>0){
						//El producto sí es de Tokio
						String precio=
								hijo.getAttribute(
										"precio");
						System.out.println("Precio:"+precio);
					}
				}
				Node finLinea=hijo.getNextSibling();
				hijo=(Element) 
						finLinea.getNextSibling();
			}
			return vPrecios;
		}
		
		public static void main(String[] args) 
				throws ParserConfigurationException, SAXException, IOException {
			ProcesadorXML procesador=
					new ProcesadorXML();
			int[] precios=
					procesador.getPreciosInestables();
		}
	}
	


Solución 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

	public String[] obtenerListaBonos(Node raiz){
		int tamanioMaximo=1000;
		String[] ciudades=new String[tamanioMaximo];
		String[] aux=new String[tamanioMaximo];
		int posPrecio=0;
		Element eRaiz=(Element) raiz;
		NodeList listaBonos=eRaiz.getElementsByTagName("bono");
		for (int i=0; i<listaBonos.getLength(); i++){
			Element bono=(Element) listaBonos.item(i);
			String atEstable=bono.getAttribute("estable");
			if (atEstable!=null){
				if (atEstable.equals("no")){
					//Examinamos la ciudad aprovechando
					//un método ya construido.
					String ciudad=this.getCiudadProcedencia(bono);
					if (ciudad.equals("tokio")){
						//Si es de tokio, copiamos el precio
						String precio=bono.getAttribute("precio");
						aux[posPrecio]=precio;
						posPrecio++;
					} //Fin del if para tokio
				} //Fin del if para el "no"
			} //Fin del if para atEstable
		} //Fin del for que recorre los bonos
		if (posPrecio>2){
			return aux;
		}
		return ciudades;
	}

	
Anexo
===========================================

Código Java
----------------------------------------------

A continuación se muestra el código Java completo:

.. code-block:: java

	package com.ies;
	import javax.xml.parsers.*;
	import javax.xml.transform.Transformer;
	import javax.xml.transform.TransformerFactory;
	import javax.xml.transform.dom.DOMSource;
	import javax.xml.transform.stream.StreamResult;

	import java.io.File;

	import org.w3c.dom.*;



	public class ProcesadorXML {
		public Node extraerRaiz(String nombreArchivo){
			DocumentBuilderFactory fabrica;
			DocumentBuilder constructor;
			Document documentoXML=null;
			File fichero=new File(nombreArchivo);
			fabrica= 
				DocumentBuilderFactory.newInstance();
			System.out.println("Procesando "+nombreArchivo);
			try {
				constructor=
				  fabrica.newDocumentBuilder();
				documentoXML=constructor.parse(fichero);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return documentoXML.getDocumentElement();
			
		}
		public void imprimirNombreDeLaRaiz(Node nodo){
			if (nodo!=null){
				String nombre=nodo.getNodeName();
				System.out.println("La raíz se llama:"+nombre);
				Node primerHijo=nodo.getFirstChild();
				String nombreHijo=primerHijo.getNodeName();
				System.out.println("El primer hijo se llama <"+nombreHijo+">");
			} else {
				System.out.println("No se pudo leer la raíz por ser nula");
			}
		}
		public void imprimirHijos(Node nodoRaiz){
			if (nodoRaiz==null){
				System.out.println("Imposible procesar raiz null");
				return ;
			}
			Node nodo=nodoRaiz.getFirstChild();
			while (nodo!=null){
				short tipo=nodo.getNodeType();
				if (tipo==nodo.ELEMENT_NODE){
					System.out.println("Nodo hijo:"+nodo.getNodeName());
				}
				nodo=nodo.getNextSibling();	
			}
		}
		
		public void imprimirHijos2(Node nodoRaiz){
			if (nodoRaiz==null){
				System.out.println("Imposible procesar raíz nula");
				return;
			} //Fin del if null
			NodeList lista=nodoRaiz.getChildNodes();
			for (int i=0; i<lista.getLength();i++){
				Node nodo=lista.item(i);
				short tipo=nodo.getNodeType();
				if (tipo==Node.ELEMENT_NODE){
					System.out.println("Hijo:"+nodo.getNodeName());
				} //Fin del if
			} //Fin del for
		} //Fin del método
		
		public int contadorElementos(Node raiz,String nombreElemento){
			int contador=0;
			NodeList nodosHijo=raiz.getChildNodes();
			for (int i=0; i<nodosHijo.getLength();i++){
				Node nodo=nodosHijo.item(i);
				short tipo=nodo.getNodeType();
				if (tipo==Node.ELEMENT_NODE){
					String nombre=nodo.getNodeName();
					if (nombre==nombreElemento){
						contador++;
					} //Fin del if interno
				} //Fin del if externo
			} //Fin del for
			return contador;
		} //Fin del método
		private void comprobarSiEsBono(Node n){
			String nombre=n.getNodeName();
			if (nombre=="bono"){
				Element e=(Element) n;
				String precio=e.getAttribute("precio");
				System.out.println("Precio:"+precio);
			}
		}
		
		public int cuantosInestables (Node raiz){
			int cuantos=0;
			NodeList lista=raiz.getChildNodes();
			for (int i=0; i<lista.getLength(); i++){
				Node n=lista.item(i);
				if (n.getNodeType()!=Node.ELEMENT_NODE) continue;
				Element e=(Element) lista.item(i);
				if (e.getNodeName()=="divisa" || 
						e.getNodeName()=="bono"){
					String atEstable=e.getAttribute("estable");
					if (atEstable!=null){
						System.out.println("Atributo:"+atEstable);
						if (atEstable.equals("no")){
							cuantos+=1;
						} //Fin del if interno
					} //Fin del if atEstable
				} //Fin de if nodo es divisa o bono
			} //Fin del for que recorre los nodos
			return cuantos;
		} //Fin del método cuantosInestables
		
		public float sumarAtributosPrecio(Node raiz){
			float precioTotal=0;
			NodeList hijos=raiz.getChildNodes();
			for (int i=0; i<hijos.getLength(); i++){
				Node hijo=hijos.item(i);
				if (hijo.getNodeType()!=Node.ELEMENT_NODE) continue;
				Element e=(Element) hijo;
				String precio=e.getAttribute("precio");
				Float f=Float.parseFloat(precio);
				precioTotal+=f;
			}
			return precioTotal;
		} //Fin del método sumarAtributosPrecio
		public void imprimirPrecioBonos(Node raiz){
			if (raiz==null){
				System.out.println("Imposible procesar null");
				return;
			}
			NodeList nodos=raiz.getChildNodes();
			for (int i=0; i<nodos.getLength(); i++){
				Node nodo=nodos.item(i);
				short tipo=nodo.getNodeType();
				if (tipo==Node.ELEMENT_NODE){
					this.comprobarSiEsBono(nodo);
				}
			}
		}
		/**
		 * 
		 * @param raiz 
		 * @param nombrePais
		 * @return Numero de elementos dentro del nodo en
		 * los cuales aparece de alguna forma el país
		 */
		public int algoQueVerCon(Node raiz, String nombrePais){
			int cuantos=0;
			Element elementoRaiz=(Element) raiz;
			NodeList lista=elementoRaiz.getElementsByTagName("bono");
			for (int i=0; i<lista.getLength(); i++){
				Node nodoBono=lista.item(i);
				Node primerHijoTexto=nodoBono.getFirstChild();
				Node segHijoPais=primerHijoTexto.getNextSibling();
				String paisExtraido=segHijoPais.getTextContent();
				//Limpiamos espacios
				paisExtraido=paisExtraido.trim();
				System.out.println("Pais extraido:"+paisExtraido);
				if (paisExtraido.equals(nombrePais)){
					cuantos++;
				}
			}
			return cuantos;
		}
		
		/**
		 * Este método averigua cuantos elementos futuro
		 * tienen una cierta ciudad procedencia
		 * @param argumentos
		 */
		public int cuantosFuturosTienenCiudadProcedencia(
				Node raiz, String ciudad
				)
		{
			int cuantos=0;
			Element nodoRaiz=(Element) raiz;
			NodeList lista=nodoRaiz.getElementsByTagName("futuro");
			for (int i=0; i<lista.getLength(); i++){
				Element e=(Element)lista.item(i);
				NodeList listaHijos=e.getChildNodes();
				//El elemento ciudad procedencia es el quinto hijo
				Node nodoCiudad=listaHijos.item(5);
				NodeList hijosCiudad=nodoCiudad.getChildNodes();
				Node nodoElemCiudad=hijosCiudad.item(1);
				String nombreCiudad=nodoElemCiudad.getNodeName();
				if (nombreCiudad.equals(ciudad)){
					cuantos++;
				} //Fin del if
			} //Fin del for
			return cuantos;
		}
		/**
		 * 
		 * @param raiz Raíz del documento
		 * @param nombrePais (Debe ser "espania" para España)
		 * @return
		 */
		public int letrasConPaisEmisor(Node raiz, String nombrePais){
			int cuantos=0;
			Element eRaiz=(Element) raiz;
			NodeList listaLetras=eRaiz.getElementsByTagName("letra");
			for (int i=0; i<listaLetras.getLength();i++){
				Node nodo=listaLetras.item(i);
				Element eNodo=(Element) nodo; //Devuelve elemento letra
				NodeList hijosLetra=eNodo.getChildNodes();
				Node nodoPaisEmisor=hijosLetra.item(3);
				NodeList hijosPais=nodoPaisEmisor.getChildNodes();
				Node nodoPais=hijosPais.item(1);
				String nombreNodoPais=nodoPais.getNodeName();
				if (nombreNodoPais.equals(nombrePais)){
					cuantos++;
				}
			} //Fin del for
			return cuantos;
		}
		
		public int algoQueVerConEspania(Node raiz){
			int cuantasLetras=this.letrasConPaisEmisor(raiz, "espania");
			int cuantosFuturos=this.cuantosFuturosTienenCiudadProcedencia(raiz, 
					"madrid");
			int cuantosBonos=this.algoQueVerCon(raiz, "España");
			return cuantasLetras+cuantosFuturos+cuantosBonos;
		}
		public int extraerHijoNumero (Element padre, 
				String nombreHijo){
			int valor=0;
			//Esta lista tiene solo un elemento
			NodeList listaHijos=
					padre.getElementsByTagName(nombreHijo);
			Element hijoNumerico=(Element) listaHijos.item(0);
			String contenidoTextual=hijoNumerico.getTextContent();
			valor=Integer.parseInt(contenidoTextual);
			return valor;
		}
		public void imprimirBonos(Node raiz){
			
			Element eRaiz=(Element) raiz;
			NodeList listaBonos=eRaiz.getElementsByTagName("bono");
			for (int i=0; i<listaBonos.getLength(); i++){
				Node bono=listaBonos.item(i);
				Element eBono=(Element) listaBonos.item(i);
				
				int valorDeseado=this.extraerHijoNumero(
						eBono, "valor_deseado");					
				int valorMinimo=this.extraerHijoNumero(
						eBono, "valor_minimo");
				int valorMaximo=this.extraerHijoNumero(
						eBono, "valor_maximo");
				
				if ((valorDeseado>valorMinimo) &&
					(valorDeseado<valorMaximo) ){
					System.out.println("Encontrado un bono!");
					String ciudad=this.getCiudadProcedencia(eBono);
					System.out.println("Su ciudad era:"+ciudad);
				}
				//Element eValorDeseado=(Element) 
				//		listaParaValorDeseado.item(0);
				
			}
			
		}
		public String getCiudadProcedencia(Element e){
			NodeList listaHijos=
					e.getElementsByTagName("ciudad_procedencia");
			Element eCiudad=(Element) listaHijos.item(0);
			NodeList listaHijosCiudad=eCiudad.getChildNodes();
			Element eCiudadConcreto=
					(Element) listaHijosCiudad.item(1);
			String nombre=eCiudadConcreto.getNodeName();
			return nombre;		
		}
		
		public void imprimirMismaCiudad(Node raiz){
			NodeList hijos=raiz.getChildNodes();
			for (int i=0; i<hijos.getLength(); i++){
				Node hijo=hijos.item(i);
				if (hijo.getNodeType()!=Node.ELEMENT_NODE){
					continue;
				}
				String ciudadHijo=
						this.getCiudadProcedencia((Element)hijo);
				for (int j=i+1; j<hijos.getLength(); j++){
					Node otroHijo=hijos.item(j);
					if (otroHijo.getNodeType()!=Node.ELEMENT_NODE){
						continue;
					}
					
					String ciudadOtro=
							this.getCiudadProcedencia((Element)otroHijo);
					if (ciudadHijo.equals(ciudadOtro)){
						System.out.println(
								"Encontré dos elementos con la ciudad "+ciudadHijo);
					
					} //Fin del if ciudadHijo
				} //Fin del for interno
			} //Fin del for externo
		} //Fin del método
		
		public String[] obtenerListaBonos(Node raiz){
			int tamanioMaximo=1000;
			String[] ciudades=new String[tamanioMaximo];
			String[] aux=new String[tamanioMaximo];
			int posPrecio=0;
			Element eRaiz=(Element) raiz;
			NodeList listaBonos=eRaiz.getElementsByTagName("bono");
			for (int i=0; i<listaBonos.getLength(); i++){
				Element bono=(Element) listaBonos.item(i);
				String atEstable=bono.getAttribute("estable");
				if (atEstable!=null){
					if (atEstable.equals("no")){
						//Examinamos la ciudad aprovechando
						//un método ya construido.
						String ciudad=this.getCiudadProcedencia(bono);
						if (ciudad.equals("tokio")){
							//Si es de tokio, copiamos el precio
							String precio=bono.getAttribute("precio");
							aux[posPrecio]=precio;
							posPrecio++;
						} //Fin del if para tokio
					} //Fin del if para el "no"
				} //Fin del if para atEstable
			} //Fin del for que recorre los bonos
			if (posPrecio>2){
				return aux;
			}
			return ciudades;
		}
		
		public void crearElemento(Document d,
				String nombre,String contenido){
			Element e=d.createElement(nombre);
			e.setTextContent(contenido);
		}
		
		public void crearRSS(){
			DocumentBuilderFactory fabrica;
			DocumentBuilder constructor;
			Document documentoXML;
			try{
				fabrica= 
						DocumentBuilderFactory.newInstance();
				constructor=fabrica.newDocumentBuilder();
				documentoXML=constructor.newDocument();
				TransformerFactory fabricaConv = 
						TransformerFactory.newInstance();
				Transformer transformador = 
						fabricaConv.newTransformer();
				DOMSource origenDOM = 
						new DOMSource(documentoXML);
				Element e=documentoXML.createElement("rss");
				documentoXML.appendChild(e);
				StreamResult resultado= 
						new StreamResult(
								new File("D:\\oscar\\archivo.rss"));
				transformador.transform(origenDOM, resultado);
			}
			catch (Exception e){
				System.out.print("No se han podido crear los");
				System.out.println(" objetos necesarios.");
				e.printStackTrace();
				return ;
			}		
		}
		
		public static void main (String[] argumentos){
			System.out.println("Probando...");
			ProcesadorXML proc=new ProcesadorXML();
			Node nodoRaiz=proc.extraerRaiz("bolsas.xml");
	//		proc.imprimirNombreDeLaRaiz(nodoRaiz);
	//		proc.imprimirHijos(nodoRaiz);
	//		proc.imprimirHijos2(nodoRaiz);
	//		int cuantosFuturos=proc.contadorElementos(nodoRaiz, "futuro");
	//		System.out.println("Hay "+cuantosFuturos);
	//		proc.imprimirPrecioBonos(nodoRaiz);
	//		int inestables=proc.cuantosInestables(nodoRaiz);
	//		System.out.println("Inestables hay:"+inestables);
	//		float preciosTotales=proc.sumarAtributosPrecio(nodoRaiz);
	//		System.out.println("La suma total es:"+preciosTotales);
			int cuantos=proc.algoQueVerCon(nodoRaiz, "Islandia");
	//		System.out.println("Num paises Islandia:"+cuantos);
	//		cuantos=proc.cuantosFuturosTienenCiudadProcedencia(
	//				nodoRaiz, "madrid");
	//		System.out.println("Futuros de Madrid:"+cuantos);
	//		cuantos=proc.letrasConPaisEmisor(nodoRaiz, "espania");
	//		System.out.println("Letras con espania:"+cuantos);
			cuantos=proc.algoQueVerConEspania(nodoRaiz);
			//System.out.println("Productos rel. con España:"+cuantos);
			//proc.imprimirBonos(nodoRaiz);
			proc.imprimirMismaCiudad(nodoRaiz);
			String[] resultados=proc.obtenerListaBonos(nodoRaiz);
			System.out.println("La ciudad 0 es:"+resultados[0]);
			proc.crearRSS();
		}
	}


Archivo XML
----------------------------------------------

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE listado [
		<!ELEMENT listado (futuro+, divisa+, bono+, letra+)>
		<!ATTLIST futuro precio CDATA #REQUIRED>
		<!ATTLIST divisa precio CDATA #REQUIRED>
		<!ATTLIST bono precio CDATA #REQUIRED>
		<!ATTLIST letra precio CDATA #REQUIRED>
		<!ELEMENT ciudad_procedencia (madrid|nyork|frankfurt|tokio)>
		<!ELEMENT madrid EMPTY>
		<!ELEMENT nyork EMPTY>
		<!ELEMENT frankfurt EMPTY>
		<!ELEMENT tokio EMPTY>
		<!ATTLIST divisa estable CDATA #IMPLIED>
		<!ATTLIST bono estable CDATA #IMPLIED>
		<!ELEMENT futuro (producto, mercado?, ciudad_procedencia)>
		<!ELEMENT producto (#PCDATA)>
		<!ELEMENT mercado (#PCDATA)>
		<!ELEMENT bono (pais_de_procedencia,valor_deseado,
				valor_minimo, valor_maximo, ciudad_procedencia)>
		<!ELEMENT valor_deseado (#PCDATA)>
		<!ELEMENT valor_minimo (#PCDATA)>
		<!ELEMENT valor_maximo (#PCDATA)>
		<!ELEMENT pais_de_procedencia (#PCDATA)>
		<!ELEMENT divisa (nombre_divisa, 
				tipo_de_cambio+, ciudad_procedencia)>
		<!ELEMENT nombre_divisa (#PCDATA)>
		<!ELEMENT tipo_de_cambio (#PCDATA)>
		<!ELEMENT letra (tipo_de_interes, pais_emisor,ciudad_procedencia)>
		<!ELEMENT tipo_de_interes (#PCDATA)>
		<!ELEMENT pais_emisor (espania|eeuu|alemania|japon)>
		<!ELEMENT espania     EMPTY>
		<!ELEMENT eeuu        EMPTY>
		<!ELEMENT alemania    EMPTY>
		<!ELEMENT japon       EMPTY>
	]>


	<listado><futuro precio="11.28">
			<producto>Cafe</producto>
			<mercado>América Latina</mercado>
			<ciudad_procedencia>
				<madrid/>
			</ciudad_procedencia>
		</futuro>
		<divisa precio="183">
			<nombre_divisa>Libra esterlina</nombre_divisa>
			<tipo_de_cambio>2.7:1 euros</tipo_de_cambio>
			<tipo_de_cambio>1:0.87 dólares</tipo_de_cambio>
			<ciudad_procedencia>
				<madrid/>
			</ciudad_procedencia>
		</divisa>
		<bono precio="100" estable="si">
			<pais_de_procedencia>
				España
			</pais_de_procedencia>
			<valor_deseado>9980</valor_deseado>
			<valor_minimo>9950</valor_minimo>
			<valor_maximo>10020</valor_maximo>
			<ciudad_procedencia>
				<tokio/>
			</ciudad_procedencia>
		</bono>
		<bono precio="10000" estable="si">
			<pais_de_procedencia>
				España
			</pais_de_procedencia>
			<valor_deseado>9980</valor_deseado>
			<valor_minimo>9950</valor_minimo>
			<valor_maximo>10020</valor_maximo>
			<ciudad_procedencia>
				<tokio/>
			</ciudad_procedencia>
		</bono>
		<bono precio="10000" estable="no">
			<pais_de_procedencia>
				España
			</pais_de_procedencia>
			<valor_deseado>9980</valor_deseado>
			<valor_minimo>9950</valor_minimo>
			<valor_maximo>10020</valor_maximo>
			<ciudad_procedencia>
				<tokio/>
			</ciudad_procedencia>
		</bono>
		<bono precio="10000" estable="no">
			<pais_de_procedencia>
				España
			</pais_de_procedencia>
			<valor_deseado>9980</valor_deseado>
			<valor_minimo>9950</valor_minimo>
			<valor_maximo>10020</valor_maximo>
			<ciudad_procedencia>
				<tokio/>
			</ciudad_procedencia>
		</bono>
		<letra precio="45020">
			<tipo_de_interes>4.54%</tipo_de_interes>
			<pais_emisor>
				<espania/>
			</pais_emisor>
			<ciudad_procedencia>
				<madrid/>
			</ciudad_procedencia>
		</letra>
	</listado>
  
  
Procesamiento con SAX
==============================

Simple Api for XML (o SAX) es un conjunto de clases para procesar XML de una forma muchísimo más eficiente (pero también más incómoda). Consiste en un *parser* que va leyendo etiqueta por etiqueta. Cada vez que el parser encuentra una etiqueta nueva nos lo comunicará mediante un evento y tendremos que incluir código de gestión de eventos que decidan que hacer.

La forma más sencilla de trabajar es hacer que nuestra clase herede de ``DefaultHandler`` y sobrecargar el código de los métodos ``startElement`` y ``endElement``.

Cuando se procesa XML podemos encontrarnos con que se usen o no espacios de nombres. Si usamos espacios de nombres SAX nos devolverá un argumento pero si no los usamos SAX nos devolverá otro argumento. Observemos el siguiente código:

.. code-block:: java

  public class ProcesadorSAX extends DefaultHandler{
  
    @Override
    public void startElement(
        String ns, String nombreCuandoHayNS, 
        String nombreCuandoNoHayNS, 
        Attributes atributos) 
        throws SAXException 
    {
      System.out.println(nombreCuandoNoHayNS);
    }
  }


En este código SAX avisará a nuestro método ``startElement`` (el nombre debe ser así), cada vez que
encuentre una etiqueta. Como en nuestros documentos no estamos usando espacios de nombres nos interesa imprimir el tercer parámetro.

Para hacer que Java procese un fichero mediante SAX usando nuestra clase como procesador de etiquetas haremos lo siguiente:

.. code-block:: java

  public class ProcesadorSAX extends DefaultHandler{
  
    @Override
    public void startElement(
        String ns, String nombreCuandoHayNS, 
        String nombreCuandoNoHayNS, 
        Attributes atributos) 
        throws SAXException 
    {
      System.out.println(nombreCuandoNoHayNS);
    }
    
    public static void main(String[] args) 
        throws ParserConfigurationException, 
        SAXException, IOException {
      
      SAXParserFactory fabrica;
      fabrica=SAXParserFactory.newInstance();
      SAXParser parser=fabrica.newSAXParser();
      XMLReader lector=parser.getXMLReader();
      lector.setContentHandler(new ProcesadorSAX());
      lector.parse(
        "c:/users/ogomez/documents/finanzas.xml");
    }
  }

Ahora Java irá leyendo el fichero etiqueta por etiqueta y mostrándonos los nombres de todas. No importará que el fichero ocupe varios GB, ya que SAX no cargará el fichero completo en memoria.

Ejercicio: encontrar producto
----------------------------------

Encontrar todos los productos cuyo nombre sea "Cafe" y su mercado "América Latina".

.. code-block:: java

  public void characters(
        char[] letras, int ini, int longitud){
      if ((mercadoEncontrado) && (cafeEncontrado)){
        String cadena=new String(letras, ini, longitud);
        if (cadena.equals("América Latina")){
          System.out.println("Encontrado Cafe de AL");
          cafeEncontrado=false;
          mercadoEncontrado=false;
          productoEncontrado=false;
          futuroEncontrado=false;
        }
      }
      if ((productoEncontrado) && (futuroEncontrado)){
        String cadena=new String(letras, ini, longitud);
        if (cadena.equals("Cafe")){
          cafeEncontrado=true;
        } //Fin del if interno
      } //Fin del if externo
    } //Fin del método characters
    
Ejercicio: precios
-----------------------

Encontrar todos las divisas cuya ciudad de procedencia sea "Madrid".


Ejercicios para preparar examen
===========================================	

1. Indicar cuantas letras tienen un tipo de interés inferior al 3% e indicar para cada una de ellas el país emisor.

2. Comprobar si hay alguna divisa con nombre "Euro" cuyo precio sea mayor de 195.

3. Indicar todos los productos que tengan la misma ciudad de procedencia.