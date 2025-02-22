Anexo: Ejercicios DTDs
--------------------------------------------------------------------------------


Peso simple
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crear una DTD que compruebe simplemente que el elemento raíz es peso y con un atributo "unidad" (el atributo es obligatorio). Es decir, la DTD debería validar este fichero:

.. code-block:: xml

    <peso unidad="kg">20</peso>

La solución puede ser algo así:

.. code-block:: dtd

    <!ELEMENT peso  (#PCDATA)>
    <!ATTLIST peso unidad CDATA #REQUIRED>

Lista de productos
--------------------------------------------------------------------------------

Se desea controlar un formato como el siguiente:

* El elemento raíz se llama "listaarticulos".
* El elemento raíz puede llevar un atributo fecha.
* Dentro de listaarticulos hay 0 o muchos articulos.
* Todo artículo debe llevar un atributo id.
* Los artículos no se desglosan más, solo son texto.


Comprobar con un fichero como el siguiente:

.. code-block:: xml

    <listaarticulos fecha="29-01-2021">
        <articulo id="00A"> PC    </articulo>
        <articulo id="00A"> Ratón </articulo>
    </listaarticulos>

Catálogo de productos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En una empresa desean almacenar su catálogo de productos en XML. Se ha definido este fichero canónico.

.. code-block::

    <catalogo>
        <!--El catalogo lleva uno o más elementos producto-->
        <producto> <!--Producto puede tener un atributo codigo-->
            <nombre>Caja con autocierre</nombre>
            <!--La descripción es optativa-->
            <descripcion>Caja de seguridad...</descripcion>
        </producto>
        <producto codigo="jjjjj">
            <nombre>Caja llaves</nombre>
        </producto>
    </catalogo>


La solución:

.. code-block:: dtd

    <!ELEMENT catalogo    (producto)+>
    <!ELEMENT producto    (nombre, descripcion?)>
    <!ATTLIST producto    codigo CDATA #IMPLIED>
    <!ELEMENT nombre      (#PCDATA)>
    <!ELEMENT descripcion (#PCDATA)>

Catalogo (versión v2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En una empresa desean almacenar su catálogo de productos en XML. Se ha definido este fichero canónico.

.. code-block::

    <catalogo>
        <!--El catalogo lleva uno o más elementos producto-->
        <producto> <!--Producto puede tener un atributo codigo-->
            <nombre>Caja con autocierre</nombre>
            <!--La descripción es optativa-->
            <descripcion>Caja de seguridad...</descripcion>
            <origen>Alemania</origen>
        </producto>
        <producto aaabbbccc="jjjjj">
            <nombre>Caja llaves</nombre>
            <!-- Despues de la descripcion debe haber
            uno de estos dos elementos :
              a) origen
              b) pais -->
            <pais>Francia</pais>
        </producto>
    </catalogo>

Solución:

.. code-block:: dtd

    <!ELEMENT catalogo     (producto)+>
    <!ELEMENT producto     (nombre, descripcion?, (origen|pais))>
    <!ATTLIST producto     codigo CDATA #IMPLIED>
    <!ELEMENT nombre       (#PCDATA)>
    <!ELEMENT descripcion  (#PCDATA)>
    <!ELEMENT origen       (#PCDATA)>
    <!ELEMENT pais         (#PCDATA)>
