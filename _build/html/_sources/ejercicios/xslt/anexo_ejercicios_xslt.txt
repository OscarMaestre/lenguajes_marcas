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

2. Mostrar en un HTML la lista de los autores ordenada por orden alfabético inverso.


.. code-block:: xml

  <xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/">
      <html>
        <head><title>Resultado</title></head>
        <body>
          <xsl:for-each select="catalogo/libro">
            <xsl:variable name="contador" select='0'/>
            <xsl:for-each select="autores/autor">
              <xsl:if test="@nacimiento &gt; 1900">
              </xsl:if>
            </xsl:for-each>
            
          </xsl:for-each>
        </body>
      </html>
    </xsl:template>
  </xsl:stylesheet>
