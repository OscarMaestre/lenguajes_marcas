==========
Javascript
==========


Introducción
============


Surgió como una iniciativa de Netscape. **No hay ninguna relación entre Java y Javascript**. Algunas características de Javascript son:

* No se convierte en bytecodes, lo interpreta el navegador 
* Está estandarizado aunque no todos los navegadores se ciñen al 100% al estándar. El nombre del estándar es "ECMAScript"
* No está orientado a objetos, sino que está basado en objetos.
* Es de tipado débil: esto significa que podemos cambiar una variable de tipo sin problemas, el intérprete intentará hacer las conversiones correctas.


Tipos de datos
==============

Javascript acepta los siguientes tipos de datos:

* Números.
* Cadenas
* Booleanos (lógicos)
* undefined: se utiliza cuando intentamos acceder a una variable que no contiene nada porque no se ha creado.
* null: se utiliza habitualmente para indicar algo vacío.




Incrustando Javascript
======================

Javascript se inserta en HTML con la etiqueta ``<script>``. Esta etiqueta puede ir en cualquier sitio del HTML, dentro de ``<head>`` o dentro de ``<body>``.



Un programa muy simple sería este:

.. code-block:: javascript

	var una_variable
    una_variable=42
    document.write(una_variable)
	
	
Decisiones
==========

Las decisiones se toman con la sentencia ``if`` que funciona exactamente igual que en Java. Se pueden utilizar los mismos operadores ``&&`` y ``||`` al igual que en Java.

.. code-block:: javascript

	if (una_variable > otra_variable) {
        document.write ("La primera es mayor que la segunda")
    } else {
        document.write ("La segunda es mayor que la primera")
    }
		
Vectores o Arrays
=================


En Javascript los arrays pueden almacenar elementos de distinto tipo. Al crearlos podemos indicar el tamaño o no, pero no habrá problemas si queremos almacenar más elementos de los previstos.


.. code-block:: javascript

	/* Una forma de crear un array*/
    vector_nombres=new Array()
    vector_nombres[0]="Juan Perez"
    vector_nombres[1]="Pedro Diaz"
    document.write ("El primer nombre es:"+vector_nombres[0])
    
    /* Otra forma de crearlos*/
    vector_numeros=new Array(2)
    vector_numeros[0]=23
    vector_numeros[1]=-45.23
    vector_numeros[2]=45e2

Bucles
======

Bucles for
----------

Bucles for estilo clásico
~~~~~~~~~~~~~~~~~~~~~~~~~

En estos bucles hay que poner la inicialización, la condición de final y la actualización:


.. code-block:: javascript

	for (var i=0; i<vector_numeros.length; i++){
		document.write("<br/>")
        document.write ("En la posición "+i)
        document.write (" está el número " + vector_numeros[i])
	}

Obsérvese que hemos introducido el atributo ``length`` de la clase ``Array`` que nos indica la longitud del vector.


Ejercicio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Crear un vector de 6 posiciones y rellenarlo con estos números: 9.98, 7.86, 4.53, 8.91, 5.76, 2.31.

Ordenar el vector y mostrar el contenido del vector ordenado por pantalla.

.. code-block:: java

        var v=new Array()
        v=[9.98, 7.86, 4.53,
           8.91, 5.76, 2.31]
        
        /* Vamos cogiendo cada elemento...*/
        for (var i=0; i<v.length; i++){
            /* Y se compara con
             * todos los demas*/
            for (var j=0; j<v.length; j++) {
                if (v[j]>v[i]) {
                    aux=v[i]
                    v[i]=v[j]
                    v[j]=aux
                } /* Fin del if*/
            } /* Fin del for interno*/
        } /* fin del for externo*/
   
        
        /* Se imprime el contenido*/
        for (var i=0; i<v.length; i++){
            alert ("Pos "+i+ ":"+v[i])
        }
	
	









Bucles foreach
~~~~~~~~~~~~~~

Funciona igual que el anterior pero es mucho más corto.


.. code-block:: javascript

	for (var posicion in vector_numeros) {
			document.write("<br/>")
			document.write ("En la posición "+posicion)
			document.write (" está el número " + vector_numeros[posicion])
	}


Bucles while
------------

Los bucles ``while`` funcionan igual que en Java

.. code-block:: javascript

	var posicion=0
	while (posicion<vector_numeros.length){
			document.write("<br/>")
			document.write ("En la posición "+posicion)
			document.write (" está el número " + vector_numeros[posicion])
			posicion++
    }


Ejercicio: media aritmética
===========================

Crear un programa que calcule la media aritmética del vector de números.

.. code-block:: javascript

		var suma=0
		for (var pos in vector_numeros){
			suma=suma+vector_numeros[pos]
		}
		var media=suma / vector_numeros.length
		document.write("<br/>La media es:" + media)


Ejercicio: desviación media
===========================

Crear un programa que calcule la desviación media del vector de números.



.. code-block:: javascript

	/* Para calcular la desviación media*/
    suma=0
    for (var pos in vector_numeros) {
        var desviacion= Math.abs ( vector_numeros[pos] - media )
        suma = suma + desviacion
    }
    /* En este punto la variable suma contiene la suma de las desviaciones*/
    var desv_media = suma / vector_numeros.length
    document.write("<br/>La desv media es:"+desv_media)

Ejercicio: la mediana
===================================================

Calcular la mediana del vector

.. code-block:: java

		if (v.length%2==0) {
            var pos1=v.length/2
            var pos2=pos1-1
            var elem1=v[pos1]
            var elem2=v[pos2]
            var mediana=(elem1+elem2)/2
        } else {
            var pos_central=(v.length-1)/2
            var mediana=v[pos_central]
        }
        doc	ument.write("La mediana es:"+mediana)	
	
Funciones
=========

Para crear una función usaremos la palabra ``function``, pondremos el nombre, luego los parámetros, dentro irá el código de la función, y si queremos devolver algo usaremos ``return``.

.. code-block:: javascript

	/* Función a la que le pasamos un vector de números y que
     * nos devuelve la media de sus valores*/
    
    function calcularMedia(vector_valores){
        var suma=0
        for (var pos in vector_valores){
            suma = suma + vector_valores[pos]
        }
        return suma / vector_valores.length
    }
    
    var vector=new Array(4)
    vector[0]=5
    vector[1]=2
    vector[2]=7
    vector[3]=8
    
    var media=calcularMedia(vector)
    document.write("<br/>La media es:"+media)

Una cuestión importante es que las funciones son valores asignables. Cuando queramos asignar una función a una variable **no pondremos paréntesis**. Cuando sí queramos ejecutar una función (ya sea con su nombre original o con el de la variable, sí pondremos los paréntesis con los parámetros que queramos pasar**.

.. code-block:: javascript

	function saludar(nombre){
        document.write("Hola "
            +nombre+"<br/>")
    }
    function despedir(nombre){
        document.write("Adios "
            +nombre+"<br/>")
    }
    saludar("Antonio")
    despedir("Antonio")
    /* Las funciones son valores
     * asignables*/
    var f=despedir
    f("Tomas")

	
	
	
	
	
Ejercicio
---------
Crear un programa que tenga una función que calcule la desviación media de valores de un vector.


.. code-block:: javascript

	/* Función que calcula la desviacion media de
	* un vector de valores numericos*/
    function calcularDesviacionMedia(vector_valores){
        var media=calcularMedia(vector_valores)
        var suma=0
        for (var pos in vector_valores){
            suma= suma + Math.abs (  vector_valores[pos] - media  )
        }
        return suma / vector_valores.length
    }

Ejercicio
---------

Crear un programa que tenga una función que calcule la moda.

.. code-block:: javascript

	/* Este vector nos dice cuantas veces aparece un número
     * en un vector*/
    function calcularFrecuencia(numero, vector){
        var num_veces=0
        for (var pos in vector) {
            if (vector[pos]==numero) {
                num_veces++
            }
        }
        return num_veces
    }
    
    /* Dado un vector de números se nos devuelve la posición
     * del número mayor*/
    function obtenerPosMayor(vector_valores){
        var posMayor=0
        var numMayor=vector_valores[0]
        for (var pos in vector_valores){
            if (vector_valores[pos]>numMayor) {
                numMayor=vector_valores[pos]
                posMayor=pos
            }
        }
        return posMayor
    }
    /* Función que devuelve el número "moda" de un vector*/
    function obtenerModa(vector_valores){
        var frecuencias=new Array(vector_valores.length)
        for (var pos in vector_valores){
             var numero=vector_valores[pos]
             frecuencias[pos]=calcularFrecuencia(numero, vector_valores)
        }
        var posModa=obtenerPosMayor(frecuencias)
        return vector_valores[posModa]
        
    }
    var vector=new Array(4)
    vector[0]=7
    vector[1]=7
    vector[2]=7
    vector[3]=5
	var moda=obtenerModa(vector)
	document.write("<br/>La moda es:"+moda)



Programación OO
===============

Se ha dicho anteriormente que Javascript es "basado en objetos" y no "orientado a objetos", es decir la POO es optativa. No por ello es menos potente.

En primer lugar, es posible crear objetos sin crear clases.

.. code-block:: javascript

	var empleado={
        nombre:"Pepe Perez",
        edad:27,
        fijo:true,
        estaJubilado:function (){
            if (this.edad>65) {
                return true
            } else {
                return false
            }
            
        }
    }
    document.write("<br/>El nombre es:"+empleado.nombre)
    document.write("<br/>¿Jubilado?" + empleado.estaJubilado() )

Ejercicio
---------

Añadir un método llamado ``nivelExperiencia`` que nos diga una de estas cosas:

* Nos debe devolver "junior" si la edad está entre 18 y 25
* Nos debe devolver "asociado" si la edad está entre 26 y 45
* Nos debe devolver "senior" si la edad está entre 46 y 60
* Nos debe devolver "experto" si la edad está entre 61 y 65
* Nos debe devolver "no aplicable" si la edad es mayor de 65


.. code-block:: javascript

	var empleado={
        nombre:"Pepe Perez",
        edad:27,
        fijo:true,
        estaJubilado:function (){
            if (this.edad>65) {
                return true
            } else {
                return false
            }
        },
        nivelExperiencia:function(){
            if ( (this.edad>18)  && (this.edad<=25) ){
                return "junior"
            }
            if ( (this.edad>=26)  && (this.edad<=45) ){
                return "asociado"
            }
        }
    }


Ejercicio
---------

Crear una clase GestorVectores que tenga los principales métodos estadísticos vistos hasta ahora: media, desviación media, mediana y moda.


.. code-block:: javascript

	gestor_vectores={
		vector_numeros:new Array(),
		setDatos:function(vector){
			this.vector_numeros=vector
			
		}
		, //Importante: separar métodos y atributos con ,
		getMedia:function(){
			var suma=0
			var media=0
			for (pos in this.vector_numeros) {
				suma=suma + this.vector_numeros[pos]
			}
			media=suma / this.vector_numeros.length
			return media
		}
		,
		getModa:function(){
			
		}
		,
		getMediana:function(){
			this.vector_numeros.sort()
		}
	}


	var vector_prueba=new Array(3)
	vector_prueba[0]=5
	vector_prueba[1]=10
	vector_prueba[2]=8
	gestor_vectores.setDatos ( vector_prueba )
	var media=gestor_vectores.getMedia()
	document.write ("La media es:"+media)

	
	
Programación con JQuery
=======================

Existen muchos navegadores que a veces muestran pequeñas diferencias entre ellos. Para evitar problemas los programadores tenían que incluir muchos código para comprobar qué navegador ejecutaba su JS y en función de eso actuar. Para resolver estas diferencias John Resig creó JQuery.

Inicio
------

A partir de ahora todos nuestros archivos HTML tendrán que cargar al comienzo la biblioteca JQuery con una etiqueta como esta:

.. code-block:: html

	<script src="jquery.js" language="Javascript">
	</script>
	<script src="nuestroprograma.js" language="Javascript">
	</script>


**El orden es importante**

La función $
------------

La función $ selecciona elementos de la página para que podamos hacer cosas con ellos. Es la función más utilizada de JQuery y veremos que podemos pedir que nos seleccione grupos de cosas de forma muy sencilla.


La función $ devuelve siempre objetos. Los atributos y métodos de esos objetos los iremos aprendiendo poco a poco.

En general, antes de poder procesar un elemento, deberemos seleccionarlo utilizando los mismos selectores que en CSS.

Gestión de eventos
------------------

Utilizando ``click`` podemos indicar a la biblioteca que queremos que cuando alguien haga click en un elemento se ejecute una cierta función. El siguiente código HTML y JS ilustra una posibilidad

.. code-block:: html

	<!DOCTYPE html>
	<html>
	<head>
		<script src="jquery.js"></script>
		<script src="ejemplo.js"></script>
		<title>Ejemplos</title>
		<style>
			div#texto{
				background-color:yellow;
			}
		</style>
	</head>

	<body>
	<form>
		<input type="button" value="fadeOut" id="botonizq">
		<input type="button" value="fadeIn" id="botonder">
	</form>

	<div id="texto">
		Texto texto texto
	</div>

	</body>
	</html>

El código Javascript asociado al HTML anterior es este.

.. code-block:: javascript

	/* Esperaremos hasta que el documento esté cargado y listo
	 * para ser procesado por nuestro programa*/

	var obj_documento = $(document)

	/* Cuando esté cargado ejecutaremos la función cuyo nombre aparezca aquí*/
	obj_documento.ready(inicio)

	//* Error gravísimo*/
	//obj_documento.ready( inicio() )

	function inicio(){
		var obj_izq=$("#botonizq")
		obj_izq.click ( fn_click_izq )
		var obj_der=$("#botonder")
		obj_der.click ( fn_click_der )
	}

	function fn_click_izq(){
		var obj_div=$("#texto")
		obj_div.fadeOut()
	}

	function fn_click_der(){
		var obj_div=$("#texto")
		obj_div.fadeIn()
	}

Solución HTML (párrafos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

    <div data-role="content">
        <div class="ui-grid-c">
            <div class="ui-block-a">
                <input type="submit"
                       id="mostrar_pares"
                       value="Mostrar pares">
            </div>
            <div class="ui-block-b">
                <input type="submit"
                       id="ocultar_pares"
                       value="Ocultar pares">
            </div>
            <div class="ui-block-c">
                <input type="submit"
                       id="mostrar_impares"
                       value="Mostrar impares">
            </div>
            <div class="ui-block-d">
                <input type="submit"
                       id="ocultar_impares"
                       value="Ocultar impares">
            </div>
        </div>
        <p class="p_impar">
            Soy un párrafo impar
        </p>
        <p class="p_par">
            Soy un párrafo par
        </p>
        <p class="p_impar">
            Soy un párrafo impar
        </p>
        <p class="p_par">
            Soy un párrafo par
        </p>
        <p class="p_impar">
            Soy un párrafo impar
        </p>
        <p class="p_par">
            Soy un párrafo par
        </p>
    </div>

Solución Javascript (párrafos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

	$(document).ready(main)

	function mostrar_pares(){
		var objetos=$(".p_par")
		objetos.slideDown()
	}
	function mostrar_impares(){
		var objetos=$(".p_impar")
		objetos.slideDown()
	}
	function ocultar_pares(){
		var objetos=$(".p_par")
		objetos.slideUp()
	}
	function ocultar_impares(){
		var objetos=$(".p_impar")
		objetos.slideUp()
	}


	function main(){

		$("#mostrar_pares").click(mostrar_pares)
		$("#mostrar_impares").click(mostrar_impares)
		
		$("#ocultar_pares").click(ocultar_pares)
		$("#ocultar_impares").click(ocultar_impares)
		
	}

	
	

Existen diversos eventos aunque los más utilizados son:

* ``click``

* ``dblclick``

* ``mouseover``

Ejercicio
------------------------------------------------------
Crear un programa que tenga varios párrafos con 4 botones que permitan que cuando se haga click en ellos ocurran distintas cosas

* Habrá un botón con el texto "Ocultar pares". Cuando se hace click en él se ocultan los párrafos pares.
* Habrá un botón con el texto "Ocultar impares". Cuando se hace click en él se ocultan los párrafos impares.
* Habrá un botón con el texto "Mostrar pares". Cuando se hace click en él se muestran los párrafos pares (que tal vez estaban ocultos).
* Habrá un botón con el texto "Mostrar impares". Cuando se hace click en él se muestran los párrafos impares (que tal vez estaban ocultos).


Ejercicio
---------

Crear una página en la que hay un div con texto y al pasar el ratón por encima de ella, la caja cambia de color.

Antes de poder resolver este ejercicio, hay que echar un vistazo a varias posibilidades de JQuery.


Procesado de atributos
======================

En JQuery sabemos que podemos procesar elementos utilizando su ``id`` con cosas como esta:

.. code-block:: javascript

	var objeto=$("#identificador1")
	objeto.metodo( ... )
	
	
Una de las cosas que se puede hacer es leer y escribir diversos atributos de los objetos. Además, se pueden leer propiedades especiales como comprobar si un radio o un checkbox están en el estado ``checked``.

Supongamos este formulario:

.. code-block:: html

	<form>
        <input type="radio" name="sexo" value="h" id="opc_h">Hombre
        <br/>
        <input type="radio" name="sexo" value="m" id="opc_m">Mujer
        <br/>
        <input type="text" id="informe">
        <br/>
        <input type="checkbox" name="medios[]" id="bus">Autobús
        <br/>
        <input type="checkbox" name="medios[]" id="coche">Coche
        <br/>
        <input type="checkbox" name="medios[]" id="moto">Moto        
        <br/>
        <input type="checkbox" name="medios[]" id="bici">Bici
        <br/>
        <input type="checkbox" name="medios[]" id="tren">Tren
        <br/>
        
    </form>
	
Podemos usar el método ``val`` para cambiar el valor de un objeto cualquiera:

.. code-block:: javascript

	function inicio(){
		var opc_h=$("#opc_h")
		opc_h.click ( click_hombre )
		
		var opc_m=$("#opc_m")
		opc_m.click ( click_mujer )
	}

	function click_hombre() {
		var cuadro_texto=$("#informe")
		cuadro_texto.val("Bienvenido Sr.")
	}

	function click_mujer(){
		var cuadro_texto=$("#informe")
		cuadro_texto.val("Bienvenido Sra/Srta.")
	}
	
Por ejemplo, en los checkboxes y en los radios, podemos comprobar si uno de ellos está marcado comprobando la propiedad "checked" con el método ``prop``.

Supongamos que deseamos saber cuantos checkboxes se marcan. Si se marcan cero, una o dos, mostraremos el texto "poca variedad", si se marcan tres mostraremos "cierta variedad" y si se marcan cuatro o cinco, mostraremos "mucha variedad".


Aquí hay dos posibles soluciones, siendo una de ellas  más corta y flexible que la otra.

La primera:

.. code-block:: javascript

    var opc_coche=$("#coche")
    opc_coche.click ( cuantas_pulsadas )
    
    var opc_moto=$("#moto")
    opc_moto.click ( cuantas_pulsadas )
    
    var opc_bici=$("#bici")
    opc_bici.click ( cuantas_pulsadas )
    
    var opc_bus=$("#bus")
    opc_bus.click ( cuantas_pulsadas )
    
    var opc_tren=$("#tren")
    opc_tren.click ( cuantas_pulsadas )
	
	function cuantas_pulsadas(){
		//Aquí contaríamos cuantas tienen la propiedad checked
	}




El segundo implica que todos los controles tengan el mismo atributo ``class``. Ahora la solución tendría un HTML como este:

.. code-block:: html

		<input type="checkbox" name="medios[]" id="bus" class="medio">Autobús
        <br/>
        <input type="checkbox" name="medios[]" id="coche" class="medio">Coche
        <br/>
        <input type="checkbox" name="medios[]" id="moto" class="medio">Moto        
        <br/>
        <input type="checkbox" name="medios[]" id="bici" class="medio">Bici
        <br/>
        <input type="checkbox" name="medios[]" id="tren" class="medio">Tren
        <br/>
		
Y el JS sería así:


.. code-block:: javascript

	var medios_de_locomocion=$(".medio")
    medios_de_locomocion.click ( cuantas_pulsadas )
	function cuantas_pulsadas(){
		var cuantas_marcadas=0
		var vector_ids=["#bus", "#coche", "#moto", "#bici", "#tren"]
		
		for (pos in vector_ids){
			var objeto = $( vector_ids[pos] )
			if (objeto.prop("checked")) {
				cuantas_marcadas=cuantas_marcadas+1
			}
		}
		
		if ((cuantas_marcadas>=0 ) && (cuantas_marcadas<=2)){
			alert ("Poca variedad")
		}
		if (cuantas_marcadas==3) {
			alert ("Variedad media")
		}
		if (cuantas_marcadas>=4){
			alert ("Mucha variedad")
		}   
	}
	
Ejercicio: recuento de medios de locomoción
------------------------------------------------------
Crear un programa que permita al usuario indicar cinco posibles medios de locomoción (usar checkboxes), a saber:coche, moto, bus, tren y avión. El programa debe contabilizar cuantos se usan en informar del número de medios usados en un textbox.

Solución: recuento de medios (HTML)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

		<div class="ui-grid-d">
            <div class="ui-block-a">
                <input type="checkbox"
                       name="medio"
                       id="coche">
                <label for="coche">Coche</label>
            </div>
            <div class="ui-block-b">
                <input type="checkbox"
                       name="medio"
                       id="moto">
                <label for="moto">Moto</label>
            </div>
            <div class="ui-block-c">
                <input type="checkbox"
                       name="medio"
                       id="bus">
                <label for="bus">Bus</label>
            </div>
            <div class="ui-block-d">
                <input type="checkbox"
                       name="medio"
                       id="tren">
                <label for="tren">Tren</label>
            </div>
            <div class="ui-block-e">
                <input type="checkbox"
                       name="medio"
                       id="avion">
                <label for="avion">Avión</label>
            </div>
        </div>
        <input type="text" id="informe">
		
Solución: recuento de medios (JS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Variante 1: Sin vectores, implica usar muchos ``if``. Aunque funcione supone cortar y pegar, que aunque en este caso no sea un trabajo muy grande nos obliga a adoptar malos hábitos

.. code-block:: javascript

	$(document).ready(main)

	function contar(){
		var contador=0
		
		if ($("#coche").prop("checked"))
		{
			contador=contador+1
		}
		if ($("#moto").prop("checked"))
		{
			contador=contador+1
		}
		var mensaje="Medios:"+contador
		$("#informe").val(mensaje)
		
	}

	function main(){
		$("#coche").click(contar)
		$("#moto").click(contar)
		$("#bus").click(contar)
		$("#tren").click(contar)
		$("#avion").click(contar)
		
	}
	

Variante 2: Con vectores

.. code-block:: javascript

	$(document).ready(main)
	function contar(){
		var contador=0
		var ids=new Array()
		var ids=["#coche", "#moto",
				 "#bus", "#tren",
				 "#avion"]
		
		for (pos in ids){
			var medio=$(ids[pos])
			if (medio.prop("checked"))
			{
				contador=contador+1
			}
		}
		var mensaje="Medios:"+contador
		$("#informe").val(mensaje)
		
	}

	function main(){
		$("#coche").click(contar)
		$("#moto").click(contar)
		$("#bus").click(contar)
		$("#tren").click(contar)
		$("#avion").click(contar)
	}	

	
Ejercicio configurador
------------------------------------------------------

Se desea tener una aplicación que permita configurar un equipo al gusto del usuario:

* Se debe elegir entre un procesador Intel o AMD. El primero cuesta 250 euros y el segundo 230.
* Se debe elegir entre 2, 4 y 8 GB de memoria. El coste es respectivamente 90, 145, 210
* Hay extras que se pueden elegir o no, ya que son completamente optativos (es decir, usar checkboxes). En concreto se puede tener un grabador de Blu-ray (190 euros), tarjeta gráfica aceleradora (430 euros) y un monitor LED (185 euros).
	
	
Solución HTML configurador
------------------------------------------------------	

.. code-block:: html

	<label for="intel">Intel i5</label>
	<input type="radio"
               name="procesador" id="intel">
        <label for="amd">AMD</label>
        <input type="radio"
               name="procesador" id="amd">
        <label for="2gb">2GB</label>
        <input type="radio"
               name="memoria" id="2gb">
        <label for="4gb">4 GB</label>
        <input type="radio"
               name="memoria" id="4gb">
        <label for="8gb">8 GB</label>
        <input type="radio"
               name="memoria" id="8gb">
        <label for="bluray">Blu-ray</label>
        <input type="checkbox" name="extra[]"
               id="bluray">
        <label for="aceleradora">Aceleradora</label>
        <input type="checkbox" name="extra[]"
               id="aceleradora">
        <label for="monitor">Monitor 25</label>
        <input type="checkbox" name="extra[]"
               id="monitor">
        <input type="text" id="total">

	
Solución JS configurador
------------------------------------------------------

.. code-block:: javascript

	$(document).ready(main)

	function calcular_precio(){
		var precio=0
		if ($("#intel").prop("checked")) {
			precio=precio+250
		}
		if ($("#amd").prop("checked")) {
			precio=precio+210
		}
		if ($("#2gb").prop("checked")) {
			precio=precio+90
		}
		if ($("#4gb").prop("checked")) {
			precio=precio+140
		}
		if ($("#8gb").prop("checked")) {
			precio=precio+210
		}
		if ($("#bluray").prop("checked")) {
			precio=precio+190
		}
		if ($("#aceleradora").prop("checked")) {
			precio=precio+430
		}
		if ($("#monitor").prop("checked")) {
			precio=precio+185
		}
		
		$("#total").val(precio)
	}
	function main(){
		$("#intel").click (calcular_precio)
		$("#amd").click (calcular_precio)
		
		$("#2gb").click (calcular_precio)
		$("#4gb").click (calcular_precio)
		$("#8gb").click (calcular_precio)
		
		$("#bluray").click (calcular_precio)
		$("#monitor").click (calcular_precio)
		$("#aceleradora").click (calcular_precio)
	}		

	
Ejercicio configurador de PCs ampliado
------------------------------------------------------
En el ejercicio anterior ocurre que por un problema hardware no es posible tener procesadores AMD con aceleradora, por lo que cuando se marque un AMD se debe desactivar el checkbox de la aceleradora y si hubiera una marca, también se debe desactivar y por supuesto recalcular el precio.


Configurador de coches
===================================================
Un fabricante de automóviles desea ofrecer a sus clientes una aplicación que les permita configurar sus vehículos según sus preferencias y ver el precio final del coche. Los precios y las restricciones son los siguientes:

* Se pueden tener dos tipos de motor: gasolina (precio base 7000 euros) y diésel (precio base 8200).
* Se pueden tener 3 potencias: 1100, 1800 y 2300 centímetros cúbicos. Los precios de cada uno son 800, 1900 y 2500. Sin embargo **no es posible fabricar motores diésel de 2300**.
* Hay dos tipos de pintura: normal y metalizada. Los precios respectivos son 750 y 1580 euros.
* Hay seis colores: negro, blanco, rojo, azul polar, verde turquesa y gris marengo. **No se pueden fabricar colores de pintura normal de ninguno de los tres últimos colores**.
* Se dispone de diversos extras: alerón deportivo (190 euros **pero solo se puede elegir si se elige pintura metalizada**), radio-CD con MP3 (230 euros más), altavoces traseros (320 euros más, **pero solo si se elige antes el Radio-CD**), y GPS incorporado (520 euros más).



Crear la aplicación que respete las restricciones exigidas por el cliente.

HTML del configurador
----------------------

JS del configurador (con JQuery (DAM))
-----------------------------------------



Dinamismo con Google Maps
=========================

Google Maps ofrece un servicio de mapas con una limitación de 25.000 peticiones diarias. El código básico sería así:

HTML de GMaps
-------------

.. code-block:: html

	<!DOCTYPE html>

	<html>
	<head>
		<!--En móviles poner la escala inicial a 1-->
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<!--Cargamos los estilos y los efectos de Bootstrap-->
		<link 
		rel="stylesheet" 
		type="text/css" href="bootstrap/css/bootstrap.css"/>
		<script src="bootstrap/js/bootstrap.js"></script>
		<script src="js/jquery.js"></script>
		<script 
		src="http://maps.googleapis.com/maps/api/js?key=AIzaSyDpv9zCj9szIIu--LuNmDsry2fZCRrOqfY&sensor=false">
			
		</script>
		<style>
			#mapa{
				width: 500px;
				height: 500px;
				float: right;
				background-color: rgb(180,190,240);
			}
			#controles{
				float: left;
			}
		</style>
		<script src="js/programa.js"></script>
		<title>Plantilla JQuery</title>
	</head>

	<body>
	<div class="container">
		<h1>Javascript con mapas</h1>
			<div id="controles">
				Introduzca latitud:<input type="text" id="latitud">
				<br/>
				Introduzca longitud:<input type="text" id="longitud">
				<br/>
				<input type="submit" id="mover" value="¡Viajar!">
				<select id="ciudades">
					<option value="CR">Ir a Ciudad Real</option>
					<option value="BA">Ir a Barcelona</option>
					<option value="PO">Ir a Pontevedra</option>
				</select>
				<br/>
				Calculador de distancias desde CR a otras ciudades
				<select id="ciudades">
					<option value="CR">Ir a Ciudad Real</option>
					<option value="BA">Ir a Barcelona</option>
					<option value="PO">Ir a Pontevedra</option>
				</select>
		</div>
		<div id="mapa">
			
		</div>
	</div>

	</body>
	</html>

Javascript de GMaps
-------------------

.. code-block:: javascript


	var latitud=38.59
	var longitud=-3.55
	var mi_nivel_de_zoom=8
	var obj_mapa
	function inicio(){
		var div_mapa=document.getElementById("mapa")
		var obj_coordenadas=new google.maps.LatLng(latitud,longitud)
		var obj_opciones={
			center:obj_coordenadas,
			zoom:mi_nivel_de_zoom
		}
		obj_mapa=new google.maps.Map(div_mapa, obj_opciones)
		
		$("#mover").click (mover_el_mapa)
	}


	function mover_el_mapa() {
		var obj_latitud=$("#latitud")
		var valor_latitud=obj_latitud.val()
		
		var valor_longitud=$("#longitud").val()
		var nuevas_coordenadas=new google.maps.LatLng(
					valor_latitud, valor_longitud)
		obj_mapa.panTo(nuevas_coordenadas)
	}
	

Ejercicio
---------

Ampliar el programa con una lista de ciudades del mundo. Cuando el usuario elija una de ellas, nuestro programa nos dirá la distancia desde Ciudad Real a dichas ciudades. Considerar las siguientes coordenadas en formato (latitud, longitud):

* Ciudad Real: (38.59, -3.55)
* Nueva York: (40.73, -73.87)
* Sidney: (-33.90, 151.13)
* Berlin: (52.31, 13.39)
* París: (48.85, 2.35)

Para poder conseguir esto, hay que modificar la URL de carga de GoogleMaps para solicitar que se cargue una biblioteca que nos ayudará a resolver este punto. En concreto, ahora pasaremos un parámetro ``libraries`` con el valor ``geometry`` que nos permitirá utilizar la biblioteca en concreto. Ahora el HTML es así:

.. code-block:: html

	<script src="http://maps.googleapis.com/maps/api/js?key=AIzaSyDpv9zCj9szIIu--LuNmDsry2fZCRrOqfY&sensor=false&libraries=geometry">
        
    </script>
	
Ahora una función que nos calcula la distancia sería algo como esto:

.. code-block:: javascript

	/* Nos da la distancia en metros entre CR 
	 * y el punto (latitud_destino,longitud_destino)
	 * (abreviados lat_dest y lng_dest)*/
	function distancia(lat_dest, lng_dest)
	{
		var latitud_cr=38.59
		var longitud_cr=-3.55
		var coords_origen=new google.maps.LatLng(
			latitud_cr, longitud_cr)
		var coords_destino=new google.maps.LatLng(
			lat_dest, lng_dest)
		var distancia=google.maps.geometry.spherical.computeDistanceBetween(
			coords_origen, coords_destino
		)
		return distancia
	}

	
Ejercicio
---------

La empresa Automobile Creation for Millenium Enterprise (ACME) planea lanzar una página web en la que se permita al usuario configurar los coches a su medida, ofreciendo las distintas opciones en pantalla para que el usuario las elija. Sin embargo no todas las combinaciones se permiten en fábrica por lo que deberán tenerse en cuentas las siguientes

Especificaciones
~~~~~~~~~~~~~~~~

* Hay dos motores: gasolina (5000) y diésel (6800)
* Hay dos carrocerías: monovolumen (4500) y berlina (3700)
* Hay tres accesorios: radio-cd con MP3 (180), alerones deportivos (220) y llantas de aleación (200)

Por diversos problemas, no es posible combinar las siguientes opciones:

* No se pueden tener berlinas de gasolina.
* No se puede integrar el alerón en los monovolúmenes.
* No se puede poner el radio-cd a los monovolúmenes.

Cuando se marque cualquiera de estas opciones, hay que limpiar todo el configurados y avisar de que no se puede hacer eso. No se pueden usar ``alerts``

.. code-block:: javascript

	var vector_ids=["#gasolina", "#diesel", "#monovolumen",
			"#berlina", "#radiocd", "#alerones", "#llantas"]
	var precios=[5000, 6800, 4500,
			3700, 180, 220, 200]

	function inicio(){
	 
		for (var pos in vector_ids){
			var el_id=vector_ids[pos]
			$(el_id).click ( calcularPrecio )
		}
	}

	function cocheEsFabricable() {
		//Caso 1: nada de berlinas de gasolina
		var marcada_la_berlina=$("#berlina").prop("checked")
		var marcada_la_gasolina=$("#gasolina").prop("checked")
		if (marcada_la_berlina && marcada_la_gasolina) {
			alert ("No se pueden fabricar berlinas de gasolina")
			return false
		}
		
		var marcado_aleron=$("#alerones").prop("checked")
		var marcado_monovolumen=$("#monovolumen").prop("checked")
		if (marcado_aleron && marcado_monovolumen ) {
			alert ("No podemos integrar los alerones en monovolúmenes")
			return false
		}
		
		var marcado_radiocd=$("#radiocd").prop("checked")
		if (marcado_radiocd && marcado_monovolumen) {
			alert ("No podemos fabricar un monovol. con radio-cd")
			return false
		}
		return true
	}
	/* Calcula el precio del coche en función de lo que esté marcado
	 * y lo que no.*/
	function calcularPrecio() {
		var todo_bien=cocheEsFabricable()
		if (todo_bien!=true) {
			return 
		}
		var precioCoche=0
		for (var pos in vector_ids){
			var el_id=vector_ids[pos]       
			if ($(el_id).prop("checked")) {
				var precio_accesorio=precios[pos]
				precioCoche=precioCoche+precio_accesorio
			}
		}
		alert ("El precio es:"+precioCoche)
	}
	
Ampliación
----------

Se desea que el usuario puede elegir entre los siguientes colores con los siguientes precios:

* Blanco: 700 euros
* Rojo, Verde y Azul básicos: 950
* Gris, Negro y Naranja: 1400 euros por ser colores metalizados

Además, se desea ver una muestra de color en algún punto de la página. Para lograrlo se necesitará utilizar un método que proporciona JQuery y que se llama ``addClass``

Solución HTML
~~~~~~~~~~~~~

.. code-block:: html

	<head>
		<style>
			.muestrarojo{
				background-color:red;
			}
			.muestraverde{
				background-color: green;
			}
			.muestraazul{
				background-color: blue;
			}
			.muestragris{
				background-color: grey;
			}
			.muestrablanco{
				background-color: white;
			}
		</style>
	</head>
	<body>
		<div class="container">
			<h1>Motores</h1>
			<input type="radio" id="gasolina" name="motor">Motor Gasolina
			<br/>
			<input type="radio" id="diesel" name="motor">Motor Diésel
			<br/>
			<h1>Carrocerías</h1>
			<input type="radio" id="monovolumen"
			name="carroceria">Monovolumen
			<br/>
			<input type="radio" id="berlina" name="carroceria">Berlina
			<br/>
			<h1>Accesorios</h1>
			<input type="checkbox" name="accesorios[]" 
			id="radiocd">Radio-CD
			<br/>
			<input type="checkbox" name="accesorios[]" 
			id="alerones">Alerones
			<br/>
			<input type="checkbox" name="accesorios[]" 
			id="llantas">Llantas
			<br/>
			<h1>Colores</h1>
			<!--Los colores irán 
			en una columna y la muestra en otra-->
			<div class="row">
				<div class="col-md-3">
					<input type="radio"
					name="colores" 
					id="blanco">Blanco
					<br/>
					<input type="radio"
					name="colores" 
					id="rojo">Rojo
					<br/>
					<input type="radio"
					name="colores" id="gris">Gris        
				</div>
				<div class="col-md-9 center-block">
					<h2>Muestra de color
					<small>Observe y compare</small></h2>
				</div>
			</div><!--Fin de la fila-->
		</div>
	</body>
	
Solución JS
~~~~~~~~~~~~

Añadiremos este código a nuestro programa anterior.

.. code-block:: javascript

	var obj_documento = $(document)
	obj_documento.ready(inicio)

	var vector_ids=["#gasolina", "#diesel", "#monovolumen",
			"#berlina", "#radiocd", "#alerones", "#llantas"]
	var precios=[5000, 6800, 4500,
			3700, 180, 220, 200]

	function inicio(){
	 
		for (var pos in vector_ids){
			var el_id=vector_ids[pos]
			$(el_id).click ( calcularPrecio )
		}
		$("#blanco").click ( ponerColorBlanco )
		$("#rojo").click ( ponerColorRojo )
		$("#gris").click (ponerGris )
	}
	function limpiarColores(){
		var clases=["muestrarojo", "muestrablanco",
					"muestragris"]
		for (var pos in clases) {
			$("#muestra").removeClass( clases[pos] )
		}
	}
	function ponerGris() {
		limpiarColores()
		$("#muestra").addClass("muestragris")
	}
	function ponerColorRojo(){
		limpiarColores()
		$("#muestra").addClass ("muestrarojo")
	}
	function ponerColorBlanco(){
		limpiarColores()
		$("#muestra").addClass ("muestrablanco")
	}

	
Otro configurador de coches
==============================
Sin utilizar JQuery se desea crear un configurador de coches en JS que responda a las siguientes premisas:

* Hay dos modelos a elegir: el modelo A cuesta 7000 euros y el modelo B cuesta 9000.
* Se pueden elegir dos tipos de motor. El motor de gasolina cuesta 2000 y el diésel 5000 euros.

* Se pueden elegir 0, 1, muchos o todos los extras siguientes: Pintura metalizada por 1000 euros más, pack de sonido por 500 euros más y pack de seguridad por 1000 euros más

Configurador en HTML
--------------------

.. code-block:: html

	<form>
		<h3>Elija un modelo</h3>
		<input type="radio" name="modelo"
			   id="modelo_a">Modelo A<br/>
		<input type="radio" name="modelo"
			   id="modelo_b">Modelo B<br/>
		<h3>Elija un tipo de motor</h3>
		<input type="radio" name="motor"
			   id="gasolina">Gasolina<br/>
		<input type="radio" name="motor"
			   id="diesel">Diésel<br/>
		<h3>Elija extras</h3>
		<input type="checkbox" name="extras"
			   id="metalizada">Pintura metalizada<br/>
		<input type="checkbox" name="extras"
			   id="sonido">Extra sonido<br/>
		<input type="checkbox" name="extras"
			   id="seguridad">Extra seguridad<br/>
		<input type="submit" value="Calcular"
			   onclick="calcular();return false;">
	</form>
	<div id="zonaresultados"></div>

Configurador en JS
--------------------

.. code-block:: javascript

	function esta_checked(id){
		var control;
		control=document.getElementById(id);
		if (control.checked){
			return true;
		} else {
			return false;
		}
	}

	function calcular(){
		var preciototal   =0;
		var preciomodelo  =0;
		var preciomotor   =0;
		var precioextras  = 0;
		if ( (!esta_checked("modelo_a"))
			&& (!esta_checked("modelo_b") ) ){
			alert("Debe marcar un modelo");
			return ;
		}
		if (esta_checked("modelo_a")){
			preciomodelo=7000;
		}
		if (esta_checked("modelo_b")){
			preciomodelo=9000;
		}
		if (esta_checked("gasolina")){
			preciomotor=2000;
		}
		if (esta_checked("diesel")){
			preciomotor=4000;
		}
		if (esta_checked("metalizada")){
			precioextras=1000;
		}
		if (esta_checked("sonido")){
			precioextras=precioextras+500;
		}
		if (esta_checked("seguridad")){
			precioextras=precioextras+1000;
		}
		preciototal=preciomodelo+preciomotor+precioextras;
		
		var zonaresultados;
		zonaresultados=document.getElementById(
			"zonaresultados");
		zonaresultados.innerHTML="Precio:"+preciototal;   
	}

Calculo de impuestos
=======================

Se desea crear una pequeña aplicación web que permita calcular los impuestos que se deben pagar a partir de unos datos, en concreto:

* Se debe introducir el salario anual en un campo de tipo ``number``.
* Hay dos radios que permiten indicar si el contribuyente tiene hijos o no.
* Hay dos checkboxes que permiten saber si el contribuyente tiene derecho a algunas modificaciones llamadas B1 y B2.

Las reglas para el calculo son:

* Si el salario es menor de 20000 los impuestos son 0.
* Si el salario está entre 20001 y 30000 los impuestos son el 10%.
* Si el salario está entre 30001 y 50000 los impuestos son el 20%.
* Si el salario es mayor de 50000 se paga el 38%
* Si se tienen hijos los impuestos se reducen en 180 euros.
* Si se tiene la bonificación B1 los impuestos se reducen en 355 euros.
* Si se tiene la bonificación B2 los impuestos se reducen en 560 euros.
* Se recuerda que las bonificaciones B1 y B2 son compatibles (de hecho hemos dicho que están en checkboxes).
* La cantidad de impuestos puede ser negativa (que significa que le sale "a devolver")

HTML calculador
---------------

.. literalinclude:: ejercicios/js/calculo_impuestos_con_jquery/index.html
   :language: html
   
   
JS Calculador (con JQuery (DAM))
----------------------------------
.. literalinclude:: ejercicios/js/calculo_impuestos_con_jquery/js/programa.js
   :language: javascript
   
JS Calculador (sin JQuery (ASIR))
----------------------------------
.. literalinclude:: ejercicios/js/calculo_impuestos_sin_jquery/js/programa.js
   :language: javascript

Comparador de telefonía
===========================

Se desea crear una aplicación que permita al usuario saber qué compañía de telefonía le conviene más partiendo de los siguientes datos

* La empresa A ofrece una tarifa que cuesta 20 euros al mes con los 1000 primeros minutos gratis y despues cada minuto cuesta 8 céntimos.

* La empresa B ofrece una tarifa que cuesta 10 euros al mes con los 500 primeros minutos gratis y despues cada llamada cuesta 12 céntimos.

Hacer una aplicación que permita al usuario introducir la cantidad de minutos que llamará para tres meses distintos que llamaremos "Mes 1", "Mes 2" y "Mes 3"  y que le diga qué compañía le interesa más.

HTML del comparador
-----------------------

.. code-block:: html

	<form>
	Mes 1<input type="number" value="800"
				 min="0" max="5000" id="mes1"> <br/>
	Mes 2<input type="number" value="2000"
				 min="0" max="5000" id="mes2"> <br/>
	Mes 3<input type="number" value="600"
				 min="0" max="5000" id="mes3"> <br/>
	<input type="submit" value="¿Qué me conviene?"
				 onclick="calcular();return false">
	</form>
	
JS del comparador
--------------------

.. code-block:: javascript

	function extraer_numero(id){
		var control;
		control=document.getElementById(id);
		var valor=control.value;
		var numero=parseInt(valor);
		return numero;
	}

	function precio_mes_empresa_a(minutos){
		//Primero vemos si se pasa
		if (minutos<1000){
			//Si no se pasa, el precio es 20
			return 20;
		}
		//Si llegamos a este punto, es porque se pasa
		
		//Calculamos cuantos minutos se pasa
		var exceso=minutos-1000;
		//Y ese exceso es a 8 centimos/minutos
		var precio_exceso=exceso*0.08;
		//El precio de ese mes es
		//20 euros más lo que cueste el exceso
		var precio_mes=20+precio_exceso;
		//Devolvemos el calculo a quien lo pidiese
		return precio_mes;
	}

	function precio_mes_empresa_b(minutos){
		//Primero vemos si se pasa
		if (minutos<500){
			//Si no se pasa, el precio es 10
			return 10;
		}
		//Si llegamos a este punto, es porque se pasa
		
		//Calculamos cuantos minutos se pasa
		var exceso=minutos-500;
		//Y ese exceso es a 12 centimos/minutos
		var precio_exceso=exceso*0.12;
		//El precio de ese mes es
		//10 euros más lo que cueste el exceso
		var precio_mes=10+precio_exceso;
		//Devolvemos el calculo a quien lo pidiese
		return precio_mes;
	}

	function calcular(){
		var minutos_mes1;
		minutos_mes1=extraer_numero("mes1");
		var minutos_mes2;
		minutos_mes2=extraer_numero("mes2");
		var minutos_mes3;
		minutos_mes3=extraer_numero("mes3");
		
		var coste_mes1_empresa_a;
		coste_mes1_empresa_a=precio_mes_empresa_a(
			minutos_mes1);
		
		coste_mes2_empresa_a=precio_mes_empresa_a(
			minutos_mes2);
		coste_mes3_empresa_a=precio_mes_empresa_a(
			minutos_mes3);
		
		//Calculamos el precio que costaria
		//esos minutos en la empresa A
		var coste_total_a;
		coste_total_a=coste_mes1_empresa_a+coste_mes2_empresa_a+coste_mes3_empresa_a;
		
		//Repetimos el proceso para la empresa B
		var coste_mes1_empresa_b;
		coste_mes1_empresa_b=precio_mes_empresa_b(
			minutos_mes1);
		coste_mes2_empresa_b=precio_mes_empresa_b(
			minutos_mes2);
		coste_mes3_empresa_b=precio_mes_empresa_b(
			minutos_mes3);
		//Calculamos ahora el precio que costaria
		//esos minutos en la empresa B
		var coste_total_b;
		coste_total_b=coste_mes1_empresa_b+coste_mes2_empresa_b+coste_mes3_empresa_b;
		var zonaresultados;
		zonaresultados=document.getElementById("zonaresultados");
		var texto;
		texto="Con la A el precio es:" + coste_total_a;
		texto=texto+"<br/>";
		texto=texto+"Con la B el precio es:" + coste_total_b;   
		zonaresultados.innerHTML=texto
	}