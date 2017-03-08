===========================================
Sistemas de gestión de información
===========================================


Introducción
===========================================

Primero definiremos los términos:

* Sistema: "conjunto de elementos interrelacionados que colaboran para la consecución de un objetivo".

* Gestión de información: movimientos de información que facilitan la consecución de los objetivos de la empresa.

Entre los objetivos más habituales están:

* Objetivos económicos.
* Objetivos temporales (supervivencia).
* Objetivos legales, entre los que destacan los fiscales.

Procesar la información hoy en día es muy difícil, por lo que la informática es de gran ayuda en dicho procesamiento: (INFORmación+autoMÁTICA).


¿Todos los sistemas de una empresa son informáticos? NO. Un ejemplo es el sistema postal que no requiere (y no siempre ha requerido) parte informática.

Niveles en la empresa
===========================================

Toda empresa se puede ver desde tres puntos de vista temporales distintos

1. Nivel estratégico: en este nivel están las personas o elementos que tienen un punto de vista más global y más largo plazo (normalmente plazos de varios años).
2. Nivel táctico: en este nivel están los mandos intermedios de la empresa con plazos medios (máximo un año)
3. Nivel operativo: está el personal "de a pie", que recoge la información a diario y la procesa a diario.

Ejemplo: Mercadona.

Tipos de SGI informáticos
----------------------------------------------

* DSS o Decision Support System: ayudan a tomar decisiones en función de la información disponible.

* CRM o Customer Relationship Managements o Gestores de la relación con clientes. Son sistemas que gestionan información muy personalizada a los clientes, tales como sistemas de recomendación, sistemas de fidelización. Los CRM manejan la comunicación entre información interna y externa de la empresa.

* ERP o Enterprise Resource Planning o sistemas de planificación de recursos corporativos gestionan toda la información interna de la empresa.

Los ERP han ganado mucho auge con el tiempo, ya que pueden hacer operaciones muy sofisticadas, entre ellas:

1. Optimización de procesos: implica resolver complejos problemas matemáticos que con una herramienta informática se resuelven al instante.

2. Logística: implica resolver problemas de transporte de productos en base a diversas restricciones (no todas matemáticas). Un problema muy común es la optimización de rutas que implica resolver el "problema del viajante".

3. Fiscalidad: permite aprovechar las diferentes ventajas que en materia de fiscalidad se ofrecen en distintos casos, en distintos territorios...


4. Contabilidad: la participación en diversas sociedades empresariales puede complicar las operaciones de contabilidad, operaciones que un ERP puede registrar.

5. Optimización de recursos humanos: optimizar el volumen de contrataciones y despidos, nóminas, etc...


6. Operaciones de informes y estadística: para conocer el estado real de la empresa en sus distintos departamentos y períodos.


7. Trazabilidad: permite conocer el punto exacto de ubicación de un producto a lo largo de toda la cadena de abastecimiento (supply chain).

Almacenamiento en los SGI
===========================================


La mayor parte de SGI se apoyan en tecnologías conocidas como SGBD con SQL e incluso XML.


La mayor parte de SGBD permite procesar y extraer información en forma de SQL.

En general, cualquier consulta sobre cualquier tabla puede convertirse en XML. Cuando por ejemplo hacemos

.. code-block:: sql

	select * from marcas;
	
obtenemos un resultado como este::

	+----+--------+-------------+
	| id | nombre | ap          |
	+----+--------+-------------+
	|  1 | Juan   | Lopez Lopez |
	|  2 | Andres | Ruiz Gomez  |
	|  3 | Tomas  | Perez Diaz  |
	+----+--------+-------------+

	3 rows in set (0.00 sec)
	

Sin embargo, podemos ejecutar el siguiente comando que se conecta a MySQL ejecuta la consulta dada y devuelve un fichero XML::

	mysql -uroot -Ddatos -e"select * from usuarios" --xml

El resultado será algo como esto:

.. code-block:: xml

	<?xml version="1.0"?>

	<resultset statement="select * from usuarios
	" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	  <row>
			<field name="id">1</field>
			<field name="nombre">Juan</field>
			<field name="ap">Lopez Lopez</field>
	  </row>

	  <row>
			<field name="id">2</field>
			<field name="nombre">Andres</field>
			<field name="ap">Ruiz Gomez</field>
	  </row>

	  <row>
			<field name="id">3</field>
			<field name="nombre">Tomas</field>
			<field name="ap">Perez Diaz</field>
	  </row>
	</resultset>	




Puntos de vista en los SGI
===========================================

Desarrollador
----------------------------------------------

Para un desarrollador hay ciertos temas fundamentales a conocer del SGI con el que trabaje:

* Programable ¿qué lenguaje de programación usa? ¿usa OOP? ¿es un tipo de lenguaje distinto?.

* ¿Se puede conectar desde algún lenguaje general?

* ¿Se pueden usar otras bibliotecas de uso general? (Hibernate)


Administrador
----------------------------------------------

* ¿Se pueden controlar  los accesos?

* ¿Como cumplir la LOPD y sus 3 niveles?

Usuario
----------------------------------------------

* ¿Como se usa el SGI? En unos casos hay muchos requisitos pero cada vez más abundan los SGI con interfaz Web.

* La adaptación específica que ofrece el sistema a la empresa. El PGC en España es un elemento al cual un programa puede estar adaptado o no. Otra posibilidad es que el programa permita INCOTERMS.


Ejercicio
----------------------------------------------

Modelar el diagrama de estados para el cajero en el caso "Sacar dinero"






























