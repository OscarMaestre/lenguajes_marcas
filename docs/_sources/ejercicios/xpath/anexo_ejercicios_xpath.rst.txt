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
* Extraer el código de los productos que pesen más de un cuarto de kilo.

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
    

Una correcta sería

``/inventario/producto[peso/@unidad="g"]/nombre``


Y otra posibilidad sería

``/inventario/producto[peso[@unidad="g"]]/nombre``

Que literalmente pone *"extraer el nombre de productos que cumplan la condicion de tener un hijo peso y a su vez ese hijo peso cumpla la condición de tener un atributo unidad con el valor g"*

Esto devuelve

.. code-block:: xml
    
    <nombre>Teclado</nombre>
    <nombre>Raton</nombre>

Enunciado: *Extraer el codigo de los productos cuyo nombre sea "Monitor"*

Una posible solución sería

``/inventario/producto[nombre/text()="Monitor"]/@codigo``


Aunque en realidad también serviría lo siguiente:

``/inventario/producto[nombre="Monitor"]/@codigo``

La clave es que **como el elemento nombre no tiene hijos entonces se permite comparar el elemento como una cadena**. El evaluador XPath sobreentiende que queremos comparar "el contenido del elemento nombre" con la cadena "Monitor".



Enunciado: *Extraer el código de los productos que pesen más de un cuarto de kilo.*.

La solución sería

``/inventario/producto[
(peso/@unidad="g" and peso/text()>"250")
or
(peso/@unidad="kg" and peso/text()>"0.25") 
]/@codigo`` 


Información bancaria
-------------------------
Dado el siguiente fichero XML, contestar a las preguntas que se enuncian más abajo usando XPath.

.. code-block:: xml
    
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


Consulta: "cantidad depositada"
-------------------------------------

*Extraer la cantidad depositada en la cuenta 20-A*


* ``/listado/fondo`` nos devolvería todos los elementos ``fondo``
* ``/listado/fondo/datos`` nos devolvería todos los elementos ``datos`` que sean hijos de ``fondo`` los cuales a su vez deben ir dentro de ``inventario``.
Como nos piden una cantidad el último elemento XPath debe ser forzosamente ``cantidad``. Como nos ponen una condición tendremos que usar corchetes. El elemento ``cuentaasociada`` es hijo de ``fondo`` así que una buena posibilidad sería poner la condicion con el elemento fondo, así tendríamos que
* Si añadimos la condición parece entonces que una buena posibilidad sería algo como esto::

    /listado/fondo[cuentaasociada = "20-A"]/datos/cantidaddepositada
    
Si realmenten nos piden la cantidad sin etiquetas podemos añadir al final ``/text()`` y dejarlo así::

    /listado/fondo[cuentaasociada = "20-A"]/datos/cantidaddepositada/text()




Consulta: "monedas usadas"
--------------------------------

*Extraer un listado sin etiquetas de todas las monedas usadas por los distintos fondos*

La consulta sería simplemente::

    /listado/fondo/datos/moneda/text()


Consulta: "dnis con dólares"
-----------------------------
*Extraer el DNI de las cuentas que usen dolares como moneda de base*

En las cuentas la moneda es un atributo de ``saldoactual``, por lo que la condición debería ser::

    ...[@moneda="dolares"]...
    
Como nos piden el DNI  este debe ser el campo que debe aparecer al final del XPath. Aparte de eso el DNI es un atributo de ``titular``, por lo que la consulta debería ser algo así::

    ...[@moneda="dolares"]... /@dni
    
Como el ``dni`` es un atributo de ``titular`` y ``moneda`` es un atributo de ``saldoactual`` una buena posibilidad es mover la condición al elemento padre ``cuenta`` y hacer algo así::

    /listado/cuenta[saldoactual/@moneda = "dolares"]/titular/@dni
    
Obsérvese que para el ejemplo dado **no hay ningún resultado** (de hecho el evaluador dará error porque nadie cumple la condición). Si se desea comprobar que el XPath está bien se invita al lector a añadir datos al conjunto para verificar que la expresión XPath funciona correctamente.
    
Consulta: "fondos con menos de 2500 euros"
-----------------------------------------------

*Extraer toda la información de los fondos que usen "euros" por un valor inferior a 2500*

Por el texto del enunciado es evidente que el último elemento del XPath debe ser ``fondo``, por lo que de momento podemos saber que la expresión tendría este aspecto::

    .../fondo
    
También es evidente que hay una condición de filtrado. Esta condición tiene dos partes:

* Por un lado la divisa debe ser "Dolares". La divisa va dentro del elemento ``moneda`` que es hijo de ``datos`` que a su vez es hijo de ``fondo``
* Por otro lado la cantidad debe ser inferior a 2500. Esta información está en ``cantidaddepositada``.
* Para este caso necesitamos que se cumplan ambas condiciones por lo que deberemos usar ``AND``

Una posible consulta que resuelve esto es::

    /listado/fondo[datos/cantidaddepositada<2500 and datos/moneda = "Dolares"]
    
De nuevo nos encontramos con que el programa puede dar une rror, lo que tiene todo el sentido del mundo, ya que le pedimos que extraiga datos de algo que no existe.

