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
* Todo artículo debe llevar un atributo ID.
* Los artículos no se desglosan más, solo son texto.


Comprobar con un fichero como el siguiente:

.. code-block:: xml

    <listaarticulos fecha="29-01-2021">
        <articulo ID="00A"> PC    </articulo>
        <articulo ID="00A"> Ratón </articulo>
    </listaarticulos>
