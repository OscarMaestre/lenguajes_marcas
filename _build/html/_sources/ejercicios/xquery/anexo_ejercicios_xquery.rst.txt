Anexo: Ejercicios de XQuery
==============================

En los ejercicios siguientes se asume que se va a utilizar la siguiente base de datos XML (tomada del libro de C.J. Date "Sistemas Gestores de Bases de Datos")


.. literalinclude:: bd.xml
   :language: xml
   

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
    
Consulta: cantidad de partes de Londres
------------------------------------------

Averiguar cuantas partes existen cuya ciudad sea "Londres", es decir, el total de filas de la "tabla" partes pero teniendo en cuenta la condición de que el "campo" ciudad debe ser Londres.

.. code-block:: php

    count (doc("datos.xml")/datos/partes/parte[ciudad='Londres'])
    
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