===
XML
===

Introducción
============

Los lenguajes de marcas como HTML tienen una orientación muy clara: describir páginas web.

En un contexto distinto, muy a menudo ocurre que es muy difícil intercambiar datos entre programas.

XML es un conjunto de tecnologías orientadas a crear nuestros propios lenguajes de marcas. A estos lenguajes de marcas "propios" se les denomina "vocabularios".

Un ejemplo sencillo
===================

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre>AcerSA</nombre>
			<cif>5664332</cif>
		</cliente>
		<cliente>
			<nombre>Mer SL</nombre>
			<cif>5111444</cif>
		</cliente>
	</clientes>
	
	
	
Lo fundamental es que podemos crear nuestros propios "vocabularios" XML.


Construcción de XML
===================

Para crear XML es importante recordar una serie de reglas:

* XML es "case-sensitive", es decir que no es lo mismo mayúsculas que minúsculas y que por tanto no es lo mismo ``<cliente>``, que ``<Cliente>`` que ``<CLIENTE>``.

* Obligatorio: solo un elemento raíz.

* En general, la costumbre es poner todo en minúsculas.

* Solo se puede poner una etiqueta que empiece por letra o _. Es decir, esta etiqueta no funcionará en los programas ``<12Cliente>``.

* Aparte de eso, una etiqueta sí puede contener números, por lo que esta etiqueta sí es válida ``<Cliente12>``.

Validez
=======

Un documento XML puede "estar bien formado" o "ser válido". Se dice que un documento "está bien formado" cuando respeta las reglas XML básicas. Si alguien ha definido las reglas XML para un vocabulario, podremos además decir si el documento es válido o no, lo cual es mejor que simplemente estar bien formado.

Por ejemplo, los siguientes archivos ni siquiera están bien formados.

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre>AcerSA
			<CIF>5666333</CIF>
		</cliente>
	</clientes>
	
En este caso la etiqueta ``<nombre>`` no está cerrada.

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre>AcerSA</nombre>
			<cif>5666333</CIF>
		</cliente>
	</clientes>


En este caso, se ha puesto ``<cif>`` cerrado con ``</CIF>`` (mayúsculas).

.. code-block:: xml

	<clientes>
		<cliente>
			<nombre!>AcerSA</nombre!>
			<CIF>5666333</CIF>
		</cliente>
	</clientes>

Se ha utilizado la admiración, que no es válida.

Atención a este ejemplo:


.. code-block:: xml

	
	<cliente>
		<nombre>AcerSA</nombre>
		<CIF>5666333</CIF>
	</cliente>
	<cliente>
		<nombre>ACME</nombre>
		<CIF>455321</CIF>
	</cliente>
	
En este caso, el problema es que hay más de un elemento raíz.

En general, podemos asumir que un documento puede estar en uno de estos estados que de peor a mejor podríamos indicar así:

1. Mal formado (lo peor)
2. Bien formado.
3. Válido: está bien formado y además nos han dado las reglas para determinar si algo está bien o mal y el documento XML cumple dichas reglas. Este es el mejor caso.

Para determinar si un documento es válido o no, se puede usar el validador del W3C situado en http://validator.w3c.org

Gramáticas
==========

Pensemos en el siguiente problema, un programador crea aplicaciones con documentos que se almacenan así:

.. code-block:: xml

	<clientes>	
		<cliente>
			<nombre>AcerSA</nombre>
			<cif>455321</cif>
		</cliente>
		<cliente>
			<nombre>ACME</nombre>
			<cif>455321</cif>
		</cliente>
	</clientes>

	
Sin embargo, otro programador de la misma empresa lo hace así:



.. code-block:: xml

	<clientes>	
		<cliente>			
			<cif>455321</cif>
			<nombre>AcerSA</nombre>
		</cliente>
		<cliente>
			<cif>455321</cif>
			<nombre>ACME</nombre>
		</cliente>
	</clientes>

Está claro, que ninguno de los dos puede leer los archivos del otro, sería crítico ponerse de acuerdo en lo que se puede hacer, lo que puede aparecer y en qué orden debe hacerlo. Esto se hará mediante las DTD.

DTD significa Declaración de Tipo de Documento, y es un mecanismo para expresar las reglas sobre lo que se va a permitir y lo que no en archivos XML.

Por ejemplo, supongamos el mismo ejemplo ejemplo anterior en el que queremos formalizar lo que puede aparecer en un fichero de clientes. Se debe tener en cuenta que en un DTD se pueden indicar reglas para lo siguiente:

* Se puede indicar si un elemento aparece o no de forma opcional
* Se puede indicar si un elemento debe aparecer de forma obligatoria.
* Se puede indicar si algo aparecer una o muchas veces.
* Se puede indicar si algo aparece cero o muchas veces.


Supongamos que en nuestros ficheros deseamos indicar que el elemento raíz es ``<listaclientes>``. Dentro de ``<listaclientes>`` deseamos permitir uno o más elementos ``<cliente>``. Dentro de ``<cliente>`` todos deberán tener ``<cif>`` y ``<nombre>`` y en ese orden. Dentro de ``<cliente>`` puede aparecer o no un elemento ``<diasentrega>`` para indicar que ese cliente exige un máximo de plazos. Como no todo el mundo usa plazos el ``<diasentrega>`` es optativo.


Por ejemplo, este XML sí es válido:

.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<nombre>Mercasa</nombre>
		</cliente>
	</listaclientes>
	
Este también lo es:

.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<nombre>Mercasa</nombre>
			<diasentrega>30</diasentrega>
		</cliente>
	</listaclientes>
	
Este también:


.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<nombre>Mercasa</nombre>
			<diasentrega>30</diasentrega>
		</cliente>
		<cliente>
			<cif>5121554</cif>
			<nombre>Acer SL</nombre>
		</cliente>
	</listaclientes>

Sin embargo, estos no lo son:

.. code-block:: xml

	<listaclientes>
	</listaclientes>

Este archivo no tenía clientes (y era obligatorio al menos uno)

.. code-block:: xml

	<listaclientes>
		<cliente>
			<cif>5676443</cif>
			<diasentrega>30</diasentrega>
		</cliente>
	</listaclientes>

Este archivo no tiene nombre de cliente.

.. code-block:: xml

	<listaclientes>
		<cliente>
			<nombre>Mercasa</nombre>
			<cif>5676443</cif>
		</cliente>
		<cliente>
			<cif>5121554</cif>
			<nombre>Acer SL</nombre>
		</cliente>
	</listaclientes>

En este archivo no se respeta el orden cif, nombre.

Sintaxis DTD
----------------------------------------------

Una DTD es como un CSS, puede ir en el mismo archivo XML o puede ir en uno separado. Para poder subirlos al validador, meteremos la DTD junto con el XML.


La primera línea de todo XML debe ser esta:

.. code-block:: xml

	<?xml version="1.0"?>
	
	
Al final del XML pondremos los datos propiamente dichos

.. code-block:: xml

	<listaclientes>
		<cliente>
			<nombre>Mercasa</nombre>
			<cif>5676443</cif>
		</cliente>
		<cliente>
			<cif>5121554</cif>
			<nombre>Acer SL</nombre>
		</cliente>
	</listaclientes>

	
La DTD tiene esta estructura

.. code-block:: dtd

	<!DOCTYPE listaclientes [
			<!ELEMENT listaclientes (cliente+)>
			<!ELEMENT cliente (nombre, cif, diasentrega?)>
			<!ELEMENT nombre (#PCDATA)>
			<!ELEMENT cif (#PCDATA)>
			<!ELEMENT diasentrega (#PCDATA)>
			]
		>

Esto significa lo siguiente:

* Se establece el tipo de documento ``listaclientes`` que consta de una serie de elementos (dentro del corchete)
* Un elemento ``listaclientes	`` consta de uno o más clientes. El signo ``+`` significa "uno o más".
* Un cliente tiene un nombre y un cif. También puede tener un elemento ``diasentrega`` que puede o no aparecer (el signo ``?`` significa "0 o 1 veces").
* Un ``nombre`` no tiene más elementos dentro, solo caracteres (``#PCDATA``)
* Un ``CIF`` solo consta de caracteres.
* Un elemento ``diasentrega`` consta solo de caracteres.

La solución completa sería así:


.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE listaclientes [
			<!ELEMENT listaclientes (cliente+)>
			<!ELEMENT cliente (nombre, cif, diasentrega?)>
			<!ELEMENT nombre (#PCDATA)>
			<!ELEMENT cif (#PCDATA)>
			<!ELEMENT diasentrega (#PCDATA)>
		]>
	<listaclientes>
		<cliente>
			<nombre>Mercasa</nombre>
			<cif>5676443</cif>
		</cliente>
		<cliente>			
			<nombre>Acer SL</nombre>
			<cif>5121554</cif>
		</cliente>
	</listaclientes>
	
Ejercicio I (DTD)
===================================================
Unos programadores necesitan un formato de fichero para que sus distintos programas intercambien información sobre ventas. El acuerdo al que han llegado es que su XML debería tener esta estructura:

* El elemento raíz será ``<listaventas>``
* Toda ``<listaventas>`` tiene una o más ventas.
* Toda ``<venta>`` tiene los siguientes datos: 

	* Importe.	
	* Comprador.
	* Vendedor.
	* Fecha (optativa).
	* Un codigo de factura.


.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE listaventas[
	  <!ELEMENT listaventas (venta+)>
	  <!ELEMENT venta (importe, comprador, vendedor, fecha?, codigofactura)>
	  <!ELEMENT importe (#PCDATA)>
	  <!ELEMENT comprador (#PCDATA)>
	  <!ELEMENT vendedor (#PCDATA)>
	  <!ELEMENT fecha (#PCDATA)>
	  <!ELEMENT codigofactura (#PCDATA)>
	  
	]>

	<listaventas>
	  <venta>
		<importe>1500</importe>
		<comprador>Wile E.Coyote</comprador>
		<vendedor>ACME</vendedor>
		<codigofactura>E17</codigofactura>
	  </venta>
	  <venta>
		<importe>750</importe>
		<comprador>Elmer Fudd</comprador>
		<vendedor>ACME</vendedor>
		<fecha>27-2-2015</fecha>
		<codigofactura>E18</codigofactura>
	  </venta>
	</listaventas>   
	
Ejercicio II (DTD)
===========================================

Crear un XML de ejemplo y la DTD asociada para unos programadores que programan una aplicación de pedidos donde hay una lista de pedidos con 0 o más pedidos. Cada pedido tiene un número de serie, una cantidad y un peso que puede ser opcional.

Solución
----------------------------------------------
Este ejemplo es un documento XML válido.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listapedidos [
		<!ELEMENT listapedidos (pedido*)>
		<!ELEMENT pedido (numeroserie, cantidad, peso?)>
		<!ELEMENT numeroserie (#PCDATA)>
		<!ELEMENT cantidad (#PCDATA)>
		<!ELEMENT peso (#PCDATA)>
	]>

	<listapedidos>
	</listapedidos>




Este documento **no es válido**

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listapedidos [
		<!ELEMENT listapedidos (pedido*)>
		<!ELEMENT pedido (numeroserie, cantidad, peso?)>
		<!ELEMENT numeroserie (#PCDATA)>
		<!ELEMENT cantidad (#PCDATA)>
		<!ELEMENT peso (#PCDATA)>
	]>

	<listapedidos>
		<pedido>
			<numeroserie>23332244</numeroserie>
		</pedido>
	</listapedidos>
	

Este documento **sí es válido**. Las DTD solo se ocupan de determinar qué elementos hay y en qué orden, pero no se ocupan de lo que hay dentro de los elementos.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listapedidos [
		<!ELEMENT listapedidos (pedido*)>
		<!ELEMENT pedido (numeroserie, cantidad, peso?)>
		<!ELEMENT numeroserie (#PCDATA)>
		<!ELEMENT cantidad (#PCDATA)>
		<!ELEMENT peso (#PCDATA)>
	]>

	<listapedidos>
		<pedido>
			<numeroserie>23332244</numeroserie>
			<cantidad>ññlñ</cantidad>
		</pedido>
	</listapedidos>

Ejercicio (con atributos)
===========================

Unos programadores necesitan estructurar la información que intercambiarán los ficheros de sus aplicaciones para lo cual han determinado los requisitos siguientes:

* Los ficheros deben tener un elemento ``<listafacturas>``
* Dentro de la lista debe haber una o más facturas.
* Las facturas tienen un atributo ``fecha`` que es optativo.
* Toda factura tiene un ``emisor``, que es un elemento obligatorio y que debe tener un atributo ``cif`` que es obligatorio. Dentro de ``emisor`` debe haber un elemento ``nombre``, que es obligatorio y puede o no haber un elemento ``volumenventas``.
* Toda factura debe tener un elemento ``pagador``, el cual tiene exactamente la misma estructura que ``emisor``.
* Toda factura tiene un elemento ``importe``.

Solución ejercicio con atributos
------------------------------------------------------

La siguiente DTD refleja los requisitos indicados en el enunciado.

.. code-block:: dtd

	<!ELEMENT listafacturas (factura+)>
	<!ELEMENT factura (emisor, pagador, importe)>
	<!ATTLIST factura fecha CDATA #IMPLIED>
	<!ELEMENT emisor (nombre, volumenventas?)>
	<!ELEMENT nombre (#PCDATA)>
	<!ATTLIST emisor cif CDATA #REQUIRED>
	<!ELEMENT volumenventas (#PCDATA)>
	<!ELEMENT pagador (nombre, volumenventas?)>
	<!ATTLIST pagador cif CDATA #REQUIRED>
	<!ELEMENT importe (#PCDATA)>

Y el XML siguiente refleja un posible documento. Puede comprobarse que es válido con respecto a la DTD.

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE listafacturas SYSTEM "ListaFacturas.dtd">
	<listafacturas>
	  <factura fecha="11-2-2015">
		<emisor cif="123">
		  <nombre>ACME</nombre>
		</emisor>
		<pagador cif="234">
		  <nombre>ACME Inc</nombre>
		  <volumenventas>2000</volumenventas>
		</pagador>
		<importe>2500</importe>
	  </factura>
	</listafacturas>


Ejercicio
=========

Un instituto necesita registrar los cursos y alumnos que estudian en él y necesita una DTD para comprobar los documentos XML de los programas que utiliza:

* Tiene que haber un elemento raíz ``listacursos``. Tiene que haber uno o más cursos.
* Un curso tiene uno o más alumnos
* Todo alumno tiene un DNI, un nombre y un apellido, puede que tenga segundo apellido o no.
* Un alumno escoge una lista de asignaturas donde habrá una o más asignaturas. Toda asignatura tiene un nombre, un atributo código y un profesor.
* Un profesor tiene un NRP (Número de Registro Personal), un nombre y un apellido (también puede tener o no un segundo apellido).
	
	
Solución punto 1
----------------------------------------------

La raíz es ``listacursos`` y tiene uno o más cursos

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
	]>
	
Solución punto 2
----------------------------------------------
Un curso tiene uno o más elementos ``alumno``.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
	]>		

	
Solución punto 3
----------------------------------------------
Todo alumno tiene DNI, nombre y apellido 1, pero puede que tenga el segundo o no

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre, ap1, ap2?)>
	]>	
	
Solución al punto 4
----------------------------------------------
Todo alumno tiene una lista de asignaturas que consta de una o más asignaturas. Ampliamos el elemento alumno:

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)
	]>
	
	
Solución punto 5
----------------------------------------------
Una posible solución implicaría usar dos elementos ``nombre``. *Está permitido* pero solo si ambos elementos se usan de la misma forma (por ejemplo que usen ``(#PCDATA)``. Para evitar problemas cambiaremos algunos nombres de elementos.

Este punto pedía contemplar que una asignatura tiene un nombre, un código y un profesor.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre_alumno, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)>
		<!ELEMENT asignatura (nombre_asig, profesor)>
		<!ATTLIST asignatura codigo CDATA #REQUIRED>
		<!ELEMENT nombre_asig (#PCDATA)>
	]>	
	
	
Solución punto 6
----------------------------------------------
Se indica que un profesor tiene una serie de elementos dentro. Aquí hay un claro ejemplo en el que repetir el elemento ``ap1`` o el ``ap2`` hubiera sido apropiado, ya que los apellidos de alumnos o profesores en realidad no se distinguen en nada.


.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre_alumno, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)>
		<!ELEMENT asignatura (nombre_asig, profesor)>
		<!ATTLIST asignatura codigo CDATA #REQUIRED>
		<!ELEMENT nombre_asig (#PCDATA)>
		<!ELEMENT profesor (nrp, nombre_prof, ap_prof1, ap_prof2?)>
	]>
	
Solución completa
----------------------------------------------
.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>

	<!DOCTYPE listacursos [
		<!ELEMENT listacursos (curso+)>
		<!ELEMENT curso (alumno+)>
		<!ELEMENT alumno (dni, nombre_alumno, ap1, ap2?, listaasignaturas)>
		<!ELEMENT listaasignaturas (asignatura+)>
		<!ELEMENT asignatura (nombre_asig, profesor)>
		<!ATTLIST asignatura codigo CDATA #REQUIRED>
		<!ELEMENT nombre_asig (#PCDATA)>
		<!ELEMENT profesor (nrp, nombre_prof, ap_prof1, ap_prof2?)>
		
		<!ELEMENT dni (#PCDATA)>
		<!ELEMENT nombre_alumno (#PCDATA)>
		<!ELEMENT ap1 (#PCDATA)>
		<!ELEMENT ap2 (#PCDATA)>
		<!ELEMENT nrp (#PCDATA)>
		<!ELEMENT nombre_prof (#PCDATA)>
		<!ELEMENT ap_prof1 (#PCDATA)>
		<!ELEMENT ap_prof2 (#PCDATA)>
	]>


	<listacursos>
		<curso>
			<alumno>
				<dni>1234567</dni>
				<nombre_alumno>Juan</nombre_alumno>
				<ap1>Sanchez</ap1>
				<listaasignaturas>
					<asignatura>
						<nombre_asig>
						  Lenguajes de marcas
						</nombre_asig>
						<codigo>
						  XML-DAM1
						</codigo>
						<profesor>
							<nrp>
							  03409435898W0303
							</nrp>
							<nombre_prof>
							  Andres
							</nombre_prof>
							<ap_prof1>
							  Ruiz
							</ap_prof1>
						</profesor>
					</asignatura>
				</listaasignaturas>
			</alumno>
		</curso>
	</listacursos>

	
	




Otras características de XML
============================

Atributos
----------------------------------------------

Un atributo XML funciona exactamente igual que un atributo HTML, en concreto un atributo es un trozo de información que acompaña a la etiqueta, en lugar de ir dentro del elemento.

.. code-block:: xml

	<pedido codigo="20C">
		<contenido>
			...
	</pedido>
	
En este caso, la etiqueta ``pedido`` tiene un atributo ``codigo``.

¿Cuando debemos usar atributos y cuando debemos usar elementos? Resulta que el ejemplo anterior también se podría haber permitido hacerlo así:

.. code-block:: xml

	<pedido>
		<codigo>20C</codigo>
		<contenido>
			...
	</pedido>

Hay muchas discusiones sobre qué meter dentro de elemento o atributo. Sin embargo, los expertos coinciden en señalar que en caso de duda es mejor el segundo.

La definición de atributos se hace por medio de una directiva llamada ``ATTLIST``. En concreto si quisieramos permitir un atributo ``código`` en el elemento ``pedido`` se haría algo así.

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE pedido[
		<!ELEMENT pedido (contenido)>
		<!ELEMENT contenido (#PCDATA)>
		<!ATTLIST pedido codigo CDATA #REQUIRED>
	]>

	<pedido codigo="20C">
		<contenido>Pedido de cosas</contenido>
	</pedido>
		
En concreto este código pone que el elemento ``pedido`` tiene un atributo ``código`` con datos carácter dentro y que es obligatorio que esté presente (un atributo optativo en vez de ``#REQUIRED`` usará ``#IMPLIED``)

Si probamos esto, también validará porque el atributo es *optativo*

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE pedido[
		<!ELEMENT pedido (contenido)>
		<!ELEMENT contenido (#PCDATA)>
		<!ATTLIST pedido codigo CDATA #IMPLIED>
	]>

	<pedido>
		<contenido>Pedido de cosas</contenido>
	</pedido>





Elementos vacíos
----------------------------------------------

En ocasiones, un elemento en especial puede interesarnos que vaya vacío porque simplemente no contiene mucha información de relevancia. Por ejemplo en HTML podemos encontrarnos esto:

.. code-block:: html

	<b>Texto texto...</b>
	<br/>
	
Los elementos vacíos suelen utilizar para indicar pequeñas informaciones que no deseamos meter en atributos y que de todas formas tampoco son de demasiada relevancia.

Un elemento vacío se indica poniendo ``EMPTY`` en lugar de ``#PCDATA``

Por supuesto, estas dos formas de usar un atributo son válidas:

.. code-block:: xml

	<pedido>
		<pagado></pagado>
		<contenido>...</contenido>
	</pedido>
	
.. code-block:: xml

	<pedido>
		<pagado/>
		<contenido>...</contenido>
	</pedido>

	
La definición completa sería así:

.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE pedido[
		<!ELEMENT pedido (pagado?,contenido)>
		<!ELEMENT pagado EMPTY>
		<!ELEMENT contenido (#PCDATA)>
		<!ATTLIST pedido codigo CDATA #IMPLIED>
	]>

	<pedido>
		<pagado/>
		<contenido>Pedido de cosas</contenido>
	</pedido>
	
	
Alternativas
----------------------------------------------

Hasta ahora hemos indicado elementos donde un elemento puede aparecer o puede no aparecer, pero ¿qué ocurre si deseamos obligar a que aparezca una posibilidad entre varias?


Por ejemplo, supongamos que en un nuestro ejemplo de pedidos deseamos indicar si el pedido se entregó en almacén o a domicilio. A la fuerza todo pedido se entrega de alguna manera, sin embargo queremos exigir que en los XML aparezca una de esas dos alternativas. Los elementos alternativos se indican con la barra vertical ``almacen|domicilio``

Una tentación sería hacer esto (que está **mal**):

.. code-block:: xml

	<!DOCTYPE pedido[
		<!ELEMENT pedido (pagado?, contenido, almacen?,domicilio?)>
		<!ELEMENT pagado EMPTY>
		<!ELEMENT contenido (#PCDATA)>
		<!ELEMENT almacen (#PCDATA)>
		<!ELEMENT domicilio (#PCDATA>
	]>

Está mal porque se permite esto:

.. code-block:: xml

	<pedido>
		<pagado/>
		<contenido>Ordenadores</contenido>
		<almacen>Entregado el 20-2-2011</almacen>
		<domicilio>Entregado el 20-2011</domicilio>
	</pedido>
	
La forma **correcta** es esta:

.. code-block:: xml

	<!DOCTYPE pedido[
		<!ELEMENT pedido (pagado?, contenido, (almacen|domicilio)?>
		<!ELEMENT pagado EMPTY>
		<!ELEMENT contenido (#PCDATA)>
		<!ELEMENT almacen (#PCDATA)>
		<!ELEMENT domicilio (#PCDATA>
	]>
	<pedido>
		<contenido>Ordenadores</contenido>
	</pedido>
	
Ejercicio
===========================================

Un mayorista informático necesita especificar las reglas de los elementos permitidos en las aplicaciones que utiliza en sus empresas, para ello ha indicado los siguientes requisitos:

* Una entrega consta de uno o más lotes.
* Un lote tiene uno o más palés
* Todo palé tiene una serie de elementos: número de cajas, contenido y peso y forma de manipulación.
* El contenido consta de una serie de elementos: nombre del componente, procedencia (puede aparecer 0, 1 o más países), número de serie del componente, peso del componente individual y unidad de peso que puede aparecer o no.

Solución
----------------------------------------------

Observa como en la siguiente DTD se pone ``procedencia?`` y dentro de ella ``pais+``. Esto nos permite que si aparece la procedencia se debe especificar uno o más países. Sin embargo si no queremos que aparezca ningun pais, el XML **no necesita contener un elemento vacío**.

.. code-block:: dtd

	<!ELEMENT entrega (lote+)>
	<!ELEMENT lote (pale+)>
	<!ELEMENT pale (numcajas, contenido, peso, formamanipulacion?)>
	<!ELEMENT numcajas (#PCDATA)>
	<!ELEMENT peso (#PCDATA)>
	<!ELEMENT formamanipulacion (#PCDATA)>
	<!ELEMENT contenido (nombrecomponente, procedencia?, 
				numserie, peso, unidades)>
	<!ELEMENT nombrecomponente (#PCDATA)>
	<!ELEMENT procedencia (pais+)>
	<!ELEMENT pais (#PCDATA)>
	<!ELEMENT numserie (#PCDATA)>
	<!ELEMENT unidades (#PCDATA)>


.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE entrega SYSTEM "mayorista.dtd">
	<entrega>
	  <lote>
		<pale>
		  <numcajas>3</numcajas>
		  <contenido>
			<nombrecomponente>Fuentes</nombrecomponente>
			<numserie>3A</numserie>
			<peso>2kg</peso>
			<unidades>50</unidades>
		  </contenido>
		  <peso>100kg</peso>
		  <formamanipulacion>Manual</formamanipulacion>
		</pale>
	  </lote>
	  <lote>
		<pale>
		  <numcajas>2</numcajas>
		  <contenido>
			<nombrecomponente>CPUs</nombrecomponente>
			<procedencia>
			  <pais>China</pais>
			  <pais>Corea del Sur</pais>
			</procedencia>
			<numserie>5B</numserie>
			<peso>100g</peso>
			<unidades>1000</unidades>
		  </contenido>
		  <peso>100kg</peso>
		  <formamanipulacion>Manual</formamanipulacion>
		</pale>
	  </lote>
	</entrega>

Ejercicio: mayorista de libros
======================================
Se desea crear un formato de intercambio de datos para una empresa mayorista de libros con el fin de que sus distintos programas puedan manejar la información interna. El formato de archivo debe tener la siguiente estructura:

* Un archivo tiene una serie de operaciones dentro.
* Las operaciones pueden ser "venta", "compra", o cualquier combinación y secuencia de ellas, pero debe haber al menos una.
* Una venta tiene: 

	* Uno o más títulos vendidos.
	* La cantidad total de libros vendidos.
	* Puede haber un elemento "entregado" que indique si la entrega se ha realizado.
	* Debe haber un elemento importe con un atributo obligatorio llamado "moneda".
	
* Una compra tiene:

	* Uno o más títulos comprados.
	* Nombre de proveedor.
	* Una fecha de compra, que debe desglosarse en elementos día, mes y año

Solución al mayorista de libros
------------------------------------------------------


Ejercicio: fabricante de tractores
===========================================

Un fabricante de tractores desea unificar el formato XML de sus proveedores y para ello ha indicado que necesita que los archivos XML cumplan las siguientes restricciones:

* Un pedido consta de uno o más tractores.
* Un tractor consta de uno o más componentes.
* Un componente tiene los siguientes elementos: nombre del fabricante (atributo obligatorio), fecha de entrega  (si es posible, aunque puede que no aparezca, si aparece el dia es optativo, pero el mes y el año son obligatorios). También se necesita saber del componente si es frágil o no. También debe aparecer un elemento peso del componente y dicho elemento peso tiene un atributo unidad del peso (kilos o gramos), un elemento número de serie y puede que aparezca o no un elemento km_maximos indicando que el componente debe sustituirse tras un cierto número de kilómetros.

Una posible solución sería esta (aunque se puede mejorar en algunos aspectos):

.. code-block:: dtd

	<!ELEMENT pedido (tractor+)>
	<!ELEMENT tractor (componente+)>
	<!ELEMENT componente (fecha?, peso, fragil?, km_maximos?)>
	<!ELEMENT fragil EMPTY>
	<!ELEMENT peso (#PCDATA)>
	<!ELEMENT km_maximos (#PCDATA)>
	<!ATTLIST componente nombre_fabricante CDATA #REQUIRED>
	<!ATTLIST peso unidades CDATA #IMPLIED>
	<!ELEMENT fecha (dia?, mes, anio)>
	<!ELEMENT dia (#PCDATA)>
	<!ELEMENT mes (#PCDATA)>
	<!ELEMENT anio (#PCDATA)>   

Un ejemplo de XML sería este:

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE pedido SYSTEM "tractores.dtd">
	<pedido>
	  <tractor>
		<componente nombre_fabricante="John Deere">
		  <peso unidades="kilos">2.5</peso>
		  <fragil/>
		</componente>
		<componente nombre_fabricante="Agrotrans">
		  <peso unidades="gramos">50</peso>
		</componente>
	  </tractor>
	  <tractor>
		<componente nombre_fabricante="John Deere">
		  <fecha>
			<mes>Enero</mes>
			<anio>2015</anio>
		  </fecha>
		  <peso>150</peso>
		  <fragil/>
		</componente>
		<componente nombre_fabricante="Agrotrans">
		  <peso unidades="gramos">50</peso>
		</componente>
	  </tractor>
	</pedido> 

Ejercicio: repeticiones de opciones
===================================

Se necesita un formato de archivo para intercambiar productos entre almacenes de productos de librería y se desea una DTD que incluya estas restricciones:

* Debe haber un elemento raíz pedido que puede constar de libros, cuadernos y/o lápices. Los tres elementos pueden aparecer repetidos y en cualquier orden. Tambien pueden aparecer por ejemplo 4 libros, 2 lapices y luego 4 lapices de nuevo.
* Todo libro tiene un atributo obligatorio titulo.
* Los elementos cuaderno tiene un atributo optativo num_hojas.
* Todo elemento lápiz debe tener dentro un  elemento obligatorio número.

La solución a la DTD:

.. code-block:: dtd

	<!ELEMENT pedido (libro|cuaderno|lapiz)+>
	<!ELEMENT libro (#PCDATA)>
	<!ATTLIST libro titulo CDATA #REQUIRED>
	<!ELEMENT cuaderno (#PCDATA)>
	<!ATTLIST cuaderno num_hojas CDATA #IMPLIED>
	<!ELEMENT lapiz (numero)>
	<!ELEMENT numero (#PCDATA)>


   

.. code-block:: xml

	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE pedido SYSTEM "libreria.dtd">
	<pedido>
	  <libro titulo="Java 8"></libro>
	  <cuaderno></cuaderno>
	  <libro titulo="HTML y CSS"/>
	  <libro titulo="SQL para Dummies"/>
	  <cuaderno num_hojas="150"/>
	  <lapiz>
		<numero>2H</numero>
	  </lapiz>
	  <cuaderno num_hojas="250"/>
	  <cuaderno num_hojas="100"/>
	  <lapiz>
		<numero>2B</numero>
	  </lapiz>
	  <lapiz>
		<numero>1HB</numero>
	  </lapiz>
	</pedido>   

Ejercicio: multinacional
===========================

Una multinacional que opera en bolsa necesita un formato de intercambio de datos para que sus programas intercambien información sobre los mercados de acciones.

En general todo archivo constará de un listado de cosas como se detalla a continuación


* En el listado aparecen siempre uno o varios futuros, despues una o varias divisas, despues uno o varios bonos y una o varias letras.

* Todos ellos tienen un atributo precio que es **obligatorio**
* Todos ellos tienen un elemento vacío que indica  de donde es el producto anterior: "Madrid", "Nueva York", "Frankfurt" o "Tokio".
* Las divisas y los bonos tienen un atributo optativo que se usa para indicar si el producto ha sido estable en el pasado o no.
* Un futuro es un valor esperado que tendrá un cierto producto en el futuro. Se debe incluir este producto en forma de elemento. También puede aparecer un elemento mercado que indique el país de procedencia del producto.
* Todo bono tiene un elemento país_de_procedencia para saber a qué estado pertenece. Debe tener tres elementos extra llamados "valor_deseado", "valor_mínimo" y "valor_máximo" para saber los posibles precios.
* Las divisas tienen siempre un nombre pueden incluir uno o más tipos de cambio para otras monedas.
* Las letras tienen siempre un tipo de interés pagadero por un país emisor. El país emisor también debe existir y debe ser siempre de uno de los países cuyas capitales aparecen arriba (es decir "España", "EEUU", "Alemania" y "Japón"



.. code-block:: xml

	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE listado [
		<!ELEMENT listado (futuro+, divisa+, bono+, letra+)>
		<!ATTLIST futuro precio CDATA #REQUIRED>
		<!ATTLIST divisa precio CDATA #REQUIRED>
		<!ATTLIST bono precio CDATA #REQUIRED>
		<!ATTLIST letra precio CDATA #REQUIRED>
		<!ELEMENT ciudad_procedencia (madrid|nyork|frankfurt|tokio)>
		<!ELEMENT madrid EMPTY>
		<!ELEMENT nyork EMPTY>
		<!ELEMENT frankfurt EMPTY>
		<!ELEMENT tokio EMPTY>
		<!ATTLIST divisa estable CDATA #IMPLIED>
		<!ATTLIST bono estable CDATA #IMPLIED>
		<!ELEMENT futuro (producto, mercado?, ciudad_procedencia)>
		<!ELEMENT producto (#PCDATA)>
		<!ELEMENT mercado (#PCDATA)>
		<!ELEMENT bono (pais_de_procedencia,valor_deseado,
				valor_minimo, valor_maximo, ciudad_procedencia)>
		<!ELEMENT valor_deseado (#PCDATA)>
		<!ELEMENT valor_minimo (#PCDATA)>
		<!ELEMENT valor_maximo (#PCDATA)>
		<!ELEMENT pais_de_procedencia (#PCDATA)>
		<!ELEMENT divisa (nombre_divisa, 
				tipo_de_cambio+, ciudad_procedencia)>
		<!ELEMENT nombre_divisa (#PCDATA)>
		<!ELEMENT tipo_de_cambio (#PCDATA)>
		<!ELEMENT letra (tipo_de_interes, pais_emisor,ciudad_procedencia)>
		<!ELEMENT tipo_de_interes (#PCDATA)>
		<!ELEMENT pais_emisor (espania|eeuu|alemania|japon)>
		<!ELEMENT espania     EMPTY>
		<!ELEMENT eeuu        EMPTY>
		<!ELEMENT alemania    EMPTY>
		<!ELEMENT japon       EMPTY>
	]>


	<listado>
		<futuro precio="11.28">
			<producto>Cafe</producto>
			<mercado>América Latina</mercado>
			<ciudad_procedencia>
				<frankfurt/>
			</ciudad_procedencia>
		</futuro>
		<divisa precio="183">
			<nombre_divisa>Libra esterlina</nombre_divisa>
			<tipo_de_cambio>2.7:1 euros</tipo_de_cambio>
			<tipo_de_cambio>1:0.87 dólares</tipo_de_cambio>
			<ciudad_procedencia>
				<madrid/>
			</ciudad_procedencia>
		</divisa>
		<bono precio="10000" estable="si">
			<pais_de_procedencia>
				Islandia
			</pais_de_procedencia>
			<valor_deseado>9980</valor_deseado>
			<valor_minimo>9950</valor_minimo>
			<valor_maximo>10020</valor_maximo>
			<ciudad_procedencia>
				<tokio/>
			</ciudad_procedencia>
		</bono>
		<letra precio="45020">
			<tipo_de_interes>4.54%</tipo_de_interes>
			<pais_emisor>
				<espania/>
			</pais_emisor>
			<ciudad_procedencia>
				<madrid/>
			</ciudad_procedencia>
		</letra>
	</listado>

	
	
Ejercicio
===========================================

La Seguridad Social necesita un formato de intercambio unificado para distribuir la información personal de los afiliados.

* Todo archivo XML contiene un listado de uno o mas afiliados
* Todo afiliado tiene los siguientes elementos:

	* DNI o NIE
	* Nombre
	* Apellidos
	* Situación laboral: que tiene que ser una y solo una de entre estas posibilidades: "en_paro", "en_activo", "jubilado", "edad_no_laboral"
	* Fecha de nacimiento: que se desglosa en los elementos obligatorios día, mes y anio.
	* Listado de bajas: que indica las situaciones de baja laboral del empleado. Dicho listado consta de una repetición de 0 o más bajas:
	
		* Una baja consta de tres elementos: causa (obligatoria), fecha de inicio (obligatorio) y fecha de final (optativa),
		
	* Listado de prestaciones cobradas: consta de 0 o más elementos prestación, donde se indicará la cantidad percibida (obligatorio), la fecha de inicio (obligatorio) y la fecha de final (obligatorio)



Esquemas XML
===========================================

Los esquemas XML son un mecanismo radicalmente distinto de crear reglas para validar ficheros XML. Se caracterizan por:

* Estar escritos en XML. Por lo tanto, las mismas bibliotecas que permiten procesar ficheros XML de datos permitirían procesar ficheros XML de reglas.

* Son mucho más potentes: ofrecen soporte a tipos de datos con comprobación de si el contenido de una etiqueta es de tipo ``integer``, ``date`` o de otros tipos. También se permite añadir restricciones como indicar valores mínimo y máximo para un número o determinar el patrón que debe seguir una cadena válida

* Ofrecen la posibilidad de usar *espacios de nombres*. Los espacios de nombres son similares a los paquetes Java: permiten a personas distintas el definir etiquetas con el mismo nombre pudiendo luego distinguir etiquetas iguales en función del espacio de nombres que importemos.

Un ejemplo
----------------

Supongamos que deseamos tener ficheros XML con un solo elemento llamado ``<cantidad>`` que debe tener dentro un número.

.. code-block:: xml

    <cantidad>20</cantidad>

Un posible esquema sería el siguiente:

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
       <xsd:element name="cantidad" type="xsd:integer"/>
    </xsd:schema>
    
¿Qué contiene este fichero?

1. En primer lugar se indica que este fichero va a usar unas etiquetas ya definidas en un espacio de nombre (o XML Namespace, de ahí ``xmlns``). Esa definición se hace en el espacio de nombres que aparece en la URL. Nuestro validador no descargará nada, esa URL es oficial y todos los validadores la conocen. Las etiquetas de ese espacio de nombres van a usar un prefijo que en este caso será ``xsd``.

2. Se indica que habrá un solo elemento y que el tipo de ese elemento es ``<xsd:integer>``. Es decir, un entero básico.

Si probamos el fichero de esquema con el fichero de datos que hemos indicado veremos que efectivamente el fichero XML de datos es válido. Sin embargo, si en lugar de una cantidad incluyésemos una cadena, veríamos que el fichero **no se validaría**


Tipos de datos básicos
------------------------------

Podemos usar los siguientes tipos de datos:


* ``xsd:byte``: entero de 8 bits.
* ``xsd:short``: entero de 16 bits
* ``xsd:int``: número entero de 32 bits.
* ``xsd:long``: entero de 64 bits.
* ``xsd:integer``: número entero sin límite de capacidad.
* ``xsd:unsignedByte``: entero de 8 bits sin signo.
* ``xsd:unsignedShort``: entero de 16 bits sin signo.
* ``xsd:unsignedInt``: entero de 32 bits sin signo.
* ``xsd:unsignedLong``: entero de 64 bits sin signo.
* ``xsd:string``: cadena de caracteres en la que los espacios en blanco se respetan.
* ``xsd:normalizedString``: cadena de caracteres en la que los espacios en blanco no se respetan y se reemplazarán secuencias largas de espacios o fines de línea por un solo espacio.
* ``xsd:date``: permite almacenar fechas que deben ir **obligatoriamente** en formato AAAA-MM-DD (4 digitos para el año, seguidos de un guión, seguido de dos dígitos para el mes, seguidos de un guión, seguidos de dos dígitos para el día del mes)
* ``xsd:time``: para almacenar horas en formato HH:MM:SS.C
* ``xsd:datetime``: mezcla la fecha y la hora separando ambos campos con una T mayúscula. Esto permitiría almacenar ``2020-09-22T10:40:22.6``.
* ``xsd:duration``. Para indicar períodos. Se debe empezar con "P" y luego indicar el número de años, meses, días, minutos o segundos. Por ejemplo "P1Y4M21DT8H" indica un período de 1 año, 4 meses, 21 días y 8 horas. Se aceptan períodos negativos poniendo -P en lugar de P.
* ``xsd:boolean``: acepta solo valores "true" y "false".
* ``xsd:anyURI``: acepta URIs.
* ``xsd:anyType``: es como la clase ``Object`` en Java. Será el tipo del cual heredaremos cuando no vayamos a usar ningún tipo especial como tipo padre.



La figura siguiente (tomada de la web del W3C) ilustra todos los tipos así como sus relaciones de herencia:

.. figure:: tipos_xml_schema.png
   :figwidth: 50%
   :align: center	

   Tipos en los XML Schemas


Derivaciones
-----------------

Prácticamente en cualquier esquema XML crearemos tipos nuevos (por establecer un símil es como si programásemos clases Java). Todos nuestros tipos tienen que heredar de otros tipos pero a la hora de "heredar" tenemos más posibilidades que en Java (dondo solo tenemos el "extends"). En concreto podemos heredar de 4 formas:

1. Poniendo restricciones (``restriction``). Consiste en tomar un tipo y crear otro nuevo en el que no se puede poner cualquier valor.
2. Extendiendo un tipo (``extension``). Se toma un tipo y se crea uno nuevo añadiendo cosas a los posibles valores que pueda tomar el tipo inicial.
3. Haciendo listas (``lists``). Es como crear vectores en Java.
4. Juntando otros tipos para crear tipos complejos (``union``). Es como crear clases Java en las que añadimos atributos de tipo ``int``, ``String``, etc...

En general, las dos derivaciones más usadas con diferencia son las restricciones y las extensiones, que se comentan por separado en los puntos siguientes.

Tipos simples y complejos
----------------------------

Todo elemento de un esquema debe ser de uno de estos dos tipos.

* Un elemento es de tipo simple si no permite dentro ni elementos hijo ni atributos.
* Un elemento es tipo complejo si permite tener dentro otras cosas (que veremos en seguida). Un tipo complejo puede a su vez tener contenido simple o contenido complejo:

    * Los que son de contenido simple no permiten tener dentro elementos hijo pero sí permiten atributos.
    * Los que son de contenido complejo sí permiten tener dentro elementos hijo y atributos.
    
Así, por ejemplo un tipo simple que no lleve ninguna restricción se puede indicar con el campo ``type`` de un ``element`` como hacíamos antes:

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
       <xsd:element name="cantidad" type="xsd:integer"/>
    </xsd:schema>


Sin embargo, si queremos indicar alguna restricción adicional ya no podremos usar el atributo ``type``. Deberemos reescribir nuestro esquema así:


.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
       <xsd:simpleType>
        Aquí irán las restricciones, que hemos omitido por ahora.
       </xsd:simpleType>
    </xsd:schema>


Ejercicio:edad de los trabajadores
-----------------------------------

Se desea crear un esquema que permita validar la edad de un trabajador, que debe tener un valor entero de entre 16 y 65.

Por ejemplo, este XML debería validarse:

.. code-block:: xml

    <edad>28</edad>
    
Pero este no debería validarse:

.. code-block:: xml

    <edad>-3</edad>
    
La solución podría ser algo así:

.. code-block:: xml

    <xsd:schema
     xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="edad"
                     type="tipoEdad"/>
        <xsd:simpleType name="tipoEdad">
            <xsd:restriction base="xsd:integer">
                <xsd:minInclusive value="16"/>
                <xsd:maxInclusive value="65"/>
            </xsd:restriction>
        </xsd:simpleType>    
    </xsd:schema>


Ejercicio: peso de productos
------------------------------

Se desea crear un esquema que permita validar un elemento peso, que puede tener un valor de entre 0 y 1000 pero aceptando valores con decimales, como por ejemplo 28.88

Una posible solución sería:

.. code-block:: xml

  <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="peso" type="tipoPeso"/>
    <xsd:simpleType name="tipoPeso">
      <xsd:restriction base="xsd:decimal">
        <xsd:minInclusive value="0"/>
        <xsd:maxInclusive value="1000"/>
      </xsd:restriction>
    </xsd:simpleType>
  </xsd:schema>

Ejercicio: pagos validados
---------------------------

Crear un esquema que permita validar un elemento ``pago`` en el cual puede haber cantidades enteras de entre 0 y 3000 euros.


.. code-block:: xml

  <xsd:schema
      xmlns:xsd="http://www.w3.org/2001/XMLSchema">    
    <xsd:element name="pago" type="tipoPago"/>
    <xsd:simpleType name="tipoPago">
      <xsd:restriction base="xsd:integer">
        <xsd:minInclusive value="0"/>
        <xsd:maxInclusive value="3000"/>
      </xsd:restriction>
    </xsd:simpleType>
  </xsd:schema>
  
Ejercicio: validación de DNIs
--------------------------------

Crear un esquema que permita validar un único elemento ``dni`` que valide el patrón de 7-8 cifras + letra que suelen tener los DNI en España:

.. code-block:: xml

  <xsd:schema
      xmlns:xsd="http://www.w3.org/2001/XMLSchema">  
    <xsd:element name="dni" type="tipoDNI"/>
    <xsd:simpleType name="tipoDNI">
      <xsd:restriction base="xsd:string">
        <xsd:pattern value="[0-9]{7,8}[A-Z]"/>
      </xsd:restriction>
    </xsd:simpleType>
  </xsd:schema>


Uniendo la herencia y el sistema de tipos
--------------------------------------------


Llegados a este punto ocurre lo siguiente:

* Por un lado tenemos que especificar si nuestros tipos serán simples o complejos (los cuales a su vez pueden ser complejos con contenido simple o complejos con contenido complejo).
* Por otro lado se puede hacer herencia ampliando cosas (extensión) o reduciendo cosas (restricciones a los valores).

Se deduce por tanto que no podemos aplicar todas las "herencias" a todos los tipos:

1. Los tipos simples no pueden tener atributos ni subelementos, por lo tanto **les podremos aplicar restricciones pero nunca la extensión**.

2. Los tipos complejos (independientemente del tipo de contenido) sí pueden tener otras cosas dentro por lo que **les podremos aplicar tanto restricciones como extensiones**.


Restricciones
------------------
Como se ha dicho anteriormente la forma más común de trabajar es crear tipos que en unos casos aplicarán modificaciones en los tipos ya sea añadiendo cosas o restringiendo posibilidades. En este apartado se verá como aplicar restricciones.

**Si queremos aplicar restricciones para un tipo simple las posibles restricciones son:**

* ``minInclusive`` para indicar el menor valor numérico permitido.
* ``maxInclusive`` para indicar el mayor valor numérico permitido.
* ``minExclusive`` para indicar el menor valor numérico que ya no estaría permitido.
* ``maxExclusive`` para indicar el mayor valor numérico que ya no estaría permitido.
* ``totalDigits`` para indicar cuantas posibles cifras se permiten.
* ``fractionDigits`` para indicar cuantas posibles cifras decimales se permiten.
* ``length`` para indicar la longitud exacta de una cadena.
* ``minLength`` para indicar la longitud mínima de una cadena.
* ``maxLength`` para indicar la longitud máxima de una cadena.
* ``enumeration`` para indicar los valores aceptados por una cadena.
* ``pattern`` para indicar la estructura aceptada por una cadena.

**Si queremos aplicar restricciones para un tipo complejo con contenido las posibles restricciones son las mismas de antes, pero además podemos añadir el elemento <attribute> así como las siguientes.**

* ``sequence`` para indicar una secuencia de elementos
* ``choice`` para indicar que se debe elegir un elemento de entre los que aparecen.


Atributos
-----------------------
En primer lugar es muy importante recordar que **si queremos que un elemento tenga atributos entonces ya no
se puede considerar que sea de tipo simple. Se debe usar FORZOSAMENTE un complexType**. Por otro lado en los XML Schema todos los atributos **son siempre opcionales, si queremos hacerlos obligatorios habrá que añadir un "required".**

Un atributo se define de la siguiente manera:

.. code-block:: xml

    <xsd:attribute name="fechanacimiento" type="xsd:date" use="required"/>
    
Esto define un atributo llamado ``nombre`` que aceptará solo fechas como valores válidos y que además es obligatorio poner siempre.


Ejercicios de XML Schemas
======================================

Cantidades limitades
------------------------

Crear un esquema que permita verificar algo como lo siguiente:

.. code-block:: xml

    <cantidad>20</cantidad>
    
Se necesita que la cantidad tenga solo valores aceptables entre -30 y +30.

Solución a las cantidades limitadas
-------------------------------------

La primera pregunta que debemos hacernos es ¿necesitamos crear un tipo simple o uno complejo?. Dado que nuestro único elemento no tiene subelementos ni atributos dentro podemos afirmar que solo necesitamos un tipo simple.

Como aparentemente nuestro tipo necesita usar solo valores numéricos y además son muy pequeños nos vamos a limitar a usar un ``short``. Sobre ese ``short`` pondremos una restriccion que permita indicar los valores mínimo y máximo.

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="cantidad">
            <xs:simpleType>
                <xs:restriction base="xs:short">
                    <xs:minInclusive value="-30"/>
                    <xs:maxInclusive value="30"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:element>
    </xs:schema>

Este esquema dice que el elemento raíz debe ser ``cantidad``. Luego indica que es un tipo simple y dentro de él indica que se va a establecer una restricción teniendo en mente que se va a "heredar" del tipo ``short``. En concreto se van a poner dos restricciones, una que el valor mínimo debe ser -30 y otra que el valor máximo debe ser 30.

Existe una alternativa más recomendable, que es separar los elementos de los tipos. De esa manera, se pueden "reutilizar" las definiciones de tipos.

.. code-block:: xml

    <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="cantidad" type="tipoCantidades">            
        </xs:element>
        <xs:simpleType name="tipoCantidades">
                <xs:restriction base="xs:short">
                    <xs:minInclusive value="-30"/>
                    <xs:maxInclusive value="30"/>
                </xs:restriction>
            </xs:simpleType>
    </xs:schema>



Obsérvese que hemos puesto el tipo por separado y le hemos dado el nombre ``tipoCantidades``. El elemento raíz tiene su nombre y su tipo en la misma línea.

Cantidades limitadas con atributo divisa
------------------------------------------

Se desea crear un esquema para validar XML en los que haya un solo elemento raíz llamado cantidad en el que se debe poner siempre un atributo "divisa" que indique en qué moneda está una cierta cantidad. El atributo divisa siempre será una cadena y la cantidad siempre será un tipo numérico que acepte decimales (por ejemplo ``float``). El esquema debe validar los archivos siguientes:


.. code-block:: xml

    <cantidad divisa="euro">20</cantidad>
    
.. code-block:: xml

    <cantidad divisa="dolar">18.32</cantidad>
    
Pero no debe validar ninguno de los siguientes:

.. code-block:: xml

    <cantidad>20</cantidad>
    
.. code-block:: xml

    <cantidad divisa="dolar">abc</cantidad>
    
Solución a las cantidades limitadas con atributo divisa
---------------------------------------------------------

Crearemos un tipo llamado "tipoCantidad". Dicho tipo *ya no puede ser un simpleType ya que necesitamos que haya atributos**. Como no necesitamos que tenga subelementos dentro este ``complexType`` llevará dentro un ``simpleContent`` (y no un ``complexContent``).

Aparte de eso, como queremos "ampliar" un elemento para que acepte tener dentro un atributo obligatorio "cantidad" usaremos una ``<extension>``. Así, el posible esquema sería este:

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="cantidad" type="tipoCantidad"/>
        <xsd:complexType name="tipoCantidad">
            <xsd:simpleContent>
                <xsd:extension base="xsd:float">
                    <xsd:attribute name="divisa" type="xsd:string" use="required"/>
                </xsd:extension>
            </xsd:simpleContent>
        </xsd:complexType>
    </xsd:schema>


Cantidades limitadas con atributo divisa con solo ciertos valores
-------------------------------------------------------------------

Queremos ampliar el ejercicio anterior para evitar que ocurran errores como el siguiente:

.. code-block:: xml

    <cantidad divisa="aaaa">18.32</cantidad>
    
Vamos a indicar que el atributo solo puede tomar tres posibles valores: "euros", "dolares" y "yenes".

Solución al atributo con solo ciertos valores
-------------------------------------------------

Ahora tendremos que crear dos tipos. Uno para el elemento ``cantidad`` y otro para el atributo ``divisa``. Llamaremos a estos tipos ``tipoCantidad`` y ``tipoDivisa``.

La solución comentada puede encontrarse a continuación. Como puede verse, hemos includo comentarios. Pueden insertarse etiquetas ``annotation`` que permiten incluir anotaciones de diversos tipos, siendo la más interesante la etiqueta ``documentation`` que nos permite incluir comentarios.

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="cantidad" type="tipoCantidad"/>
        <xsd:annotation>
            <xsd:documentation>
            A continuación creamos el tipo cantidad
            </xsd:documentation>
        </xsd:annotation>
        <xsd:complexType name="tipoCantidad">
            <xsd:annotation>
                <xsd:documentation>
                Como solo va a llevar atributos debemos
                usar un simpleContent
                </xsd:documentation>
            </xsd:annotation>
            <xsd:simpleContent>
                <xsd:annotation>
                    <xsd:documentation>
                    Como queremos "ampliar" un tipo/clase
                    para que lleve atributos usaremos
                    una extension
                    </xsd:documentation>
                </xsd:annotation>
                <xsd:extension base="xsd:float">
                    <xsd:attribute name="divisa" type="tipoDivisa"/>
                </xsd:extension>
            </xsd:simpleContent>
        </xsd:complexType>
        <xsd:annotation>
            <xsd:documentation>
            Ahora tenemos que fabricar el "tipoDivisa" que indica
            los posibles valores válidos para una divisa. Estas
            posibilidades se crean con una "enumeration". Nuestro
            tipo es un "string" y como vamos a restringir los posibles
            valores usaremos "restriction"
            </xsd:documentation>
        </xsd:annotation>
        <xsd:simpleType name="tipoDivisa">
            <xsd:restriction base="xsd:string">
                <xsd:enumeration value="euros"/>
                <xsd:enumeration value="dolares"/>
                <xsd:enumeration value="yenes"/>
            </xsd:restriction>
        </xsd:simpleType>
    </xsd:schema>

Ejercicio: productos con atributos
-----------------------------------

Se desea crear un esquema que permita validar un elemento raíz llamado ``producto`` de tipo ``xsd:string``. El producto tiene dos atributos:

* Un atributo se llamará ``cantidad`` y es obligatorio. Debe aceptar solo enteros positivos.

* También habrá un atributo llamado ``unidad`` que solo acepta los ``xsd:string`` "cajas" y "pales".


.. code-block:: xml

  <xsd:schema
      xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="producto" type="tipoProducto"/>
    <xsd:complexType name="tipoProducto">
      <xsd:simpleContent>
        <xsd:extension base="xsd:string">
          <xsd:attribute name="cantidad"
                type="xsd:unsignedInt" use="required"/>
          <xsd:attribute name="unidad"
                type="tipoUnidad"/>
        </xsd:extension>
      </xsd:simpleContent>
    </xsd:complexType>
    <xsd:simpleType name="tipoUnidad">
      <xsd:restriction base="xsd:string">
        <xsd:enumeration value="caja"/>
        <xsd:enumeration value="pale"/>
      </xsd:restriction>
    </xsd:simpleType>
  </xsd:schema>

Ejercicio: clientes con información adicional
------------------------------------------------

Se desea crear un esquema XML que permita validar un elemento llamado ``cliente`` que puede almacenar un ``xsd:string``. El cliente contiene:

* Un atributo obligatorio llamado ``codigo`` que contiene el código del cliente, que siempre consta de tres letras mayúsculas de tres números.

* Un atributo optativo llamado ``habitual`` que se usará para saber si es un cliente habitual o no. Acepta valores "true" y "false".

* Un atributo optativo llamado ``cantidad`` que indica su compra. Es un entero con valores de entre 0 y 1000. 


Ejercicio: inventario
------------------------
Varios administradores necesitan intercambiar información sobre inventario de material de oficina. Para ello, han llegado a un acuerdo sobre lo que se permite en un fichero XML de inventario. La idea básica es permitir ficheros como este:

.. code-block:: xml

    <inventario>
        <objeto codigo="545333">
            <mesa>
                <peso>4.55</peso>
                <superficie unidad="cm2">100</superficie>
            </mesa>
        </objeto>
        <objeto codigo="343987">
            <silla>
                <peso>3.50</peso>
            </silla>
        </objeto>
    </inventario>

Las reglas concretas son estas:

1. Todo objeto tiene un atributo código de 6 cifras.
2. Dentro de ``<objeto>`` puede haber uno de estos dos elementos hijo: un elemento ``<mesa>`` o un elemento ``<silla>``.
3. Toda mesa tiene un elemento hijo ``<peso>``. El peso siempre es un decimal positivo con dos cifras decimales.
4. Toda mesa tiene una ``<superficie>``. La superficie es un ``unsignedInt``. La superficie siempre tiene un atributo que puede ser solo una de estas dos cadenas: ``m2`` o ``cm2``.
5. Toda silla tiene siempre un ``<peso>`` y las reglas de ese peso son exactamente las mismas que las reglas de ``<peso>`` del elemento ``<mesa>``












Lista de clientes como XML Schemas
------------------------------------

En este apartado volveremos a ver un problema que ya resolvíamos con DTD: supongamos que en nuestros ficheros deseamos indicar que el elemento raíz es ``<listaclientes>``. Dentro de ``<listaclientes>`` deseamos permitir uno o más elementos ``<cliente>``. Dentro de ``<cliente>`` todos deberán tener ``<cif>`` y ``<nombre>`` y en ese orden. Dentro de ``<cliente>`` puede aparecer o no un elemento ``<diasentrega>`` para indicar que ese cliente exige un máximo de plazo. Como no todo el mundo usa plazos el ``<diasentrega>`` es optativo.

Vayamos paso a paso. Primero decimos como se llama el elemento raíz y de qué tipo es:

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="listaclientes" type="tipoListaClientes"/>
    </xsd:schema>
    
Ahora queda definir el tipo ``tipoListaClientes``. Este tipo va a contener un elemento (por lo que ya sabemos que es un ``complexType`` con ``complexContent`` dentro), y en concreto queremos que sea un solo elemento llamado ``cliente``, es decir **queremos imponer una restricción**. Aunque queramos un solo elemento tendremos que indicar una restricción. Como queremos permitir que el elemento pueda aparecer muchas veces utilizaremos un ``maxOccurs`` con el valor ``unbounded``.

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="listaclientes" type="tipoListaClientes"/>
        <xsd:complexType name="tipoListaClientes">
            <xsd:complexContent>
                <xsd:restriction>
                    <xsd:element name="cliente" type="tipoCliente"
                    maxOccurs="unbounded"/>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
    </xsd:schema>
    


Definamos ahora el tipo ``tipoCliente``. Dicho tipo **necesita tener subelementos dentro** así que evidentemente va a ser de tipo complejo. La pregunta es ¿es "tipo complejo con contenido simple" o "tipo complejo con contenido complejo"?. Si lo hiciéramos de "tipo complejo con contenido simple" podríamos tener atributos pero no subelementos, así que forzosamente tendrá que ser de un "tipo complejo con contenido complejo". Igual que antes impondremos una restricciones que es permitir solo que aparezcan ciertos elementos en cierto orden. El elemento ``plazo`` lo haremos optativo.


.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="listaclientes" type="tipoListaClientes"/>
        <xsd:complexType name="tipoListaClientes">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    <xsd:sequence>
                        <xsd:element name="cliente" type="tipoCliente"
                        maxOccurs="unbounded"/>
                    </xsd:sequence>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
        <xsd:complexType name="tipoCliente">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    <xsd:sequence>
                        <xsd:element name="cif" type="xsd:string"/>
                        <xsd:element name="nombre" type="xsd:string"/>
                        <xsd:element name="plazo" type="xsd:string"
                        minOccurs="0"/>
                    </xsd:sequence>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
    </xsd:schema>



Si ahora probamos este XML veremos que el fichero se valida perfectamente a pesar de que es evidente que tiene errores. Es lógico, dado que no hemos aprovechado a fondo el sistema de tipos de XML para evitar que nadie suministre datos incorrectos en un XML. Dicha mejora la dejaremos para el siguiente ejercicio.

.. code-block:: xml

    <listaclientes>
        <cliente>
            <cif>dd</cif>
            <nombre>20</nombre>
        </cliente>    
        <cliente>
            <cif>dd</cif>
            <nombre>20</nombre>
            <plazo>ABCD</plazo>
        </cliente>  
    </listaclientes>


Ampliación del esquema para clientes
-------------------------------------

Ahora ampliaremos el XML Schema del fichero anterior para que nadie suministre información incorrecta.

En concreto tenemos tres datos:

1. El CIF, que vamos a presuponer que siempre tiene 8 cifras y al final una letra mayúsculas. Si alguna empresa tiene 7 cifras deberá incluir un 0 extra.
2. El nombre, que puede ser una cadena cualquiera.
3. El plazo, que debería ser un número positivo válido.

Ahora, el fichero anterior no debería ser validado por el validador, pero sí debería serlo un fichero como este.

.. code-block:: xml

    <listaclientes>
        <cliente>
            <cif>01234567D</cif>
            <nombre>Juan Sanchez</nombre>
        </cliente>    
        <cliente>
            <cif>05676554A</cif>
            <nombre>Pedro Diaz</nombre>
            <plazo>45</plazo>
        </cliente>  
    </listaclientes>

La solución a los tres problemas indicados antes sería la siguiente:

1. El nombre puede ser una cadena cualquiera, por lo que tendrá que seguir siendo de tipo ``xsd:string``. Eso significa que si alguien introdujese un número en el nombre el fichero seguiría validándose. Por desgracia dicho problema no se puede resolver.
2. El plazo debería ser un número. Le asignaremos un tipo ``xsd:unsignedInt``.
3. El CIF es más complejo. Deberemos crear un tipo nuevo y establecer una restricción a los posibles valores que puede tomar.

Así, una posible solución sería esta:

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="listaclientes" type="tipoListaClientes"/>
        <xsd:complexType name="tipoListaClientes">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    <xsd:sequence>
                        <xsd:element name="cliente" type="tipoCliente"
                            maxOccurs="unbounded"/>
                    </xsd:sequence>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
        
        <xsd:complexType name="tipoCliente">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                <xsd:sequence>
                    <xsd:element name="cif" type="tipoCif"/>
                    <xsd:element name="nombre" type="xsd:string"/>
                    <xsd:element name="plazo" type="xsd:unsignedInt" minOccurs="0"/>
                </xsd:sequence>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
        <xsd:simpleType name="tipoCif">
            <xsd:restriction base="xsd:string">
                <xsd:pattern value="[0-9]{8}[A-Z]"/>
            </xsd:restriction>
        </xsd:simpleType>
        <xsd:simpleType name="tipoPlazo">
            <xsd:restriction base="xsd:unsignedInt"/>
        </xsd:simpleType>
    </xsd:schema>

Ejercicio: lista de códigos
-----------------------------
Se nos pide crear un esquema que permita validar un fichero como el siguiente:

.. code-block:: xml

  <listacodigos>
    <codigo>AAA2DD</codigo>
    <codigo>BBB2EE</codigo>
    <codigo>BBB2EE</codigo>
  </listacodigos>

En concreto, todo código tiene la estructura siguiente:

1. Primero van tres mayúsculas
2. Despues va exactamente un digito.
3. Por último hay exactamente dos mayúsculas.

Un posible esquema XML sería el siguiente (obsérvese como usamos ``maxOccurs`` para indicar que el elemento puede repetirse un máximo de "infitas veces":

.. code-block:: xml

  <xsd:schema
      xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="listacodigos"
                 type="tipoLista"/>
    <xsd:complexType name="tipoLista">
      <xsd:complexContent>
        <xsd:restriction base="xsd:anyType">
          <xsd:sequence>
            <xsd:element name="codigo"
                         type="tipoCodigo"
                         maxOccurs="unbounded"/>
          </xsd:sequence>
        </xsd:restriction>
      </xsd:complexContent>
    </xsd:complexType>
    <xsd:simpleType name="tipoCodigo">
      <xsd:restriction base="xsd:string">
        <xsd:pattern value="[A-Z]{3}[0-9][A-Z]{2}"/>
      </xsd:restriction>
    </xsd:simpleType>
  </xsd:schema>


Ejercicio: otra lista de clientes
------------------------------------

Ahora se nos pide crear un esquema que permita validar un fichero como el siguiente, en el que hay una lista de clientes y el nombre es optativo, aunque los apellidos son obligatorios:

.. code-block:: xml
  
  <listaclientes>
    <cliente>
      <nombre>Juan</nombre>
      <apellidos>Sanchez</apellidos>
    </cliente>
    <cliente>
      <nombre>Jose</nombre>
      <apellidos>Diaz</apellidos>
    </cliente>
  </listaclientes>
  
La solución puede ser algo así:

.. code-block:: xml

  <xsd:schema
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="listaclientes"
                 type="tipoLista"/>
    <xsd:complexType name="tipoLista">
      <xsd:complexContent>
        <xsd:restriction base="xsd:anyType">
          <xsd:sequence>
            <xsd:element name="cliente"
                         type="tipoCliente"
                         maxOccurs="unbounded"/>
          </xsd:sequence>
        </xsd:restriction>
      </xsd:complexContent>
    </xsd:complexType>
    
    <xsd:complexType name="tipoCliente">
      <xsd:complexContent>
        <xsd:restriction base="xsd:anyType">
          <xsd:sequence>
            <xsd:element name="nombre"
                         type="xsd:string"
                         minOccurs="0"/>
            <xsd:element name="apellidos"
                         type="xsd:string"/>
          </xsd:sequence>
        </xsd:restriction>
    </xsd:complexContent>
    </xsd:complexType>
  </xsd:schema>


Ejercicio: listas de productos
--------------------------------

Se pide validar correctamente algo como esto:

.. code-block:: xml

  <listaproductos>
    <producto codigo="DX-22"><!--Codigo obligatorio-->
      <descripcion>Ordenador</descripcion><!--Optativa-->
      <peso>23.44</peso><!--Positivo con decimales-->
    </producto>
    <producto codigo="CX-124">
      <peso>17.50</peso>
    </producto>
    <producto codigo="CX-124">
      <peso>17.50</peso>
    </producto>
  </listaproductos>
  
Las reglas son:

1. Una lista de productos puede tener dentro muchos productos.
2. Todo producto tiene un "codigo" cuya estructura *dos mayúsculas seguidas de un guión seguido de dos o tres cifras*
3. Todo producto *puede tener (optativo)* un elemento descripción que es de tipo texto.
4. Todo producto **debe tener** un elemento peso que debe aceptar decimales pero que nunca puede ser negativo, es decir su valor mínimo es 0

La solución se muestra a continuación:

.. code-block:: xml

  <xsd:schema
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:element name="listaproductos" type="tipoLista"/>
    <xsd:complexType name="tipoLista">
      <xsd:complexContent>
        <xsd:restriction base="xsd:anyType">
          <xsd:sequence>
            <xsd:element name="producto"
                         type="tipoProducto"
                         maxOccurs="unbounded"/>
          </xsd:sequence>
        </xsd:restriction>
      </xsd:complexContent>
    </xsd:complexType>
    <xsd:complexType name="tipoProducto">
      <xsd:complexContent>
        <xsd:restriction base="xsd:anyType">
          <xsd:sequence>
            <xsd:element name="descripcion"
                         type="xsd:string"
                         minOccurs="0"/>
            <xsd:element name="peso"
                         type="tipoPeso"/>
  
          </xsd:sequence>
          <xsd:attribute name="codigo"
                         type="tipoCodigo"
                         use="required"/>
        </xsd:restriction>
      </xsd:complexContent>
    </xsd:complexType>
    <xsd:simpleType name="tipoPeso">
      <xsd:restriction base="xsd:decimal">
        <xsd:minInclusive value="0"/>
      </xsd:restriction>
    </xsd:simpleType>
    <xsd:simpleType name="tipoCodigo">
      <xsd:restriction base="xsd:string">
        <xsd:pattern value="[A-Z]{2}-[0-9]{2,3}"/>
      </xsd:restriction>
    </xsd:simpleType>
  </xsd:schema>

Ejercicio: validación de componentes
--------------------------------------

Validar un fichero como este:

.. code-block:: xml

  <listacomponentes>
    <componente>
      <tarjetagrafica>
        <memoria>2GB</memoria>
        <precio moneda="euros">190</precio>
      </tarjetagrafica>
    </componente>
    <componente codigo="123456">
      <monitor>
        <tamanio>14</tamanio>
        <precio moneda="euros">99.49</precio>
      </monitor>
    </componente>
  </listacomponentes>

Las reglas son las siguientes:

1. El elemento raíz se llama ``listacomponentes``.
2. Dentro de él puede haber uno o más elementos ``componente``
3. Un componente puede ser una ``tarjetagrafica`` o un ``monitor``.
4. Un componente puede tener un atributo llamado ``codigo`` cuya estructura es siempre un dígito de 6 cifras.
5. Una tarjeta gráfica siempre tiene dos elementos llamados ``memoria`` y ``precio``.
6. La memoria siempre es una cifra seguido de GB o TB.
7. El tamaño del monitor siempre es un entero positivo.
8. El precio siempre es una cantidad positiva con decimales. El precio siempre lleva un atributo ``moneda`` que solo puede valer "euros" o "dolares" y que se utiliza para saber en qué moneda está el precio.

La solución se muestra a continuación:

.. code-block:: xml

    <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <xsd:element name="listacomponentes" type="tipoLista"/>
        <xsd:complexType name="tipoLista">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    <xsd:sequence>
                        <xsd:element name="componente"
                                     type="tipoComponente"
                                     maxOccurs="unbounded"/>
                    </xsd:sequence>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
        <xsd:complexType name="tipoComponente">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    <xsd:choice>
                        <xsd:element name="tarjetagrafica" type="tipoTarjeta"/>
                        <xsd:element name="monitor" type="tipoMonitor"/>
                    </xsd:choice>
                    <xsd:attribute name="codigo" type="tipoCodigo"/>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
        <xsd:simpleType name="tipoCodigo">
            <xsd:restriction base="xsd:string">
                <xsd:pattern value="[1-9][0-9]{5}"/>
            </xsd:restriction>
        </xsd:simpleType>
        <xsd:complexType name="tipoTarjeta">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    <xsd:sequence>
                        <xsd:element name="memoria" type="tipoMemoria"/>
                        <xsd:element name="precio" type="tipoPrecio"/>
                    </xsd:sequence>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
        <xsd:simpleType name="tipoMemoria">
            <xsd:restriction base="xsd:string">
                <xsd:pattern value="[0-9]+[GT]B"/>
            </xsd:restriction>
        </xsd:simpleType>
        <!--Aqui definimos un precio con restriccion del cual
        heredaremos despues para añadir el atributo a
        la cantidad-->
        <xsd:simpleType name="tipoPrecioRestringido">
            <xsd:restriction base="xsd:decimal">
                <xsd:minInclusive value="0"/>
            </xsd:restriction>
        </xsd:simpleType>
        <!--Aqui heredamos del tipo anterior y añadimos
        el atributo-->
        <xsd:complexType name="tipoPrecio">
            <xsd:simpleContent>
                <xsd:extension base="tipoPrecioRestringido">
                    <xsd:attribute name="moneda" type="tipoMoneda"/>
                </xsd:extension>
            </xsd:simpleContent>
        </xsd:complexType>
        
    
        <xsd:simpleType name="tipoMoneda">
            <xsd:restriction base="xsd:string">
                <xsd:enumeration value="euros"/>
                <xsd:enumeration value="dolares"/>
            </xsd:restriction>
        </xsd:simpleType>
        <xsd:complexType name="tipoMonitor">
            <xsd:complexContent>
                <xsd:restriction base="xsd:anyType">
                    <xsd:sequence>
                        <xsd:element name="tamanio" type="xsd:integer"/>
                        <xsd:element name="precio"  type="tipoPrecio"/>
                    </xsd:sequence>
                </xsd:restriction>
            </xsd:complexContent>
        </xsd:complexType>
    </xsd:schema>


Ejercicio tipo examen
===============================

Se necesita crear un esquema que controle la correcta sintaxis de ficheros con este estilo:

.. code-block:: xml

    <productosfinancieros>
        <producto>
            <bono>
                <valoractual moneda="yenes">2.212</valoractual>
                <beneficio>-2.83</beneficio>
            </bono>
        </producto>
        <producto>
            <futuro>
                <elemento idioma="espanol">Petroleo</elemento>
                <beneficio>-3.83</beneficio>
            </futuro>
        </producto>
        <producto>
            <acciones>
                <empresa pais="usa">ENRON</empresa>
                <beneficio>2.91</beneficio>
            </acciones>
        </producto>
    </productosfinancieros>

Las reglas concretas son las siguientes:

1. El elemento raíz es ``<productosfinancieros>``. Dentro de él debe haber uno o más elementos ``<producto>``.
2. Un ``<producto>`` puede ser de tres tipos: ``<bono>``, ``<futuro>`` y ``<acciones>``.
3. Todos los productos tienen siempre un elemento hijo llamado ``<beneficio>`` que puede ser un número con dos decimales (puede ser positivo o negativo).
4. Todo ``<bono>`` puede tener dentro un elemento llamado ``<valoractual>`` que contiene un valor decimal que puede ser positivo o negativo y tener o no decimales.
5. Todo ``<futuro>`` tiene un hijo llamado ``<elemento>`` que puede contener dentro cadenas de cualquier tipo. Para saber en qué idioma está la cadena se usa un atributo llamado ``idioma`` que indica el idioma en el que está escrita la cadena.
6. Las acciones siempre tienen un elemento ``<empresa>`` que indica el nombre de la empresa y un atributo llamado ``país`` que indica de donde es la empresa. De momento queremos limitarnos a los países ``usa``, ``alemania``, ``japon`` y ``espana``.

Recuérdese que siempre que no nos digan nada, se supone que un elemento o atributo es **obligatorio**. Si algo es optativo nos dirán "puede tener dentro", "puede contener", "puede aparecer", etc...

Examen
===========================================

El examen de este tema tendrá lugar el miércoles 23  marzo de 2017.










