
Anexo: ejercicios sobre "grids"
=====================================

Ejercicio 01
--------------------------------------------------


El siguiente archivo HTML tiene 3 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 11 filas y 11 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 01</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 11 columnas)
	<pre>
	33333333333
	33333333333
	22222222222
	22222222222
	22222222222
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F1**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F2**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F3**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F4**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F5**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F6**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F7**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F8**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F9**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F10** | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F11** | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+

Solución al grid (Ejercicio 01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 01</title>
	<meta charset="utf-8">
	<style>
	#contenedor{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#caja1{
		grid-row:     6/12;
		grid-column:  1/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja2{
		grid-row:     3/6;
		grid-column:  1/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja3{
		grid-row:     1/3;
		grid-column:  1/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 11 columnas)
	<pre>
	33333333333
	33333333333
	22222222222
	22222222222
	22222222222
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 02
--------------------------------------------------


El siguiente archivo HTML tiene 6 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 11 filas y 11 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 02</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 11 columnas)
	<pre>
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	33333222222
	33333222222
	33333222222
	55555222222
	44444222222
	44444222222
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4
	 </div>
	 <div id="caja5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5
	 </div>
	 <div id="caja6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6 Texto 6 Texto 6 Texto 6
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F6**  | 3        | 3        | 3        | 3        | 3        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F7**  | 3        | 3        | 3        | 3        | 3        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F8**  | 3        | 3        | 3        | 3        | 3        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F9**  | 5        | 5        | 5        | 5        | 5        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F10** | 4        | 4        | 4        | 4        | 4        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F11** | 4        | 4        | 4        | 4        | 4        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+

Solución al grid (Ejercicio 02)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 02</title>
	<meta charset="utf-8">
	<style>
	#contenedor{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#caja1{
		grid-row:     1/6;
		grid-column:  1/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja2{
		grid-row:     6/12;
		grid-column:  6/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja3{
		grid-row:     6/9;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja4{
		grid-row:     10/12;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja5{
		grid-row:     9/10;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja6{
		grid-row:     9/9;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 11 columnas)
	<pre>
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	33333222222
	33333222222
	33333222222
	55555222222
	44444222222
	44444222222
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4
	 </div>
	 <div id="caja5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5
	 </div>
	 <div id="caja6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6 Texto 6 Texto 6 Texto 6
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 03
--------------------------------------------------


El siguiente archivo HTML tiene 3 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 9 filas y 12 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 03</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 12 columnas)
	<pre>
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	</pre>
	<div id="contenedor">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |  **C12**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F1**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F2**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F3**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F4**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F5**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F6**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F7**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F8**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F9**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+

Solución al grid (Ejercicio 03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 03</title>
	<meta charset="utf-8">
	<style>
	#contenedor{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#columna1{
		grid-row:     1/10;
		grid-column:  7/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna2{
		grid-row:     1/10;
		grid-column:  1/4;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna3{
		grid-row:     1/10;
		grid-column:  4/7;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 12 columnas)
	<pre>
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	</pre>
	<div id="contenedor">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 04
--------------------------------------------------


El siguiente archivo HTML tiene 4 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 11 filas y 12 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 04</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 12 columnas)
	<pre>
	111111111111
	111111111111
	111111111111
	111111111111
	111111111111
	222222222222
	222222222222
	222222222222
	333333444444
	333333444444
	333333444444
	</pre>
	<div id="contenedorglobal">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |  **C12**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F6**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F7**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F8**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F9**  | 3        | 3        | 3        | 3        | 3        | 3        | 4        | 4        | 4        | 4         | 4         | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F10** | 3        | 3        | 3        | 3        | 3        | 3        | 4        | 4        | 4        | 4         | 4         | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F11** | 3        | 3        | 3        | 3        | 3        | 3        | 4        | 4        | 4        | 4         | 4         | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+

Solución al grid (Ejercicio 04)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 04</title>
	<meta charset="utf-8">
	<style>
	#contenedorglobal{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#caja1{
		grid-row:     1/6;
		grid-column:  1/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja2{
		grid-row:     6/9;
		grid-column:  1/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja3{
		grid-row:     9/12;
		grid-column:  1/7;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja4{
		grid-row:     9/12;
		grid-column:  7/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 12 columnas)
	<pre>
	111111111111
	111111111111
	111111111111
	111111111111
	111111111111
	222222222222
	222222222222
	222222222222
	333333444444
	333333444444
	333333444444
	</pre>
	<div id="contenedorglobal">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 05
--------------------------------------------------


El siguiente archivo HTML tiene 5 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 9 filas y 9 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 05</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	333355555
	333344444
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2 Te
		xto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4
	 </div>
	 <div id="bloque5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F5**  | 3        | 3        | 3        | 3        | 5        | 5        | 5        | 5        | 5        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F6**  | 3        | 3        | 3        | 3        | 4        | 4        | 4        | 4        | 4        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F7**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F8**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F9**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Solución al grid (Ejercicio 05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 05</title>
	<meta charset="utf-8">
	<style>
	#container{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#bloque1{
		grid-row:     1/5;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque2{
		grid-row:     7/10;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque3{
		grid-row:     5/7;
		grid-column:  1/5;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque4{
		grid-row:     6/7;
		grid-column:  5/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque5{
		grid-row:     5/6;
		grid-column:  5/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	333355555
	333344444
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2 Te
		xto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4
	 </div>
	 <div id="bloque5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 06
--------------------------------------------------


El siguiente archivo HTML tiene 5 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 10 filas y 12 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 06</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 12 columnas)
	<pre>
	111111355222
	111111355222
	111111355222
	111111355222
	111111355222
	111111344222
	111111344222
	111111344222
	111111344222
	111111344222
	</pre>
	<div id="contenedorglobal">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4
	 </div>
	 <div id="columna5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |  **C12**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 5        | 5        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 5        | 5        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 5        | 5        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 5        | 5        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 5        | 5        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F6**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 4        | 4        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F7**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 4        | 4        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F8**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 4        | 4        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F9**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 4        | 4        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F10** | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 4        | 4        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+

Solución al grid (Ejercicio 06)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 06</title>
	<meta charset="utf-8">
	<style>
	#contenedorglobal{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#columna1{
		grid-row:     1/11;
		grid-column:  1/7;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna2{
		grid-row:     1/11;
		grid-column:  10/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna3{
		grid-row:     1/11;
		grid-column:  7/8;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna4{
		grid-row:     6/11;
		grid-column:  8/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna5{
		grid-row:     1/6;
		grid-column:  8/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 12 columnas)
	<pre>
	111111355222
	111111355222
	111111355222
	111111355222
	111111355222
	111111344222
	111111344222
	111111344222
	111111344222
	111111344222
	</pre>
	<div id="contenedorglobal">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4
	 </div>
	 <div id="columna5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 07
--------------------------------------------------


El siguiente archivo HTML tiene 5 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 10 filas y 9 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 07</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	111111111
	222222222
	222222222
	444455555
	333333333
	333333333
	</pre>
	<div id="contenedor">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4
	 </div>
	 <div id="columna5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F6**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F7**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F8**  | 4        | 4        | 4        | 4        | 5        | 5        | 5        | 5        | 5        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F9**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F10** | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Solución al grid (Ejercicio 07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 07</title>
	<meta charset="utf-8">
	<style>
	#contenedor{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#columna1{
		grid-row:     1/6;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna2{
		grid-row:     6/8;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna3{
		grid-row:     9/11;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna4{
		grid-row:     8/9;
		grid-column:  1/5;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna5{
		grid-row:     8/9;
		grid-column:  5/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	111111111
	222222222
	222222222
	444455555
	333333333
	333333333
	</pre>
	<div id="contenedor">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4
	 </div>
	 <div id="columna5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 08
--------------------------------------------------


El siguiente archivo HTML tiene 6 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 12 filas y 9 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 08</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (12 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	111111111
	111111111
	333333333
	444444444
	555566666
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4
	 </div>
	 <div id="columna5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5
	 </div>
	 <div id="columna6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F6**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F7**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F8**  | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F9**  | 5        | 5        | 5        | 5        | 6        | 6        | 6        | 6        | 6        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F10** | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F11** | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F12** | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Solución al grid (Ejercicio 08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 08</title>
	<meta charset="utf-8">
	<style>
	#container{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#columna1{
		grid-row:     1/7;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna2{
		grid-row:     10/13;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna3{
		grid-row:     7/8;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna4{
		grid-row:     8/9;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna5{
		grid-row:     9/10;
		grid-column:  1/5;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna6{
		grid-row:     9/10;
		grid-column:  5/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (12 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	111111111
	111111111
	333333333
	444444444
	555566666
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4
	 </div>
	 <div id="columna5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5
	 </div>
	 <div id="columna6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 09
--------------------------------------------------


El siguiente archivo HTML tiene 5 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 12 filas y 11 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 09</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (12 filas y 11 columnas)
	<pre>
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	55555333333
	44444333333
	44444333333
	22222222222
	22222222222
	22222222222
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4
	 </div>
	 <div id="caja5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F6**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F7**  | 5        | 5        | 5        | 5        | 5        | 3        | 3        | 3        | 3        | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F8**  | 4        | 4        | 4        | 4        | 4        | 3        | 3        | 3        | 3        | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F9**  | 4        | 4        | 4        | 4        | 4        | 3        | 3        | 3        | 3        | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F10** | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F11** | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F12** | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+

Solución al grid (Ejercicio 09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 09</title>
	<meta charset="utf-8">
	<style>
	#contenedor{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#caja1{
		grid-row:     1/7;
		grid-column:  1/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja2{
		grid-row:     10/13;
		grid-column:  1/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja3{
		grid-row:     7/10;
		grid-column:  6/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja4{
		grid-row:     8/10;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja5{
		grid-row:     7/8;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (12 filas y 11 columnas)
	<pre>
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	11111111111
	55555333333
	44444333333
	44444333333
	22222222222
	22222222222
	22222222222
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4
	 </div>
	 <div id="caja5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 10
--------------------------------------------------


El siguiente archivo HTML tiene 6 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 9 filas y 11 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 10</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 11 columnas)
	<pre>
	11111111111
	11111111111
	11111111111
	11111111111
	66666444444
	66666333333
	55555222222
	55555222222
	55555222222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4
	 </div>
	 <div id="bloque5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5
	 </div>
	 <div id="bloque6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6 Texto 6 Texto 6 Texto 6 
		Texto 6 Texto 6 Texto 6
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F5**  | 6        | 6        | 6        | 6        | 6        | 4        | 4        | 4        | 4        | 4         | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F6**  | 6        | 6        | 6        | 6        | 6        | 3        | 3        | 3        | 3        | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F7**  | 5        | 5        | 5        | 5        | 5        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F8**  | 5        | 5        | 5        | 5        | 5        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+
|  **F9**  | 5        | 5        | 5        | 5        | 5        | 2        | 2        | 2        | 2        | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+

Solución al grid (Ejercicio 10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 10</title>
	<meta charset="utf-8">
	<style>
	#container{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#bloque1{
		grid-row:     1/5;
		grid-column:  1/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque2{
		grid-row:     7/10;
		grid-column:  6/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque3{
		grid-row:     6/7;
		grid-column:  6/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque4{
		grid-row:     5/6;
		grid-column:  6/12;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque5{
		grid-row:     7/10;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque6{
		grid-row:     5/7;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 11 columnas)
	<pre>
	11111111111
	11111111111
	11111111111
	11111111111
	66666444444
	66666333333
	55555222222
	55555222222
	55555222222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4
	 </div>
	 <div id="bloque5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5
	 </div>
	 <div id="bloque6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6 Texto 6 Texto 6 Texto 6 
		Texto 6 Texto 6 Texto 6
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 11
--------------------------------------------------


El siguiente archivo HTML tiene 5 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 12 filas y 12 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 11</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (12 filas y 12 columnas)
	<pre>
	555555555555
	555555555555
	555555555555
	444444444444
	444444444444
	444444444444
	111111333333
	111111333333
	111111333333
	111111222222
	111111222222
	111111222222
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4
	 </div>
	 <div id="caja5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |  **C12**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F1**  | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5         | 5         | 5         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F2**  | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5         | 5         | 5         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F3**  | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5        | 5         | 5         | 5         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F4**  | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4         | 4         | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F5**  | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4         | 4         | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F6**  | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4         | 4         | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F7**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F8**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F9**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F10** | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F11** | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F12** | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+

Solución al grid (Ejercicio 11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 11</title>
	<meta charset="utf-8">
	<style>
	#contenedor{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#caja1{
		grid-row:     7/13;
		grid-column:  1/7;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja2{
		grid-row:     10/13;
		grid-column:  7/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja3{
		grid-row:     7/10;
		grid-column:  7/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja4{
		grid-row:     4/7;
		grid-column:  1/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja5{
		grid-row:     1/4;
		grid-column:  1/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (12 filas y 12 columnas)
	<pre>
	555555555555
	555555555555
	555555555555
	444444444444
	444444444444
	444444444444
	111111333333
	111111333333
	111111333333
	111111222222
	111111222222
	111111222222
	</pre>
	<div id="contenedor">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3
	 </div>
	 <div id="caja4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4
	 </div>
	 <div id="caja5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 12
--------------------------------------------------


El siguiente archivo HTML tiene 3 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 10 filas y 12 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 12</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 12 columnas)
	<pre>
	111111111111
	111111111111
	111111111111
	111111111111
	111111111111
	333333333333
	333333333333
	222222222222
	222222222222
	222222222222
	</pre>
	<div id="contenedorglobal">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |  **C12**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F6**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F7**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F8**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F9**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F10** | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+

Solución al grid (Ejercicio 12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 12</title>
	<meta charset="utf-8">
	<style>
	#contenedorglobal{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#caja1{
		grid-row:     1/6;
		grid-column:  1/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja2{
		grid-row:     8/11;
		grid-column:  1/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja3{
		grid-row:     6/8;
		grid-column:  1/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 12 columnas)
	<pre>
	111111111111
	111111111111
	111111111111
	111111111111
	111111111111
	333333333333
	333333333333
	222222222222
	222222222222
	222222222222
	</pre>
	<div id="contenedorglobal">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 13
--------------------------------------------------


El siguiente archivo HTML tiene 3 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 9 filas y 9 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 13</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	333333333
	333333333
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F5**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F6**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F7**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F8**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F9**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Solución al grid (Ejercicio 13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 13</title>
	<meta charset="utf-8">
	<style>
	#container{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#caja1{
		grid-row:     1/5;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja2{
		grid-row:     7/10;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#caja3{
		grid-row:     5/7;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	333333333
	333333333
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="caja1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1
	 </div>
	 <div id="caja2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2
	 </div>
	 <div id="caja3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 14
--------------------------------------------------


El siguiente archivo HTML tiene 4 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 9 filas y 9 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 14</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111122222
	111122222
	111122222
	111122222
	111144444
	111144444
	111133333
	111133333
	111133333
	</pre>
	<div id="contenedorglobal">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F1**  | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F2**  | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F3**  | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F4**  | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F5**  | 1        | 1        | 1        | 1        | 4        | 4        | 4        | 4        | 4        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F6**  | 1        | 1        | 1        | 1        | 4        | 4        | 4        | 4        | 4        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F7**  | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F8**  | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F9**  | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Solución al grid (Ejercicio 14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 14</title>
	<meta charset="utf-8">
	<style>
	#contenedorglobal{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#columna1{
		grid-row:     1/10;
		grid-column:  1/5;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna2{
		grid-row:     1/5;
		grid-column:  5/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna3{
		grid-row:     7/10;
		grid-column:  5/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna4{
		grid-row:     5/7;
		grid-column:  5/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111122222
	111122222
	111122222
	111122222
	111144444
	111144444
	111133333
	111133333
	111133333
	</pre>
	<div id="contenedorglobal">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3
	 </div>
	 <div id="columna4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 15
--------------------------------------------------


El siguiente archivo HTML tiene 4 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 10 filas y 9 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 15</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 9 columnas)
	<pre>
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F1**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F2**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F3**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F4**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F5**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F6**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F7**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F8**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F9**  | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F10** | 3        | 3        | 4        | 4        | 1        | 1        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Solución al grid (Ejercicio 15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 15</title>
	<meta charset="utf-8">
	<style>
	#container{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#bloque1{
		grid-row:     1/11;
		grid-column:  5/7;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque2{
		grid-row:     1/11;
		grid-column:  7/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque3{
		grid-row:     1/11;
		grid-column:  1/3;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque4{
		grid-row:     1/11;
		grid-column:  3/5;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 9 columnas)
	<pre>
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	334411222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 16
--------------------------------------------------


El siguiente archivo HTML tiene 3 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 11 filas y 12 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 16</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 12 columnas)
	<pre>
	111111333333
	111111333333
	111111333333
	111111333333
	111111333333
	111111222222
	111111222222
	111111222222
	111111222222
	111111222222
	111111222222
	</pre>
	<div id="contenedor">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |  **C12**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 3        | 3        | 3        | 3         | 3         | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F6**  | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F7**  | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F8**  | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F9**  | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F10** | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F11** | 1        | 1        | 1        | 1        | 1        | 1        | 2        | 2        | 2        | 2         | 2         | 2         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+

Solución al grid (Ejercicio 16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 16</title>
	<meta charset="utf-8">
	<style>
	#contenedor{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#columna1{
		grid-row:     1/12;
		grid-column:  1/7;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna2{
		grid-row:     6/12;
		grid-column:  7/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna3{
		grid-row:     1/6;
		grid-column:  7/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (11 filas y 12 columnas)
	<pre>
	111111333333
	111111333333
	111111333333
	111111333333
	111111333333
	111111222222
	111111222222
	111111222222
	111111222222
	111111222222
	111111222222
	</pre>
	<div id="contenedor">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2 
		Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 17
--------------------------------------------------


El siguiente archivo HTML tiene 6 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 10 filas y 10 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 17</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 10 columnas)
	<pre>
	1111111111
	1111111111
	1111111111
	1111111111
	1111111111
	5566644444
	5566644444
	2222233333
	2222233333
	2222233333
	</pre>
	<div id="contenedorglobal">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4
	 </div>
	 <div id="bloque5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5
	 </div>
	 <div id="bloque6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F5**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F6**  | 5        | 5        | 6        | 6        | 6        | 4        | 4        | 4        | 4        | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F7**  | 5        | 5        | 6        | 6        | 6        | 4        | 4        | 4        | 4        | 4         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F8**  | 2        | 2        | 2        | 2        | 2        | 3        | 3        | 3        | 3        | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F9**  | 2        | 2        | 2        | 2        | 2        | 3        | 3        | 3        | 3        | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+
|  **F10** | 2        | 2        | 2        | 2        | 2        | 3        | 3        | 3        | 3        | 3         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+

Solución al grid (Ejercicio 17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 17</title>
	<meta charset="utf-8">
	<style>
	#contenedorglobal{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#bloque1{
		grid-row:     1/6;
		grid-column:  1/11;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque2{
		grid-row:     8/11;
		grid-column:  1/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque3{
		grid-row:     8/11;
		grid-column:  6/11;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque4{
		grid-row:     6/8;
		grid-column:  6/11;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque5{
		grid-row:     6/8;
		grid-column:  1/3;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque6{
		grid-row:     6/8;
		grid-column:  3/6;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (10 filas y 10 columnas)
	<pre>
	1111111111
	1111111111
	1111111111
	1111111111
	1111111111
	5566644444
	5566644444
	2222233333
	2222233333
	2222233333
	</pre>
	<div id="contenedorglobal">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1 
		Texto 1 Texto 1 Texto 1 Te
		xto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2 Texto 2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4
	 </div>
	 <div id="bloque5">
	  Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5 Texto 5 Texto 5 Texto 
		5 Texto 5 Texto 5 Texto 5 
		Texto 5 Texto 5 Texto 5 Te
		xto 5 Texto 5 Texto 5 Text
		o 5
	 </div>
	 <div id="bloque6">
	  Texto 6 Texto 6 Texto 6 Te
		xto 6 Texto 6 Texto 6 Text
		o 6 Texto 6 Texto 6 Texto 
		6
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 18
--------------------------------------------------


El siguiente archivo HTML tiene 3 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 9 filas y 12 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 18</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 12 columnas)
	<pre>
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	</pre>
	<div id="contenedorglobal">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |  **C10**  |  **C11**  |  **C12**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F1**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F2**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F3**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F4**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F5**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F6**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F7**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F8**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+
|  **F9**  | 2        | 2        | 2        | 3        | 3        | 3        | 1        | 1        | 1        | 1         | 1         | 1         |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+-----------+-----------+-----------+

Solución al grid (Ejercicio 18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 18</title>
	<meta charset="utf-8">
	<style>
	#contenedorglobal{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#columna1{
		grid-row:     1/10;
		grid-column:  7/13;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna2{
		grid-row:     1/10;
		grid-column:  1/4;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#columna3{
		grid-row:     1/10;
		grid-column:  4/7;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 12 columnas)
	<pre>
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	222333111111
	</pre>
	<div id="contenedorglobal">
	 <div id="columna1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1
	 </div>
	 <div id="columna2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="columna3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3
	 </div>
	</div>  
	</body>
	</html>
	

Ejercicio 19
--------------------------------------------------


El siguiente archivo HTML tiene 4 secciones y se desean maquetar según la tabla que aparece justo debajo y que tiene 9 filas y 9 columnas:


.. code-block:: html

	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 19</title>
	<meta charset="utf-8">
	<style>
	
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	444444444
	333333333
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4
	 </div>
	</div>  
	</body>
	</html>
	


+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| X        |  **C1**  |  **C2**  |  **C3**  |  **C4**  |  **C5**  |  **C6**  |  **C7**  |  **C8**  |  **C9**  |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F1**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F2**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F3**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F4**  | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F5**  | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        | 4        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F6**  | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        | 3        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F7**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F8**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+
|  **F9**  | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        | 2        |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Solución al grid (Ejercicio 19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html


	
	<!DOCTYPE html>
	<html>
	<head>
	<title>Ejercicio 19</title>
	<meta charset="utf-8">
	<style>
	#container{
		display:grid;
		grid-template-rows:   1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
		grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr ;
	}
	
	#bloque1{
		grid-row:     1/5;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque2{
		grid-row:     7/10;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque3{
		grid-row:     6/7;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	#bloque4{
		grid-row:     5/6;
		grid-column:  1/10;
		border    :  solid 1px black;
		margin   :  3px;
	}
	</style>
	</head>  
	<body>
	Este ejercicio muestra una disposición de rejilla como esta (9 filas y 9 columnas)
	<pre>
	111111111
	111111111
	111111111
	111111111
	444444444
	333333333
	222222222
	222222222
	222222222
	</pre>
	<div id="container">
	 <div id="bloque1">
	  Texto 1 Texto 1 Texto 1 Te
		xto 1 Texto 1 Texto 1 Text
		o 1 Texto 1 Texto 1 Texto 
		1 Texto 1 Texto 1 Texto 1
	 </div>
	 <div id="bloque2">
	  Texto 2 Texto 2 Texto 2 Te
		xto 2 Texto 2 Texto 2 Text
		o 2 Texto 2 Texto 2 Texto 
		2 Texto 2
	 </div>
	 <div id="bloque3">
	  Texto 3 Texto 3 Texto 3 Te
		xto 3 Texto 3 Texto 3 Text
		o 3 Texto 3 Texto 3 Texto 
		3 Texto 3 Texto 3 Texto 3 
		Texto 3
	 </div>
	 <div id="bloque4">
	  Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4 Text
		o 4 Texto 4 Texto 4 Texto 
		4 Texto 4 Texto 4 Texto 4 
		Texto 4 Texto 4 Texto 4 Te
		xto 4 Texto 4 Texto 4
	 </div>
	</div>  
	</body>
	</html>
	

