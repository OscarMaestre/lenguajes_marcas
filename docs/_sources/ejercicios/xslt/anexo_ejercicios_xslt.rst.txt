Anexo: ejercicios sobre XSLT
=====================================

Fichero origen
----------------
Para los ejercicios siguiente supondremos que se va a trabajar con el fichero que se muestra a continuación:

.. code-block:: xml
    
    <inventario>
        <producto codigo="P1">
            <peso unidad="kg">10</peso>
            <nombre>Ordenador</nombre>
            <lugar edificio="B">
                <aula>10</aula>
            </lugar>
        </producto>
        <producto codigo="P2">
            <peso unidad='g'>500</peso>
            <nombre>Switch</nombre>
            <lugar edificio="A">
                <aula>6</aula>
            </lugar>
        </producto>
    </inventario>
    
    
Generación de lista con puntos
--------------------------------

Convertir el fichero origen en una lista punteada similar a la que se muestra en la figura:

.. image:: lista_punteada.png
	:align: center
	:scale: 50%
    
.. code-block:: xml
    
    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Resultado HTML</title>
            </head>
            <body>
                <ul>
                    <xsl:for-each select="inventario/producto">
                        <li>
                            Elemento
                            <xsl:value-of select="./@codigo"/>
                            <ul>
                                <li>
                                    Nombre:
                                    <xsl:value-of select="nombre"/>
                                </li>
                                <li>
                                    Peso:
                                    <xsl:value-of select="peso"/>
                                    <xsl:value-of
                                        select="peso/@unidad"/>
                                </li>
                            </ul>
                        </li>
                    </xsl:for-each>
                </ul>
            </body>
        </html>
    </xsl:template>
    </xsl:stylesheet>

Filtrado
----------------
Replicar la estructura del fichero pero filtrando
los elementos y haciendo que solo aparezcan los que estén
en el aula A6


Recuperación de elementos pesados
----------------------------------

Se pide un XSLT que muestre exactamente la misma información del fichero origen pero sin mostrar los elementos cuyo peso sea menor de 7.

Una posible solución sería esta:

.. code-block:: xml
    
    <xsl:stylesheet
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <inventario>
        <xsl:for-each select="inventario/producto">
            <xsl:if test="peso &lt; 7">
                <producto>
                    <peso>
                        <xsl:value-of select="peso"/>
                    </peso>
                    <nombre>
                        <xsl:value-of select="nombre"/>
                    </nombre>
                    <lugar>
                        <xsl:attribute name="edificio">
                            <xsl:value-of
                                select="lugar/@edificio"/>
                        </xsl:attribute>
                        <aula>
                            <xsl:value-of
                                select="lugar/aula"/>
                        </aula>
                    </lugar>
                </producto>
            </xsl:if>
        </xsl:for-each>
        </inventario>
    </xsl:template>    
    </xsl:stylesheet>
    
Sin embargo, **dicha solución está mal** porque una pregunta básica es "el peso está en kg o en g", por lo que en realidad la condición de filtrado debe refinarse un poco más.

Supongamos entonces que el enunciado correcto pone el peso en kg. Así, la solución entonces podría hacerse de esta manera.




Productos del edificio B
----------------------------

Se pide ahora mostrar en el resultado la misma información del fichero origen pero solo en los casos en que el lugar del producto sea el edificio B

La solución es muy parecida, necesitando solamente modificar la condición.


.. code-block:: xml

    
    <xsl:stylesheet
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <inventario>
        <xsl:for-each select="inventario/producto">
            <xsl:if test="lugar/@edificio='B'">
                <producto>
                    <peso>
                        <xsl:value-of select="peso"/>
                    </peso>
                    <nombre>
                        <xsl:value-of select="nombre"/>
                    </nombre>
                    <lugar>
                        <xsl:attribute name="edificio">
                            <xsl:value-of
                                select="lugar/@edificio"/>
                        </xsl:attribute>
                        <aula>
                            <xsl:value-of
                                select="lugar/aula"/>
                        </aula>
                    </lugar>
                </producto>
            </xsl:if>
        </xsl:for-each>
        </inventario>
    </xsl:template>    
    </xsl:stylesheet>
    
Tabla de localizaciones
--------------------------

Generar una tabla HTML que muestre la información del fichero origen de la manera siguiente:

.. image:: xslt_tabla_edificio_aula.png
	:align: center
	:scale: 50%
    
.. code-block:: xml
    
    <xsl:stylesheet
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <inventario>
        <xsl:for-each select="inventario/producto">
            <xsl:if test="lugar/@edificio='B'">
                <producto>
                    <peso>
                        <xsl:value-of select="peso"/>
                    </peso>
                    <nombre>
                        <xsl:value-of select="nombre"/>
                    </nombre>
                    <lugar>
                        <xsl:attribute name="edificio">
                            <xsl:value-of
                                select="lugar/@edificio"/>
                        </xsl:attribute>
                        <aula>
                            <xsl:value-of
                                select="lugar/aula"/>
                        </aula>
                    </lugar>
                </producto>
            </xsl:if>
        </xsl:for-each>
        </inventario>
    </xsl:template>    
    </xsl:stylesheet>
    
    
Tablas con edificios separados
----------------------------------

Hacer una plantilla que fabrique una tabla
con los datos de los productos del edificio A
y otra tabla separada para los productos del edificio B

.. image:: xslt_tabla_edificio_separadas.png
	:align: center
	:scale: 50%

Una posible solución sería esta:

.. code-block:: xml

    <xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head><title>Datos por edificio</title></head>
            <body>
                <h1>Edificio A</h1>
                <table border='1'>
                <xsl:for-each select="inventario/producto">
                    <xsl:if test="lugar/@edificio='A'">
                        <tr>
                            <td>
                                <xsl:value-of
                                    select="nombre"/>
                            </td>
                            <td>
                                <xsl:value-of
                                    select="peso"/>
                            </td>
                            <td>
                                <xsl:value-of
                                select="lugar/@edificio"/>
                                <xsl:value-of
                                select="lugar/aula"/>
                            </td>
                        </tr>
                    </xsl:if>
                </xsl:for-each>
                </table>
                <h1>Edificio B</h1>
                <table border='1'>
                <xsl:for-each select="inventario/producto">
                    <xsl:if test="lugar/@edificio='B'">
                        <tr>
                            <td>
                                <xsl:value-of
                                    select="nombre"/>
                            </td>
                            <td>
                                <xsl:value-of
                                    select="peso"/>
                            </td>
                            <td>
                                <xsl:value-of
                                select="lugar/@edificio"/>
                                <xsl:value-of
                                select="lugar/aula"/>
                            </td>
                        </tr>
                    </xsl:if>
                </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
    </xsl:stylesheet>

Productos del aula 6
-------------------------

Se pide generar un inventario en el que aparezcan solo los nombres de productos que estén en el aula 6.

.. code-block:: xml
  
  <xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <inventario>
    <xsl:for-each select="/inventario/producto">
      <xsl:if test=" lugar/aula= '6' ">
        <nombre>
          <xsl:value-of select="nombre"/>
        </nombre>
      </xsl:if>
    </xsl:for-each>
    </inventario>
  </xsl:template>
  </xsl:stylesheet>

Productos del edificio B
----------------------------

El siguiente ejercicio es muy parecido al anterior, con la salvedad de que ahora solo nos piden los nombres de los productos ubicados en el edificio B.

.. code-block:: xml

  <inventario>
    <xsl:for-each select="/inventario/producto">
      <xsl:if test=" lugar/@edificio = 'B' ">
        <nombre>
          <xsl:value-of select="nombre"/>
        </nombre>
      </xsl:if>
    </xsl:for-each>
    </inventario>
  </xsl:template>
  </xsl:stylesheet>


    
Condiciones múltiples: peso ligero y edificio A
-------------------------------------------------

Se pide ahora generar un fichero HTML con una tabla pero en la que solo aparezcan los productos cuyo edificio sea el A **y además** pesen menos de 7kg.

.. code-block:: xml
    
    <xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head><title>Resultados</title></head>
            <body>
                <xsl:for-each select="inventario/producto">
                    <xsl:if test="lugar/@edificio = 'A'">
                        <xsl:if test="peso/@unidad = 'g'">
                            <xsl:if test="peso &lt; 7000">
                                <tr>
                                    <td>
                                        <xsl:value-of
                                        select="nombre"/>
                                    </td>
                                </tr>
                            </xsl:if>
                        </xsl:if>
                        <xsl:if test="peso/@unidad = 'Kg'">
                            <xsl:if test="peso &lt; 7">
                                <tr>
                                    <td>
                                        <xsl:value-of
                                        select="nombre"/>
                                    </td>
                                </tr>
                            </xsl:if>
                        </xsl:if>
                    </xsl:if>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>
    </xsl:stylesheet>




Ejercicio de examen XSLT
----------------------------

Dado el siguiente fichero XML

.. code-block:: xml

  <catalogo>
    <libro isbn="i1">
      <titulo>Don Quijote</titulo>
      <autores>
        <autor nacimiento="1547">Cervantes</autor>
      </autores>
    </libro>
    <libro isbn="i2">
      <titulo>Antologia</titulo>
      <autores>
          <autor nacimiento="1898">Lorca</autor>
          <autor nacimiento="1910">Miguel Hernandez</autor>
      </autores>
    </libro>
  </catalogo>
  
Conseguir lo siguiente:

1. Mostrar en un HTML con lista numerada los títulos de los libros con algún autor nacido despues de 1900.

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:template match="/">
        <html>
          <head>
            <title>Resultado</title>
          </head>
          <body>
            <ol>
              <!--Recorremos los autores-->
              <xsl:for-each select="catalogo/libro/autores/autor">
                <!--Y si nacieron despues de 1900..."-->
                <xsl:if test="@nacimiento > 1900">
                  <li>
                    <!--Entonces "retrocedemos"
                    para extraer el titulo-->
                    <xsl:value-of select="../../titulo"/>
                  </li>
                </xsl:if>
              </xsl:for-each>
            </ol>
          </body>
        </html>
      </xsl:template>
    </xsl:stylesheet>

2. Mostrar en un HTML la lista de los autores ordenada por orden alfabético inverso.

.. code-block:: xml


    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
      <xsl:template match="/">
        <html>
          <head>
            <title>Resultado</title>
          </head>
          <body>
            <ol>
              <xsl:for-each select="catalogo/libro/autores/autor">
                <xsl:sort select="." order="descending"/>
                <li>
                  <xsl:value-of select="."/>
                </li>
              </xsl:for-each>
            </ol>
          </body>
        </html>
      </xsl:template>
    </xsl:stylesheet>


3. Mostrar el nombre de los autores nacidos despues del año 1700.



.. code-block:: xml
    
    <xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head><title>Resultado</title></head>
            <body>
                <table border='1'>
                    <tr>
                        <td>Nombre</td>
                        <td>Año nacimiento</td>
                    </tr>
                    <xsl:for-each
                    select="catalogo/libro/autores/autor">
                    <xsl:if test="@nacimiento &gt; 1700">
                        <td>
                            <xsl:value-of select="."/>
                        </td>
                        <td>
                            <xsl:value-of select="@nacimiento"/>
                        </td>
                    </xsl:if>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
    </xsl:stylesheet>



Transformación de un XML bancario
--------------------------------------------------------------------



Una empresa utiliza el siguiente XML para intercambiar información entre bases de datos de distintos proveedores. Sin embargo han comprado un nuevo sistema que necesita que la información tenga una estructura siguiente. Los dos listados que se ven a continuación ilustran la estructura original y la nueva estructura que deben tener los datos. Crear el XSLT que permita convertir la información original en un formato que pueda entender el nuevo sistema.


.. code-block:: xml
    
    <!--Estructura original de la información-->
    <listado>
        <cuenta>
            <titular dni="5671001D">Ramon Perez</titular>
            <saldoactual moneda="euros">12000</saldoactual>
            <fechacreacion>13-abril-2012</fechacreacion>
        </cuenta>
        <fondo>
            <cuentaasociada>20-A</cuentaasociada>
            <datos>
                <cantidaddepositada>20000</cantidaddepositada>
                <moneda>Euros</moneda>
            </datos>
        </fondo>
        <fondo>
            <cuentaasociada>21-DX</cuentaasociada>
            <datos>
                <cantidaddepositada>4800</cantidaddepositada>
                <moneda>Dolares</moneda>
            </datos>
        </fondo>
        <cuenta>
            <titular dni="39812341C">Carmen Diaz</titular>
            <saldoactual moneda="euros">1900</saldoactual>
            <fechacreacion>15-febrero-2011</fechacreacion>
        </cuenta>
    </listado>
    
    
.. code-block:: xml

    <!--Estructura final que debemos conseguir-->
    <datos>
        <cuentas>
            <cuenta dnititular="5671001D">
                <creacion>13-abril-2012</creacion>
                <titular>Ramon Perez</titular>
                <saldoactual>12000 euros</saldoactual>
                
            </cuenta>
            <cuenta dnititular="39812341C">
                <creacion>15-febrero-2011</creacion>
                <titular>Carmen Diaz</titular>
                <saldoactual>1900 euros</saldoactual>
                
            </cuenta>
        </cuentas>
        <fondos>
            <fondo cuentaasociada="20-A">
                <cantidaddepositada>20000</cantidaddepositada>
                <moneda>Euros</moneda>
            </fondo>
            <fondo cuentaasociada="21-DX">            
                <cantidaddepositada>4800</cantidaddepositada>
                <moneda>Dolares</moneda>
            </fondo>
        </fondos>
    </datos>

Análisis del problema
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Es necesario hacer varios cambios:

1. Se ha cambiado el nombre de elemento raíz de ``listado`` a ``datos``.
2. Ahora todos los elementos ``cuenta`` van dentro de un nuevo elemento ``cuentas`` y todos los elementos ``fondo`` van dentro de un nuevo elemento ``fondos``.
3. El ``dni`` se ha movido del elemento ``titular`` al elemento ``cuenta``.
4. La ``fechacreación`` se ha movido y se ha renombrado a ``creacion``.
5. El elememento ``moneda`` desaparece y su texto se ha puesto al lado de la cantidad que hay en ``saldoactual``.
6. En el elemento ``fondo`` se ha quitado el elemento ``datos``.
7. El elemento ``cuentaasociada`` ha pasado a ser un atributo.



Solución paso a paso
~~~~~~~~~~~~~~~~~~~~~~

Empecemos por crear una hoja muy básica, que busque el elemento raíz y devuelva como salida el elemento ``datos`` (que va a ser la nueva raíz)

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>            
        </datos>
    </xsl:template>
    </xsl:stylesheet>    

    
Si probamos dicho XSLT aplicándolo al XML original obtendremos esto:

.. code-block:: xml

    <datos/>
    
No pasa nada porque se obtenga el elemento raíz vacío, el programa de transformación lo hace para ahorrar tiempo y bytes.

Una vez que hemos cambiado el elemento raíz tenemos que generar dos elementos más que agrupen los elementos ``cuenta`` y los elementos ``fondo``. Para ello, basta con escribirlos como muestra la siguiente hoja de estilo.

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas></cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Ahora tenemos que ir buscando todos los elementos ``cuenta`` y meterlos dentro de ``cuentas``. Despues resolveremos el problema de los fondos. Para recorrer elementos necesitamos un bucle ``for-each``. Como la plantilla ya nos ha situado en la raíz necesitaremos que el bucle nos vaya dando cada uno de los elementos ``listado/cuenta``. Es decir, le pedimos al bucle que se meta en el elemento hijo ``listado`` y nos vaya dando cada uno de los elementos ``cuenta`` que hay dentro. Un posible bucle sería este:

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta></cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Que al pasárselo a nuestros datos nos da esto:

.. code-block:: xml

    <datos>
      <cuentas>
        <cuenta/>
        <cuenta/>
      </cuentas>
      <fondos/>
    </datos>
    
Como puede verse, la plantilla genera dos elementos ``cuenta``, uno por cada ``cuenta`` que nos da el bucle. Obsérvese que podríamos haber hecho esto para tener un nombre de elemento distinto, **y este es el "truco" para poder cambiar de nombre un elemento** :



.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <otroelemento></otroelemento>
                </xsl:for-each>
            </cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Sigamos con el problema original: ya hemos creado un elemento ``cuentas`` que lleva dentro un elemento ``cuenta`` para cada una de las cuentas originales. Ahora en dicho elemento ``cuenta`` vamos a meter dentro un atributo llamado ``dnititular`` usando la etiqueta ``xsl:attribute`` que debe ir **dentro del elemento al que le queramos poner el atributo y además al principio**. Si queremos varios atributos no pasa nada podemos ponerlos todos dentro del elemento pero recordando ponerlos al principio.

Así, el código siguiente nos fabrica el atributo.

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <!--Esto añade el atributo dnititular a cuenta-->
                        <xsl:attribute name="dnititular">10</xsl:attribute>
                    </cuenta>                    
                </xsl:for-each>
            </cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>

Pero hay un problema, todas las cuentas tienen el ``dnititular`` a 10. Necesitamos la etiqueta ``value-of`` que nos permite **extraer el contenido de un elemento o atributo**, en este caso queremos extrar el valor del atributo ``dni`` que está dentro del elemento ``titular``. Esto se hace con ``titular/@dni`` que significa "extraer el atributo dni que debe estar dentro del elemento titular".

Así, el código siguiente:

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                    </cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Nos devuelve como resultado:

.. code-block:: xml

    <datos>
      <cuentas>
        <cuenta dnititular="5671001D"/>
        <cuenta dnititular="39812341C"/>
      </cuentas>
      <fondos/>
    </datos>

El paso siguiente va a ser crear el elemento ``titular`` que también se llama ``titular`` en el archivo original. Para ello lo metemos dentro de ``cuenta`` y permitiendo que la creación del atributo ``dnititular`` se quede al principio.

El código XSLT es este

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                        <!--Creamos el elemento titular y metemos
                        dentro del valor original del titular-->
                        <titular>
                            <xsl:value-of select="titular"/>
                        </titular>
                    </cuenta>                    
                </xsl:for-each>
            </cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Que genera el siguiente resultado:

.. code-block:: xml
    
    <datos>
      <cuentas>
        <cuenta dnititular="5671001D">
          <titular>Ramon Perez</titular>
        </cuenta>
        <cuenta dnititular="39812341C">
          <titular>Carmen Diaz</titular>
        </cuenta>
      </cuentas>
      <fondos/>
    </datos>
    
    
Ahora vamos a crear el elemento ``saldoactual``. Dentro de ese elemento debemos escribir el texto que ya tuviese el ``saldoactual`` antiguo y escribiendo al lado el atributo ``moneda``.

El código necesario es este

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                        <!--Creamos el elemento titular y metemos
                        dentro del valor original del titular-->
                        <titular>
                            <xsl:value-of select="titular"/>
                        </titular>
                        <!--Creamos el saldo actual-->
                        <saldoactual>
                            <!--Y metemos dentro la cantidad que tuviese
                            el fichero original...-->
                            <xsl:value-of select="saldoactual"/>
                            <!--Y extraemos la moneda...-->
                             <xsl:value-of select="saldoactual/@moneda"/>
                        </saldoactual>
                    </cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Y el resultado es este:

.. code-block:: xml

    <datos>
      <cuentas>
        <cuenta dnititular="5671001D">
          <titular>Ramon Perez</titular>
          <saldoactual>12000euros</saldoactual>
        </cuenta>
        <cuenta dnititular="39812341C">
          <titular>Carmen Diaz</titular>
          <saldoactual>1900euros</saldoactual>
        </cuenta>
      </cuentas>
      <fondos/>
    </datos>


Por último, añadamos la fecha de creación. En el fichero original se llama ``fechacreación`` y en el fichero final se llama ``creación`` y además va como primer elemento. El XSLT sería este:

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                        <!--Creamos el elemento "creación" que en
                        realidad contiene el texto del elemento
                        "fechacreación" original-->
                        <creacion>
                            <xsl:value-of select="fechacreacion"/>
                        </creacion>
                        <!--Creamos el elemento titular y metemos
                        dentro del valor original del titular-->
                        <titular>
                            <xsl:value-of select="titular"/>
                        </titular>
                        <!--Creamos el saldo actual-->
                        <saldoactual>
                            <!--Y metemos dentro la cantidad que tuviese
                            el fichero original...-->
                            <xsl:value-of select="saldoactual"/>
                            <!--Y extraemos la moneda...-->
                             <xsl:value-of select="saldoactual/@moneda"/>
                        </saldoactual>
                    </cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos></fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Que genera el resultado siguiente:

.. code-block:: xml
    
    <datos>
      <cuentas>
        <cuenta dnititular="5671001D">
          <creacion>13-abril-2012</creacion>
          <titular>Ramon Perez</titular>
          <saldoactual>12000euros</saldoactual>
        </cuenta>
        <cuenta dnititular="39812341C">
          <creacion>15-febrero-2011</creacion>
          <titular>Carmen Diaz</titular>
          <saldoactual>1900euros</saldoactual>
        </cuenta>
      </cuentas>
      <fondos/>
    </datos>



Con esto, la parte de las ``cuentas`` ya está hecha. Ahora queda lo siguiente

1. Hacer un elemento ``fondos`` con un bucle que vaya generando elementos ``fondo``.
2. Poner en el ``fondo`` el atributo ``cuentaasociada``.
3. Crear el elemento ``cantidaddepositada``.
4. Crear el elemento moneda.

Vamos con el paso 1 *"crear el elemento fondos"*

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                        <!--Creamos el elemento "creación" que en
                        realidad contiene el texto del elemento
                        "fechacreación" original-->
                        <creacion>
                            <xsl:value-of select="fechacreacion"/>
                        </creacion>
                        <!--Creamos el elemento titular y metemos
                        dentro del valor original del titular-->
                        <titular>
                            <xsl:value-of select="titular"/>
                        </titular>
                        <!--Creamos el saldo actual-->
                        <saldoactual>
                            <!--Y metemos dentro la cantidad que tuviese
                            el fichero original...-->
                            <xsl:value-of select="saldoactual"/>
                            <!--Y extraemos la moneda...-->
                             <xsl:value-of select="saldoactual/@moneda"/>
                        </saldoactual>
                    </cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos>
                <xsl:for-each select="listado/fondo">
                    <!--Paso 1: crear un fondo por cada fondo original-->
                    <fondo>
                        
                    </fondo>
                </xsl:for-each>
            </fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>


Ahora el paso 2: *poner el atributo "cuentaasociada"*. El XSLT sería así:

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                        <!--Creamos el elemento "creación" que en
                        realidad contiene el texto del elemento
                        "fechacreación" original-->
                        <creacion>
                            <xsl:value-of select="fechacreacion"/>
                        </creacion>
                        <!--Creamos el elemento titular y metemos
                        dentro del valor original del titular-->
                        <titular>
                            <xsl:value-of select="titular"/>
                        </titular>
                        <!--Creamos el saldo actual-->
                        <saldoactual>
                            <!--Y metemos dentro la cantidad que tuviese
                            el fichero original...-->
                            <xsl:value-of select="saldoactual"/>
                            <!--Y extraemos la moneda...-->
                             <xsl:value-of select="saldoactual/@moneda"/>
                        </saldoactual>
                    </cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos>
                <xsl:for-each select="listado/fondo">
                    <!--Paso 1: crear un fondo por cada fondo original-->
                    <fondo>
                        <!--Paso 2, crear el atributo cuentaasociada-->
                        <xsl:attribute name="cuentaasociada">
                            <xsl:value-of select="cuentaasociada"/>
                        </xsl:attribute>
                        
                    </fondo>
                </xsl:for-each>
            </fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Con el XSLT siguiente conseguimos el paso 3: *"crear el elemento cantidaddepositada"*

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                        <!--Creamos el elemento "creación" que en
                        realidad contiene el texto del elemento
                        "fechacreación" original-->
                        <creacion>
                            <xsl:value-of select="fechacreacion"/>
                        </creacion>
                        <!--Creamos el elemento titular y metemos
                        dentro del valor original del titular-->
                        <titular>
                            <xsl:value-of select="titular"/>
                        </titular>
                        <!--Creamos el saldo actual-->
                        <saldoactual>
                            <!--Y metemos dentro la cantidad que tuviese
                            el fichero original...-->
                            <xsl:value-of select="saldoactual"/>
                            <!--Y extraemos la moneda...-->
                             <xsl:value-of select="saldoactual/@moneda"/>
                        </saldoactual>
                    </cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos>
                <xsl:for-each select="listado/fondo">
                    <!--Paso 1: crear un fondo por cada fondo original-->
                    <fondo>
                        <!--Paso 2, crear el atributo cuentaasociada-->
                        <xsl:attribute name="cuentaasociada">
                            <xsl:value-of select="cuentaasociada"/>
                        </xsl:attribute>
                        <!--Paso 3, crear el elemento cantidaddepositada-->
                        <cantidaddepositada>
                            <xsl:value-of select="datos/cantidaddepositada"/>
                        </cantidaddepositada>
                    </fondo>
                </xsl:for-each>
            </fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Y por último el paso 4 "crear el elemento moneda". El XSLT sería algo así:

.. code-block:: xml

    <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <datos>
            <cuentas>
                <xsl:for-each select="listado/cuenta">
                    <cuenta>
                        <xsl:attribute name="dnititular">
                            <xsl:value-of select="titular/@dni"/>
                        </xsl:attribute>
                        <!--Creamos el elemento "creación" que en
                        realidad contiene el texto del elemento
                        "fechacreación" original-->
                        <creacion>
                            <xsl:value-of select="fechacreacion"/>
                        </creacion>
                        <!--Creamos el elemento titular y metemos
                        dentro del valor original del titular-->
                        <titular>
                            <xsl:value-of select="titular"/>
                        </titular>
                        <!--Creamos el saldo actual-->
                        <saldoactual>
                            <!--Y metemos dentro la cantidad que tuviese
                            el fichero original...-->
                            <xsl:value-of select="saldoactual"/>
                            <!--Y extraemos la moneda...-->
                             <xsl:value-of select="saldoactual/@moneda"/>
                        </saldoactual>
                    </cuenta>
                </xsl:for-each>
            </cuentas>
            <fondos>
                <xsl:for-each select="listado/fondo">
                    <!--Paso 1: crear un fondo por cada fondo original-->
                    <fondo>
                        <!--Paso 2, crear el atributo cuentaasociada-->
                        <xsl:attribute name="cuentaasociada">
                            <xsl:value-of select="cuentaasociada"/>
                        </xsl:attribute>
                        <!--Paso 3, crear el elemento cantidaddepositada-->
                        <cantidaddepositada>
                            <xsl:value-of select="datos/cantidaddepositada"/>
                        </cantidaddepositada>
                        <!--Paso 4:Crear el elemento moneda-->
                        <moneda>
                            <xsl:value-of select="datos/moneda"/>
                        </moneda>
                    </fondo>
                </xsl:for-each>
            </fondos>
        </datos>
    </xsl:template>
    </xsl:stylesheet>
    
Si probamos el XSLT anterior veremos que efectivamente conseguimos transformar el fichero original en el fichero resultado que nos piden, que es el siguiente:

.. code-block:: xml

    <datos>
      <cuentas>
        <cuenta dnititular="5671001D">
          <creacion>13-abril-2012</creacion>
          <titular>Ramon Perez</titular>
          <saldoactual>12000euros</saldoactual>
        </cuenta>
        <cuenta dnititular="39812341C">
          <creacion>15-febrero-2011</creacion>
          <titular>Carmen Diaz</titular>
          <saldoactual>1900euros</saldoactual>
        </cuenta>
      </cuentas>
      <fondos>
        <fondo cuentaasociada="20-A">
          <cantidaddepositada>20000</cantidaddepositada>
          <moneda>Euros</moneda>
        </fondo>
        <fondo cuentaasociada="21-DX">
          <cantidaddepositada>4800</cantidaddepositada>
          <moneda>Dolares</moneda>
        </fondo>
      </fondos>
    </datos>
