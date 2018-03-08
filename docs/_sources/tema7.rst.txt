===========================================
Sindicación y transformación de contenidos
===========================================

Introducción
===========================================

Muchas páginas web disponen de "feeds". Un "feed" es un mecanismo de suscripción que facilita la recepción de información.

En general, los feed utilizan un vocabulario XML llamado RSS o uno llamado Atom.

RSS
===========================================

RSS es un estándar para la "sindicación" o "agregación" de recursos (recursos web normalmente).

Su objetivo principal era permitir a un sitio web publicar las novedades con facilidad y que el usuario puede ir derectamente al lugar que le interese.

Formato de archivo RSS
----------------------------------------------

Todo archivo RSS es, por supuesto, un XML

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<rss version="2.0">
		<channel>
			<title>
				Canal de noticias de SSOO de DAM
			</title>
			<link>
				http://ssoo.iesmaestredecalatrava.es
			</link>
			<description>
				En este canal...
			</description>
			<item>
				<title>Nueva versión de Ubuntu</title>
				<link>http://ubuntu.org</link>
				<description>
					Nueva versión...
				</description>
			</item>
		</channel>
		<channel>
			<title>
				Canal de Lenguajes de marcas
			</title>
			<link>
				http://xml.iesmaestredecalatrava.es
			</link>
			<description>
				En este canal...
			</description>
			<item>
				<title>Publicado nuevo validador del W3C</title>
				<link>http://validator.w3c.org</link>
				<description>
					Hay nuevo validador...
				</description>
			</item>
		</channel>
	</rss>
	
Las reglas serían las siguientes:

* Todo archivo de descripción de recursos en RSS utiliza el preámbulo típico de los documentos xml

.. code-block:: xml
	
	<?xml version="1.0" encoding="UTF-8"?>

* Todo RSS tiene un solo elemento raíz en el cual se puede indicar la versión RSS a la que nos ceñimos

.. code-block:: xml

	<rss version="2.0">
    
* Un RSS tiene uno o más canales

.. code-block:: xml

	<channel>
	</channel>
	
* Todo canal debe tener, al menos un título, un enlace base (la dirección del propio sitio web) y una descripción:

.. code-block:: xml

	<channel>
		<title>
		</title>
		<link>
		</link>
		<description>	
		</description>
		<item>
			...
		</item>
		<item>
			...
		</item>
	</channel>
	
Resumiendo los puntos más importantes:

1. Usar como elemento raíz ``rss``.
2. Todo RSS tiene uno o más ``channel``
3. Todo ``channel`` tiene al menos ``title``, ``link`` y ``description``
4. Despues de estos elementos, un ``channel`` puede tener uno o más elementos ``item`` (que son los que contienen las noticias)
5. Todo ``item`` también debe tener un ``title``, un ``link`` y ``description``
	

Ejercicio
----------------------------------------------

Crear un fichero Java que construya el siguiente fichero XML:

.. code-block:: xml

	<?xml version="1.0"?>
	<rss version="2.0">
		<channel>
			<title>Prueba</title>
			<link>http://www.google.es</link>
			<description>Prueba de descripcion</description>
		</channel>
	</rss>

Una posible solución es esta:

.. code-block:: java

	public class CreadorRSS {
		public byte[] getEtiquetas(
				String titulo, 
				String enlace,
				String descripcion)
		{
			String resultado="";
			resultado+="<title>";
			resultado+=titulo;
			resultado+="</title>\n";
			resultado+="<link>";
			resultado+=enlace;
			resultado+="</link>\n";
			resultado+="<description>";
			resultado+=descripcion;
			resultado+="</description>";
			return resultado.getBytes();
		}
		public void crearArchivo(String nombre) 
				throws IOException{
			FileOutputStream fos=
					new FileOutputStream(nombre);
			String cabecera="<?xml version='1.0'?>\n";
			fos.write(cabecera.getBytes());
			String rss="<rss version='1.0'>\n";
			fos.write(rss.getBytes());
			byte[] etiquetas=this.getEtiquetas(
					"Titulo de la noticia",
					"http://www.algo.com",
					"Noticia muy importante");
			fos.write(etiquetas);
			String rssCierre="</rss>";
			fos.write(rssCierre.getBytes());
			fos.close();
		}

		public static void main(String[] args) 
				throws IOException {
			CreadorRSS creador=new CreadorRSS();
			creador.crearArchivo("D:/oscar/archivo.rss");
		}
	}
		

El siguiente código Java ilustra otra forma de hacerlo:

.. code-block:: java

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
						new File("D:\\resul\\archivo.rss"));
			transformador.transform(origenDOM, resultado);
		}
		catch (Exception e){
			System.out.print("No se han podido crear los");
			System.out.println(" objetos necesarios.");
			e.printStackTrace();
			return ;
		}		
	}


XPath
===================================
Según el W3C, XPath (que ya va por su versión 3.0) es un lenguaje diseñado para acceder a las distintas partes de un archivo XML. En nuestro caso nos va a resultar de mucha utilidad combinado con XSLT, que se verá un poco despues. 

XPath se basa en expresiones. Así, dado un archivo XML y una expresión XPath se dice que la expresión "se evalúa" y se obtiene un resultado que puede ser:

* Una lista de nodos.
* Un ``boolean`` (true o false)
* Un ``float``.
* Una cadena.

XPath también ofrece algunas funciones de utilidad que se asemejan a las de algunos lenguajes de programación.

Acceso a elementos
---------------------

El mecanismo de acceso en XPath es muy similar al acceso a directorios que ofrecen algunos sistemas operativos. Para los ejemplos siguientes se usará el siguiente archivo XML

.. code-block:: xml

    <inventario>
        <producto codigo="AAA-111">
            <nombre>Teclado</nombre>
            <peso unidad="g">480</peso>
        </producto>
        <producto codigo="ACD-981">
            <nombre>Monitor</nombre>
            <peso unidad="kg">1.8</peso>
        </producto>
        <producto codigo="DEZ-138">
            <nombre>Raton</nombre>
            <peso unidad="g">50</peso>
        </producto>
    </inventario>

Así dado este archivo tenemos las expresiones siguientes:

Si usamos la expresión ``/inventario`` se selecciona *el nodo inventario que cuelga de la raíz*. Como puede verse la raíz en XPath es un elemento conceptual, no existe como elemento. Además, dado como es XML solo puede haber un elemento en la raíz. Así, el resultado de evaluar la expresión ``/inventario`` para el archivo de ejemplo produce el resultado siguiente:

.. code-block:: xml

    <inventario>
        <producto codigo="AAA-111">
            <nombre>Teclado</nombre>
            <peso unidad="g">480</peso>
        </producto>
        <producto codigo="ACD-981">
            <nombre>Monitor</nombre>
            <peso unidad="kg">1.8</peso>
        </producto>
        <producto codigo="DEZ-138">
            <nombre>Raton</nombre>
            <peso unidad="g">50</peso>
        </producto>
    </inventario>

Como puede verse, obtenemos el propio archivo original. Sin embargo, podemos movernos a través del árbol XML de forma similar a un árbol de directorios. Y obsérvese que decimos "similar". Observemos por ejemplo que dentro de ``<inventario>`` hay 3 elementos ``<producto>``. Si pensamos en la expresión XPath ``/inventario/producto`` puede que pensemos que obtendremos el primer producto (el que tiene el código AAA-111), sin embargo **una expresión XPath se parece a una consulta SQL**, y lo que obtiene la expresión es "todo elemento ``<producto>`` que sea hijo de ``<inventario>``. Es decir, el fichero siguiente (que no es XML, sino una lista de nodos):


.. code-block:: xml

    <producto codigo="AAA-111">
        <nombre>Teclado</nombre>
        <peso unidad="g">480</peso>
    </producto>
    

    <producto codigo="ACD-981">
        <nombre>Monitor</nombre>
        <peso unidad="kg">1.8</peso>
    </producto>
    

    <producto codigo="DEZ-138">
        <nombre>Raton</nombre>
        <peso unidad="g">50</peso>
    </producto>

En cualquier lista podemos acceder a sus elementos como si fuese un vector. Sin embargo en XPath **los vectores empiezan por 1**. Por lo cual la expresión ``/inventario/producto[1]`` produce este resultado:

.. code-block:: xml

    <producto codigo="AAA-111">
        <nombre>Teclado</nombre>
        <peso unidad="g">480</peso>
    </producto>
    
Y la expresión ``/inventario/producto[3]`` produce este:

.. code-block:: xml

    <producto codigo="DEZ-138">
        <nombre>Raton</nombre>
        <peso unidad="g">50</peso>
    </producto>


Obsérvese que no existe el elemento 4 y que por tanto la expresión ``/inventario/producto[4]`` producirá un error. Otro aspecto relevante es que no deben confundirse los vectores con las condiciones (que el W3C llama "predicados"), y con las cuales podremos seleccionar nodos que cumplan ciertas condiciones De hecho, una buena forma de verlos es asumir que en los corchetes **siempre se ponen condiciones y que si hay un número como por ejemplo el 2 nos referimos a la condicion "extraer el elemento cuya posición es igual a 2**.

Dado un elemento, también podemos extraer un cierto atributo usando la arroba @. Así, la expresión ``/inventario/producto[3]/@codigo`` devuelve como resultado ``ACD-981``, que es el atributo código del tercer elemento ``producto`` que está dentro de ``inventario`` el cual cuelga de la raíz.



Supongamos que deseamos extraer el producto cuyo código sea "AAA-111". Si usamos ``/inventario/producto`` extraemos todos los elementos producto hijos de inventario, pero recordemos que entre corchetes podemos poner condiciones. Dado que queremos comprobar si @codigo = "AAA-111", la expresión correcta será ``/inventario/producto[@codigo="AAA-111"]``, la cual nos devuelve lo siguiente:

.. code-block:: xml

    <producto codigo="AAA-111">
        <nombre>Teclado</nombre>
        <peso unidad="g">480</peso>
    </producto>
    
De hecho se puede profundizar aún más y usar la expresión ``/inventario/producto[@codigo="AAA-111"]/nombre`` que extrae los nombres de los elementos producto cuyo código sea "AAA-111". Y aún más para extraer solo el texto de los elementos nombre usando la expresión ``/inventario/producto[@codigo="AAA-111"]/nombre/text()``. Como vemos en esta última expresión ya hemos usado una función, en concreto ``text()``.

En una condicion podemos referirnos a cualquier hijo de un nodo, así por ejemplo, podemos extraer los productos cuyo peso sea mayor de 50 usando ``/inventario/producto[peso>=50]``. Sin embargo, sabemos que la unidad es importante, por lo que en realidad podemos extraer los que pesen más de 50 gramos usando esto ``/inventario/producto[peso>=50 and peso/@unidad="g"]``.

Si se observa despacio el fichero, se observará que en realidad el tercer producto debería aparecer también. Para ello debemos ampliar la expresión convirtiendo los 50 g a kg, es decir comparando con 0.005 kg y la expresión siguiente ``/inventario/producto[(peso>=50 and peso/@unidad="g") or (peso>=0.005 and peso/@unidad="kg")]``.

Utilizando XPath y XSLT veremos que podemos transformar un XML en casi cualquier otro XML utilizando la potencia combinada de ambos lenguajes.
    



Adaptación y transformación de XML
===========================================

Muy a menudo va a ocurrir que un cierto formato XML va a ampliarse o a modificarse o simplemente se necesita convertir un documento XML en otro con un formato distinto.

Supongamos una estructura como la siguiente:

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<catalogo>
		<libro>
			<title>Don Quijote</title>
			<autor>Cervantes</autor>
		</libro>
		<libro>
			<title>
			Poeta en Nueva York
			</title>
			<autor>Lorca</autor>
		</libro>
	</catalogo>	


Supongamos que un cierto sitio se necesita almacenar la información de esta forma:


.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<listadolibros>
		<libro>
			<titulo autor="Cervantes">Don Quijote</title>
		</libro>
		<libro>
			<titulo autor="Lorca">
			Poeta en Nueva York
			</title>
		</libro>
	</listadolibros>	


En general, para poder modificar o presentar los XML se puede hacen varias cosas:

* En primer lugar, se puede usar CSS para poder cargar los documentos XML en un navegador y mostrarlos de forma aceptable.
* Se pueden utilizar otras tecnologías para transformar por completo la estructura del XML.

	* Se puede usar un lenguaje llamado XSLT (Xml Stylesheet Language Transformation) para convertir el XML en otro distinto.
	
	* Se puede utilizar XSL:FO (Xml Stylesheet Language: Formatting Objects) cuando se desee convertir el documento en algo que se desee imprimir (normalmente un PDF)
	
	
CSS con XML
----------------------------------------------

Supongamos de nuevo el archivo anterior, el cual ahora queremos mostrar en un navegador:


.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<catalogo>
		<libro>
			<title>Don Quijote</title>
			<autor>Cervantes</autor>
		</libro>
		<libro>
			<title>
			Poeta en Nueva York
			</title>
			<autor>Lorca</autor>
		</libro>
	</catalogo>	

	
Si usamos el archivo ``estilo.css`` de esta forma:

.. code-block:: css

	catalogo{
		background-color:rgb(220, 230, 220);
		display:block;
	}

	libro{
		display:block;
		border: solid black 1px;
		margin-bottom:20px;
	}
	title{
		margin: 10px;
		display:block;
	}
	autor{
		display:block;
		font-face:Arial;
		text-decoration:underline;
	}


Veremos algo como esto:


.. image:: estilo-xml.png
	:align: center
	:scale: 50%


Ejercicio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crear una hoja de estilo asociada al catálogo anterior, que muestre la información de cada libro de forma parecida a una tabla, en la que el ``title`` utilice un color de fondo distinto del ``autor``.


.. image:: estilo-xml2.png
	:align: center
	:scale: 50%

.. code-block:: css

	catalogo{
		background-color:rgb(220, 230, 220);
		display:block;
	}

	libro{
		display:block;
		width:100%;
		margin-bottom:40px;
		clear:both;
	}
	title{
		float:left;
		width:45%;
		border:solid black 1px;
		padding:5px;
		text-align:center;
		background-color:rgb(180,180,240);
	}
	autor{
		float:left;
		text-align:center;
		width:45%;
		border:solid black 1px;
		padding:5px;
		background-color:rgb(340,180,240);
	}

Transformación de XML
----------------------------------------------

Si deseamos *transformar un XML en otro XML* necesitaremos usar XSLT. Un archivo XSLT tiene la extensión XSL e indica las reglas para convertir entre formatos XML.

El documento XSL básico sería así (los navegadores la darán por mala, ya que no hace absolutamente
nada):

.. code-block:: xml

	
	<?xml version="1.0" encoding="UTF-8"?>
	<xsl:stylesheet>
	</xsl:stylesheet>	
	
	
En este caso xsl es el espacio de nombres. Un espacio de nombres es un contenedor que
permite evitar que haya confusiones entre unas etiquetas y otras que se llamen igual. En este
caso, queremos usar la etiqueta <stylesheet> definida por el W3C. Una hoja básica sería
esta

.. code-block:: xml

	
	<?xml version="1.0" encoding="UTF-8"?>
	<xsl:stylesheet version="1.0" 
		xmlns:xsl=
		"http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<html>
				<head>
					<title>
						Resultado
					</title>
				</head>
				<body>
					Documento resultado
				</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>	


Algunos navegadores no ejecutan XSL por seguridad. Los detalles de como “abrir” la seguridad de cada uno de estos navegadores deben investigarse en el manual de cada uno de ellos. 

Cabe destacar que esta hoja simplemente genera HTML básico pero no recoge ningún dato del XML original.	

Ejercicio (carga de estilos)
----------------------------------------------

Hacer que el archivo XML de libros cargue esta hoja de estilos.

Solución: consiste en añadir una línea al archivo que referencie el archivo de transformación y el tipo de lenguaje usado para transformar.

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet href="hoja1.xsl" type="text/xsl"?>

	<catalogo>		
		... (El resto es igual)
	</catalogo>
		
Ejercicio (conversion entre XMLs)
-------------------------------------

Dado el fichero de información del catálogo, transformar dicho XML en otro fichero en el que la etiqueta ``title`` vaya en español, es decir, que el resultado quede así:

.. code-block:: xml

  <catalogo>
    <libro>
      <title>Don Quijote</title>
      <autor>Cervantes</autor>
    </libro>
    <libro>
      <title>
      Poeta en Nueva York
      </title>
      <autor>Lorca</autor>
    </libro>
  </catalogo>	


La solución podría ser algo así:

.. code-block:: xml

  <xsl:stylesheet
      version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
      <catalogo>
        <xsl:for-each select="/catalogo/libro">
          <libro>
            <titulo>
              <xsl:value-of select="title"/>
            </titulo>
            <autor>
              <xsl:value-of select="autor"/>
            </autor>
          </libro>
        </xsl:for-each>
      </catalogo>
    </xsl:template>
  </xsl:stylesheet>
                  
  
Ejercicio (generación de atributos)
------------------------------------------
Dado el archivo XML del catálogo generar un XML en el que el autor vaya como un atributo del título, es decir, que quede algo así:

.. code-block:: xml

  <catalogo>
    <libro>
      <titulo escritor="Cervantes">Don Quijote</titulo>
    </libro>
    <libro>
      <titulo escritor="Lorca">
      Poeta en Nueva York
      </titulo>
    </libro>
  </catalogo>

La solución:

.. code-block:: xml

  <xsl:stylesheet
      version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/">
      <catalogo>
        <xsl:for-each select="/catalogo/libro">
          <libro>
            <titulo>
              <xsl:attribute name="escritor">
                <xsl:value-of select="autor"/>
              </xsl:attribute>
              <xsl:value-of select="title"/>
            </titulo>
          </libro>
        </xsl:for-each>
      </catalogo>
    </xsl:template>    
  </xsl:stylesheet>
                  
Ejercicio (tabla HTML)
------------------------
Convertir el catalogo XML en una tabla HTML

Solución:

.. code-block:: xml
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
      <html>
        <head>
          <title>Catalogo de libros</title>
        </head>
        <body>
          <h1>Listado de libros</h1>
          <table border="1">
            <xsl:for-each select="catalogo/libro">
              <tr>
                <td>
                  <xsl:value-of select="title"/>
                </td>
                <td>
                  <xsl:value-of select="autor"/>
                </td>
              </tr>
            </xsl:for-each>
          </table>
        </body>
      </html>
    </xsl:template>
  </xsl:stylesheet>

Ejercicio (generacion)
----------------------------------------------
Hacer que el XSL genere un HTML con información del archivo XML de libro.

.. code-block:: xml

	<?xml version="1.0"?>
	<xsl:stylesheet version="1.1" xmlns:xsl=
			"http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<html>
				<head>
					<title>Ejemplo de transformación</title>
				</head>
				<body>
					<h1>Resultado</h1>
					<xsl:for-each select="catalogo/libro">
						<p>
							<xsl:value-of select="title"/>
						</p>
					</xsl:for-each>
				</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>		


Ejercicio
----------------------------------------------
Extraer los títulos de los libros pero consiguiendo encerrarlos en una lista ordenada HTML para que aparezcan numerados.


.. code-block:: xml

	<?xml version="1.0"?>
	<xsl:stylesheet version="1.1" xmlns:xsl=
			"http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<html>
				<head>
					<title>Ejemplo de transformación</title>
				</head>
				<body>
					<h1>Resultado</h1>
					<ol>
					<xsl:for-each select="catalogo/libro">
						<li>
							<xsl:value-of select="title"/>
						</li>
					</xsl:for-each>
					</ol>
				</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>		


Ejercicio
----------------------------------------------

Supongamos que ahora un libro tiene varios autores y el XML es algo así:

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet href="hoja1.xsl" type="text/xsl"?>

	<catalogo>
			<libro>
					<title>Don Quijote</title>
					<autores>
							<autor>Cervantes</autor>
					</autores>
			</libro>
			<libro>
				<title>Patrones de diseño en programación</title>
				<autores>
					<autor>Erich Gamma</autor>
					<autor>John Vlissides</autor>
					<autor>Ralph Johnson</autor>
				</autores>
			</libro>
	</catalogo>
	
¿Como mostrar en HTML el título y todos los autores de cada libro?	

.. code-block:: xml

	<?xml version="1.0"?>
	<xsl:stylesheet version="1.1" xmlns:xsl=
			"http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<html>
				<head>
					<title>Ejemplo de transformación</title>
				</head>
				<body>
					<h1>Resultado</h1>
					<ol>
					<xsl:for-each select="catalogo/libro">
						<li>
							<xsl:value-of select="title"/>
							<ol>
								<xsl:for-each select="autores/autor">
									<li>
										<xsl:value-of select="."/>
									</li>
								</xsl:for-each> <!--Fin del bucle autores-->
							</ol>
						</li>
					</xsl:for-each> <!--Fin del recorrido de libro-->
					</ol>
				</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>		
	
	
Ejercicio
----------------------------------------------

Se desea hacer lo mismo que en el ejercicio anterior pero haciendo que los autores aparezcan de forma ordenada.

La solución está fundamentada en el uso de la etiqueta siguiente:

.. code-block:: xml

	<xsl:for-each select="...">
		<xsl:sort select="..." ordering="...">
			..cosas del bucle...
		</xsl:sort>
	</xsl:for-each>

La solución completa sería así:

.. code-block:: xml

	<?xml version="1.0"?>
	<xsl:stylesheet version="1.1" xmlns:xsl=
			"http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<html>
				<head>
					<title>Ejemplo de transformación</title>
				</head>
				<body>
					<h1>Resultado</h1>
					<ol>
					<xsl:for-each select="catalogo/libro">
						<li>
							<xsl:value-of select="title"/>
							<ol>
								<xsl:for-each select="autores/autor">
								<xsl:sort order="descending"/>
									<li>
										<xsl:value-of select="."/>
									</li>
								</xsl:for-each>
							</ol>
						</li>
					</xsl:for-each> <!--Fin del recorrido de libro-->
					</ol>
				</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>	



Ejercicio
----------------------------------------------

Suponiendo que además todos los libros tienen además un elemento ``<fechaedicion>`` mostrar los libros editados despues del 2000.

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet href="hoja1.xsl" type="text/xsl"?>

	<catalogo>
			<libro>
					<title>Don Quijote</title>
					<autores>
							<autor>Cervantes</autor>
					</autores>
					<fechaedicion>1984</fechaedicion>
			</libro>
			<libro>
				<title>Patrones de diseño en programación</title>
				<autores>
					<autor>Ralph Johnson</autor>
					<autor>Erich Gamma</autor>
					<autor>John Vlissides</autor>
				</autores>
				<fechaedicion>2007</fechaedicion>
			</libro>
	</catalogo>	
	
.. code-block:: xml

	<?xml version="1.0"?>
	<xsl:stylesheet version="1.1" xmlns:xsl=
			"http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<html>
				<head>
					<title>Ejemplo de transformación</title>
				</head>
				<body>
					<h1>Resultado</h1>
					<ol>
					<xsl:for-each select="catalogo/libro">
						<xsl:if test="fechaedicion &gt; 2000">
						<li>
							<xsl:value-of select="title"/>
							<ol>
								<xsl:for-each select="autores/autor">
								<xsl:sort order="descending"/>
									<li>
										<xsl:value-of select="."/>
									</li>
								
								</xsl:for-each>
							</ol>
						</li>						
						</xsl:if>
						
					</xsl:for-each> <!--Fin del recorrido de libro-->
					</ol>
				</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>			
	
	
En general, las condiciones se escriben así:

* > o mayor que o ``&gt;``	
* < o menor que o ``&lt;``
* >= o mayor o igual o ``&ge;``
* <= o menor o igual o ``&le;``
* = o igual o ``&eq;``
* <> o distinto o ``&neq;``

Ejercicio XSL, paso a paso
------------------------------------------------------

Dado el siguiente XML crear un programa con XSLT que muestre los titulos y los autores de los libros cuya fecha de edicion sea posterior al 2000.

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <?xml-stylesheet	type="text/xsl" 	href="ejercicio1.xsl"?>
	<catalogo>
		<libro fechaedicion="1999">
			<titulo>Don Quijote</titulo>
			<autores>
				<autor>Cervantes</autor>
			</autores>
		</libro>
		<libro fechaedicion="2005">
			<titulo>
			La sociedad civil moderna
			</titulo>
			<autores>
				<autor>Luis Diaz</autor>
				<autor>Pedro Campos</autor>
			</autores>
		</libro>
	</catalogo>
	
Hagámoslo paso a paso. En primer lugar tendremos que crear el fichero ``ejercicio1.xsl`` y crear la estructura básica:

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.1">
	<xsl:template match="/">

	</xsl:template>
	</xsl:stylesheet>

Ahora recorramos los libros que hay en el catalogo (recordemos que la estructura es ``catalogo/libro``. Simplemente por ver si funciona, de momento el navegado solo muestra los títulos y en una sola línea.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.1">
	<xsl:template match="/">
	  <xsl:for-each select="catalogo/libro">
		<xsl:value-of select="titulo"/>
	  </xsl:for-each>
	</xsl:template>
	</xsl:stylesheet>
   
.. figure:: ejercicio1xslpaso1.png
   :figwidth: 50%
   :align: center	

   Paso inicial del XSL
   
Avancemos un poco más y creemos una estructura HTML válida

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.1">
	<xsl:template match="/">
	<html>
	  <head>
		 <title>Filtrado con XSLT</title>
	  </head>
	  <body>
	  <h1>Filtrado con XSLT</h1>
	  <ol>
		<xsl:for-each select="catalogo/libro">
			<li>
			<xsl:value-of select="titulo"/>
			</li>
		</xsl:for-each>
	  </ol>
	  </body>
	</html>
	</xsl:template>
	</xsl:stylesheet>   

.. figure:: ejercicio1xslpaso2.png
   :figwidth: 50%
   :align: center	

   Extrayendo los titulos con XSL
   
Ahora vamos a procesar solo los libros cuya ``fechaedicion`` sea posterior al 2000. Añadamos un ``if``

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.1">
	<xsl:template match="/">
	<html>
	  <head>
		 <title>Filtrado con XSLT</title>
	  </head>
	  <body>
	  <h1>Filtrado con XSLT</h1>
	  <ol>
		<xsl:for-each select="catalogo/libro">
		
			<xsl:if test="@fechaedicion &gt; 2000">
			
			<li>
			<xsl:value-of select="titulo"/>
			</li>
			
			</xsl:if>
		</xsl:for-each>
	  </ol>
	  </body>
	</html>
	</xsl:template>
	</xsl:stylesheet>   

.. figure:: ejercicio1xslpaso3.png
   :figwidth: 50%
   :align: center	

   Procesando los que son > 2000
   
Ahora para cada libro queremos también mostrar los elementos autor con su propia lista

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.1">
	<xsl:template match="/">
	<html>
	  <head>
		 <title>Filtrado con XSLT</title>
	  </head>
	  <body>
	  <h1>Filtrado con XSLT</h1>
	  <ol>
		<xsl:for-each select="catalogo/libro">
		
			<xsl:if test="@fechaedicion &gt; 2000">
			
			<li>
			<xsl:value-of select="titulo"/>
			</li>
			
			<ol>
				<xsl:for-each select="autores/autor">
					<li>
						<!--El elemento actual es .-->
						<xsl:value-of select="."/>
					</li>
				</xsl:for-each>
			</ol>
			
			</xsl:if>
		</xsl:for-each>
	  </ol>
	  </body>
	</html>
	</xsl:template>
	</xsl:stylesheet>   
	
Y el navegador muestra lo siguiente

.. figure:: ejercicio1xslpaso4.png
   :figwidth: 50%
   :align: center	

   Mostrando también los autores
   
   
Ejercicio: condiciones complejas
-----------------------------------

Supongamos que nos dan el siguiente fichero de inventario:

.. code-block: xml

  <inventario>
    <elemento codigo="C1">
      <peso unidad="kg">10</peso>
      <nombre>Ordenador</nombre>
    </elemento>
    <elemento codigo="C2">
      <peso unidad="g">450</peso>
      <nombre>Altavoz</nombre>
    </elemento>
  </inventario>

Y supongamos que nos dicen que se necesita extraer la información relativa a los productos que pesan más de 5. Una primera aproximación equivocada sería esta:

.. code-block:: xml

  
  <xsl:template match="/">
    <inventario>
      <xsl:for-each select="inventario/elemento">
        <xsl:if test="peso &gt; 5">
          <nombre>
            <xsl:value-of select="nombre"/>
          </nombre>
        </xsl:if>
      </xsl:for-each>
    </inventario>
  </xsl:template>
  </xsl:stylesheet>
  
Esta solución está equivocada porque de entrada *la pregunta está mal* Si se refieren a 5kg solo debería mostrarse el ordenador y si se refieren a 5g solo debería mostrarse el altavoz.


Una solución correcta sería esta. Obsérvese como se meten unos if dentro de otros para extraer la información deseada.

.. code-block:: xml

  <xsl:template match="/">
    <inventario>
      <xsl:for-each select="inventario/elemento">
        <xsl:if test="./peso/@unidad = 'kg'">
          <xsl:if test="peso &gt; 5">
            <nombre>
              <xsl:value-of select="nombre"/>
            </nombre>
          </xsl:if>
        </xsl:if>
        <xsl:if test="peso/@unidad = 'g'">
          <xsl:if test="peso &gt; 5000">
            <nombre>
              <xsl:value-of select="nombre"/>
            </nombre>
          </xsl:if>
        </xsl:if>
      </xsl:for-each>
    </inventario>
  </xsl:template>
  </xsl:stylesheet>

Transformación en tabla
---------------------------
Se nos pide convertir el inventario de antes en la tabla siguiente donde el peso debe estar normalizado y aparecer siempre en gramos:


.. image:: tabla_tras_xslt1.png
	:align: center
	:scale: 50%


Una posible solución sería:

.. code-block:: xml

  <xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">  
  <xsl:template match="/">
  <html>
    <head><title>Tabla de inventario</title></head>
    <body>
      <table border='1'>
        <xsl:for-each select="inventario/elemento">
          <tr>
            <td><xsl:value-of select="nombre"/></td>
            <td>
              <xsl:if test="peso/@unidad='kg'">
                <xsl:value-of select="peso * 1000"/>
              </xsl:if>
              <xsl:if test="peso/@unidad='g'">
                <xsl:value-of select="peso"/>
              </xsl:if>
            </td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>    
  </xsl:template>
  </xsl:stylesheet>
   
Transformacion de pedidos
---------------------------

Dado el siguiente archivo XML:

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<?xml-stylesheet href="estilo1.xsl" type="text/xsl"?>
	<pedido>
		<portatiles>
			<portatil>
				<peso>1430</peso>
				<ram unidad="GB">4</ram>
				<disco tipo="ssd">500</disco>
				<precio>499</precio>
			</portatil>
			<portatil>
				<peso>1830</peso>
				<ram unidad="GB">6</ram>
				<disco tipo="ssd">1000</disco>
				<precio>1199</precio>
			</portatil>
			<portatil>
				<peso>1250</peso>
				<ram unidad="GB">2</ram>
				<disco tipo="ssd">750</disco>
				<precio>699</precio>
			</portatil>
		</portatiles>
		<tablets>
			<tablet>
				<plataforma>Android</plataforma>
				<caracteristicas>
					<memoria medida="GB">2</memoria>
					<tamanio medida="pulgadas">6</tamanio>
					<bateria>LiPo</bateria>
				</caracteristicas>
			</tablet>
			<tablet>
				<plataforma>iOS</plataforma>
				<caracteristicas>
					<memoria medida="GB">4</memoria>
					<tamanio medida="pulgadas">9</tamanio>
					<bateria>LiIon</bateria>
				</caracteristicas>
			</tablet>
		</tablets>
	</pedido>   
	
Crear un fichero de estilos que permita mostrar la información de los portátiles en forma de tabla.

.. figure:: xsl1.png
   :figwidth: 50%
   :align: center
   
   Transformacion XSL
   
Una posible solución sería esta:

.. code-block:: xml

	<?xml version="1.0"?>
	<xsl:stylesheet version="1.1" 
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
			<xsl:template match="/">
				<html>
				<head>
					<title>Ejercicio 1</title>
				</head>
				<body>
				<h1>Resultado</h1>
				<table border="1">
				<tr>
						<td>Peso</td>
						<td>RAM</td>
						<td>Disco</td>
						<td>Precio</td>
				</tr>
				<xsl:for-each select=
					"pedido/portatiles/portatil">
				<tr>
					<td>
						<xsl:value-of select="peso"/>
					</td>
					<td>
						<xsl:value-of select="ram"/>
					</td>
					<td>
						<xsl:value-of select="disco"/>
					</td>
					<td>
						<xsl:value-of select="precio">
					</td>
				</tr>
				</xsl:for-each>
				</table>
			</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>      
   
Transformación de pedidos (II)
------------------------------------------------------

Con el mismo fichero de pedidos crear una sola tabla que tenga 3 columnas y aglutine información tanto de portátiles como de tablets:

* Cuando procesemos portátiles, las columnas serán respectivamente "precio", "ram" y "disco". Solo se procesan portátiles con más de 2GB de RAM.
* Cuando procesemos tablets, las columnas serán "plataforma", "ram" y "batería". Solo se procesan los tablets con más de 2GB de RAM y que además tengan un tamaño superior a 7 pulgadas.



El fichero siguiente ilustra una posible forma de hacerlo:

.. code-block:: xml

	<?xml version="1.0"?>
	<xsl:stylesheet version="1.1" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
		<xsl:template match="/">
			<html>
			<head>
				<title>Ejercicio 1</title>
			</head>
			<body>
				<h1>Resultado</h1>
				<table border="1">
				<xsl:for-each select=
				"pedido/portatiles/portatil">
				   <xsl:if test="ram &gt; 2">
					<tr>
					  <td>
						Precio:<xsl:value-of select="precio"/>
					  </td>
					  <td>
						Memoria:<xsl:value-of select="ram"/>
				      </td>
					  <td>
						Disco duro:<xsl:value-of select="disco"/>
					  </td>
					</tr>
				</xsl:if>
				</xsl:for-each>
				<xsl:for-each select="pedido/tablets/tablet">
				   <xsl:if test="caracteristicas/memoria &gt; 2">
					<xsl:if test="caracteristicas/tamanio &gt; 7">
						<tr>
						<td>
					    	<xsl:value-of select="plataforma"/>
						</td>						<td>
						<xsl:value-of select="caracteristicas/memoria"/>
						</td>
						<td>
						<xsl:value-of select="caracteristicas/bateria"/>
						</td>
					</tr>
			    	</xsl:if>
					</xsl:if>
					</xsl:for-each>
				</table>	
			</body>
			</html>
		</xsl:template>
	</xsl:stylesheet>   


	
Ejercicio (no se da la solución)
------------------------------------------------------
Poner en una lista ordenada (elemento ``ol``) todas las capacidades RAM que se encuentren en el fichero XML.




