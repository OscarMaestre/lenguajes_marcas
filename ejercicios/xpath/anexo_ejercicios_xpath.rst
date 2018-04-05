Anexo: Ejercicios de XPath
==============================

En los ejercicios siguientes se asume que se va a utilizar el fichero siguiente:


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


Resolver los siguientes problemas usando expresiones XPath. Si no nos dicen nada se puede asumir que las etiquetas no deben incluirse.

* Extraer todos los elementos peso (etiqueta incluida).
* Extraer las cantidades de todos los elementos peso (sin la etiqueta <peso>).
* Extraer el peso del ultimo elemento.
* Extraer las distintas unidades en las que se han almacenado los pesos.
* Extraer el penúltimo codigo.
* Extraer el peso del elemento cuyo codigo sea AAA-111.
* Extraer el nombre de los productos que hayan puesto el peso en gramos.
* Extraer el codigo de los productos cuyo nombre sea "Monitor".
* Extraer el nombre los productos que pesen exactamente 50 gramos.

Soluciones
-------------


Para el enunciado  *Extraer todos los elementos peso (etiqueta incluida)* . La solución sería algo como esto ``/inventario/producto/peso`` . De hecho nos devuelve esto:

.. code-block:: xml
    
    <peso unidad="g">480</peso>
    <peso unidad="kg">1.8</peso>
    <peso unidad="g">50</peso>

Enunciado: *Extraer las cantidades de todos los elementos peso (sin la etiqueta <peso>)*. La solución sería ``/inventario/producto/peso/text()``. La expresión devuelve

.. code-block:: html

    480
    1.8
    50



Enunciado:*Extraer el peso del ultimo producto.*. Una posible solución **equivocada** sería esta ``/inventario/producto/peso[last()]``, que en realidad recupera "el último peso de cada producto", es decir recupera muchos, como muestra el resultado siguiente:

.. code-block:: xml

    <peso unidad="g">480</peso>
    <peso unidad="kg">1.8</peso>
    <peso unidad="g">50</peso>
    
La expresión correcta sería ``/inventario/producto[last()]/peso`` que devuelve esto

.. code-block:: xml

    <peso unidad="g">50</peso>
        
        
Enunciado: *Extraer las distintas unidades en las que se han almacenado los pesos*. Una posible solución sería esta ``/inventario/producto/peso/@unidad``, que devuelve esto:

.. code-block:: html

    g
    kg
    g

Enunciado: *Extraer el penúltimo codigo.*. Una posible solucion sería esta:``/inventario/producto[last()-1]/@codigo``


Enunciado: *Extraer el peso del elemento cuyo codigo sea AAA-111.* ``/inventario/producto[@codigo="AAA-111"]/peso``

Esto devuelve como resultado:

.. code-block:: xml

    <peso unidad="g">480</peso>

Enunciado: *Extraer el nombre de los productos que hayan puesto el peso en gramos.*


Una idea incorrecta sería esta ``/inventario/producto/peso[@unidad="g"]``.
Esta está mal, porque recupera "pesos" en lugar de "nombres" . De hecho recupera esto:

.. code-block:: xml

    <peso unidad="g">480</peso>
    <peso unidad="g">50</peso>
    

La correcta sería

``/inventario/producto[peso/@unidad="g"]/nombre``

Esto devuelve

.. code-block:: xml
    
    <nombre>Teclado</nombre>
    <nombre>Raton</nombre>







        
















