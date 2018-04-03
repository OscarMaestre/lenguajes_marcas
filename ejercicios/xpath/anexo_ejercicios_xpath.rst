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
* Extraer el nombre de los productos que hayan pueso el peso en gramos.
* Extraer el codigo de los productos cuyo nombre sea "Monitor".
* Extraer el nombre los productos que pesen exactamente 50 gramos.