Anexo: Ejercicios de XQuery
==============================

En los ejercicios siguientes se asume que se va a utilizar la siguiente base de datos XML (tomada del libro de C.J. Date "Sistemas Gestores de Bases de Datos")


.. literalinclude:: bd.xml
   :language: xml


A continuación se muestra la estructura en forma de tabla de los elementos XML de dicho archivo. Obsérvese que los atributos llevan la arroba delante y que no se han puesto todas las filas:


Tabla proveedores

+----------+----------+--------+------------+
| @numprov | nombre   | estado | ciudad     |
+==========+==========+========+============+
|  v1      | Smith    |  20    | Londres    |
+----------+----------+--------+------------+
|  v2      | Jones    |  10    | Paris      |
+----------+----------+--------+------------+

Tabla partes:

+----------+-------------+-------+------+--------+
|@numparte | nombreparte | color | peso | ciudad |
+==========+=============+=======+======+========+
|   p1     | Tuerca      | Rojo  |  12  | Londres|
+----------+-------------+-------+------+--------+
|   p2     | Perno       | Verde |  17  | Paris  |
+----------+-------------+-------+------+--------+


Tabla proyectos

+----------------+----------------+--------+
|  @numproyecto  | nombreproyecto | ciudad |
+================+================+========+
|  y1            | Clasificador   | Paris  |
+----------------+----------------+--------+
|  y2            | Monitor        | Roma   |
+----------------+----------------+--------+

Tabla suministra

+---------+----------+-------------+----------+
| numprov | numparte | numproyecto | cantidad |
+=========+==========+=============+==========+
|  v1     |    p1    |    y1       | 200      |
+---------+----------+-------------+----------+
|  v1     |    p1    |    y4       | 700      |
+---------+----------+-------------+----------+

Obsérvese también que:

* En la tabla ``suministra`` el campo ``numprov`` es el mismo que el campo ``numprov`` de la tabla ``proveedor``
* En la tabla ``suministra`` el campo ``numparte`` es el mismo que el campo ``numparte`` de la tabla ``partes``
* En la tabla ``suministra`` el campo ``numproyecto`` es el mismo que el campo ``numproyecto`` de la tabla ``proyectos``


Consulta: ciudad de los proveedores
-------------------------------------

Extraer la ciudad de los proveedores (no debe aparecer la etiqueta) que tengan un estado mayor de 15.

.. code-block:: php

    for $proveedor in doc("datos.xml")/datos/proveedores/proveedor
    where $proveedor/estado > 15
    return $proveedor/ciudad/text()
    
Si se ejecuta esto se verá que el resultado es correcto sin embargo la presentación no es muy buena, al mostrarse todo seguido. Usemos por ejemplo la función ``concat`` para que cada resultado lleve un espacio detrás:

.. code-block:: php

    for $proveedor in doc("datos.xml")/datos/proveedores/proveedor
    where $proveedor/estado > 15
    return concat($proveedor/ciudad/text(), ' ')
    
    
Consulta: filas de la tabla partes
-----------------------------------

Averiguar cuantas partes existen, es decir, el total de filas de la "tabla" partes.

Para resolverlo una tentación muy común es resolverlo así:

.. code-block:: php

    for $partes in doc("datos.xml")/datos/partes
    return count ($partes/parte)

Y aunque esta solución funciona **en realidad estamos haciendo un bucle de una sola iteración**.

En este caso, se puede recurrir directamente a la función ``count`` que permite contar el número de elementos de una consulta parcial sin tener que hacer siquiera el recorrido.

.. code-block:: php

    count (doc("datos.xml")/datos/partes/parte)
    
    
Consulta con join's
----------------------


Obtener el nombre de los proyectos cuya ciudad sea Paris y que reciban una cantidad de partes > 350

Paso 0: análisis
------------------

La cantidad está en las filas (elementos XML) ``suministra`` pero el ``nombreproyecto`` está en las filas ``proyecto``. Será necesario "cruzar" elementos ``proyecto`` con elementos ``suministra`` usando como condición que ``@numproyecto`` de los elementos ``proyecto`` sea igual a los campos ``numproyecto`` de los elementos ``suministra``

Paso 1: hacemos el cruce
---------------------------
Una primera aproximación sería esta:

.. code-block::

   for $suministra in
     doc("datos.xml")/datos/suministros/suministra
   for $proyecto in
     doc("datos.xml")/datos/proyectos/proyecto
   where $suministra/numproyecto = $proyecto/@numproyecto
   
   return $proyecto/nombreproyecto
   
Sin embargo, esto devuelve "todos los proyectos" que de alguna manera aparezcan en la tabla ``suministra``
   
   
   
Paso 2: añadir condiciones
----------------------------
Nos han dicho que la cantidad de la tabla ``suministra`` debe ser mayor de 350, así que en el where o en el for de ``suministra`` podemos añadir una condición de filtrado:

Asimismo necesitamos solamente los proyectos cuyo campo ``ciudad`` sea Paris.

.. code-block::

   for $suministra in
     doc("datos.xml")/datos/suministros/suministra[cantidad>350]
   for $proyecto in
     doc("datos.xml")/datos/proyectos/proyecto[ciudad="Paris"]
   where $suministra/numproyecto = $proyecto/@numproyecto   
   
   return $proyecto/nombreproyecto
   
   
Otra variante usando condiciones en el ``where`` sería esta:

.. code-block::

   for $suministra in
     doc("datos.xml")/datos/suministros/suministra
   for $proyecto in
     doc("datos.xml")/datos/proyectos/proyecto
   where $suministra/numproyecto = $proyecto/@numproyecto   
      and
        $suministra/cantidad > 350
      and
        $proyecto/ciudad="Paris"
   return $proyecto/nombreproyecto
   
   
   
Consulta: ciudades iguales
---------------------------------------
Obtener los nombres de proyecto y nombres de parte que estén en la misma ciudad.

.. code-block:: php

    for $proyecto in
        doc("datos.xml")/datos/proyectos/proyecto
        for $parte in
            doc("datos.xml")/datos/partes/parte
            where
                $parte/ciudad = $proyecto/ciudad
        return concat(
            $parte/nombreparte, " en la misma ciudad que ",
            $proyecto/nombreproyecto, "-----"
        )
        
        
Consulta: partes con colores iguales
----------------------------------------
Obtener parejas de partes que tengan el mismo color (indicando el nombre de ambas partes y el color que comparten)

.. code-block:: php

    for $p1 in
        doc("datos.xml")/datos/partes/parte
    for $p2 in
        doc("datos.xml")/datos/partes/parte
        where
            $p1/color = $p2/color
        return concat ($p1/nombreparte,
                       " tiene el mismo color que ",
                       $p2/nombreparte,
                       " en concreto el color es:",
                       $p1/color, "
                       ")

Esta consulta funciona, pero ofrece parejas de partes que no tienen mucho sentido en pantalla, por ejemplo "Tuerca es igual que Tuerca". Para mejorar la consulta, vamos a eliminar parejas en la cuales el ``numparte`` sea el mismo, es decir no vamos a contemplar el emparejar una parte consigo misma.


.. code-block:: php

    for $p1 in
        doc("datos.xml")/datos/partes/parte
    for $p2 in
        doc("datos.xml")/datos/partes/parte
    where
        $p1/color = $p2/color
    and
        $p1/@numparte != $p2/@numparte
    return concat ($p1/nombreparte,
                       " tiene el mismo color que ",
                       $p2/nombreparte,
                       " en concreto el color es:",
                       $p1/color, "
                       ")
        







Consulta: cantidad de partes de Londres
------------------------------------------

Averiguar cuantas partes existen cuya ciudad sea "Londres", es decir, el total de filas de la "tabla" partes pero teniendo en cuenta la condición de que el "campo" ciudad debe ser Londres.

.. code-block:: php

    count (doc("datos.xml")/datos/partes/parte[ciudad='Londres'])
    


Consulta: media de partes rojas
----------------------------------

Crear una consulta XQuery que averigüe la media de partes suministradas cuyo color sea 'Rojo'

Paso 1: cruce de tablas
~~~~~~~~~~~~~~~~~~~~~~~~~~

Paso 2: añadir condicion de filtrado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Paso 3: calcular la media
~~~~~~~~~~~~~~~~~~~~~~~~~~

Comprobación
~~~~~~~~~~~~~~~~

Si analizamos la tabla partes veremos que las únicas partes cuyo color es 'Rojo' son las partes ``p1``, ``p4`` y ``p6``.
Esto significa que las unicas filas de ``suministra`` que nos interesan son estas:




+---------+----------+-------------+----------+
| numprov | numparte | numproyecto | cantidad |
+=========+==========+=============+==========+
|  v1     |    p1    |    y1       | 200      |
+---------+----------+-------------+----------+
|  v1     |    p1    |    y4       | 700      |
+---------+----------+-------------+----------+
|  v3     |    p4    |    y2       | 500      |
+---------+----------+-------------+----------+
|  v4     |    p6    |    y3       | 300      |
+---------+----------+-------------+----------+
|  v4     |    p6    |    y7       | 300      |
+---------+----------+-------------+----------+
|  v5     |    p6    |    y2       | 200      |
+---------+----------+-------------+----------+
|  v5     |    p1    |    y4       | 100      |
+---------+----------+-------------+----------+
|  v5     |    p4    |    y4       | 800      |
+---------+----------+-------------+----------+
|  v5     |    p6    |    y4       | 500      |
+---------+----------+-------------+----------+

Como vemos hay 9 filas con suministros de partes cuyo color es 'Rojo' y la suma de cantidades es 3600 por lo el resultado correcto es 400


    
Consulta: media de suministros
---------------------------------

Averiguar la media de la cantidad de partes que aparecen en la "tabla" suministra

.. code-block:: php

    avg (doc("datos.xml")/datos/suministros/suministra/cantidad)
    
Pregunta: ¿por qué no ponemos esta solución?

.. code-block:: php

    avg (doc("datos.xml")/datos/suministros/suministra/cantidad/text())
    
    
Respuesta: las funciones son capaces de "extraer el texto automáticamente" si en el elemento no hay hijos. En este caso, la cantidad no tiene hijos, por lo que podemos ahorrarnos el ``text()``

Consulta: media por proveedor
-----------------------------
Averiguar la media de cantidades por proveedor usando los datos de la tabla suministra.

Hagamos esta consulta por partes. En primer lugar, saquemos los distintos proveedores que hay en suministra

.. code-block:: php

    for $n in distinct-values(
    doc("datos.xml")/datos/
    proveedores/proveedor/@numprov)
    return $n
    
    
Ahora, teniendo los distintos proveedores podemos devolver algo distinto de ``numprov``. Podemos devolver la media para ese proveedor aprovechando los filtrados XPath.

.. code-block:: php

    for $n in distinct-values(
    doc("datos.xml")/datos/
    proveedores/proveedor/@numprov)
    return avg
    ( doc("datos.xml")/datos/suministros/suministra
    [numprov=$n]/cantidad)

Y por último, si usamos ``concat`` apropiadamente podemos hacer que aparezca el número de proveedor al lado de dica cantidad.

.. code-block:: php

    for $n in distinct-values(
    doc("datos.xml")/datos/proveedores/proveedor/@numprov)
    return concat (
     $n, ' ', avg(
     doc("datos.xml")/datos/suministros
    /suministra[numprov=$n]/cantidad)
    )

Consulta: suministros en grandes cantidades
--------------------------------------------
Averiguar el nombre de los proyectos (sin que haya repeticiones) que reciban una cantidad en la tabla suministra mayor de 650.

.. code-block:: php
    
    for $proyecto
    in doc("datos.xml")/datos/proyectos/proyecto
    for $suministra
    in
    doc("datos.xml")/datos/suministros/suministra[cantidad>650]
    where $proyecto/@numproyecto = $suministra/numproyecto
    return ($proyecto/nombreproyecto, $suministra/cantidad)