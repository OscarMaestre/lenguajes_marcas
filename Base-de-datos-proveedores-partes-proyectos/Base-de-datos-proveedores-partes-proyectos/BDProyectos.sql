drop database proyectos;
create database proyectos;

use proyectos;

create table proveedores (
	numprov varchar(3) primary key, 		
	nombreprov varchar(8), 
	estado tinyint, 
	ciudad varchar(15)
) ;

create table partes (
   numparte varchar(3) primary key,
   nombreparte varchar(9), 
   color varchar(6), 
   peso tinyint, 
   ciudad varchar(8)
);

create table proyectos (
   numproyecto varchar(3) primary key,
   nombreproyecto varchar(13),
   ciudad varchar(8)
);


create table suministra (
  numprov varchar(3)
      references proveedores(numprov), 
  numparte varchar(3)
      references partes(numparte), 
  numproyecto varchar(3)
      references proyectos(numproyecto),
  cantidad int,
  primary key (numprov,numparte, numproyecto)
);

insert into proveedores values ("v1", "Smith", 20, "Londres");
insert into proveedores values ("v2", "Jones", 10, "Paris");
insert into proveedores values ("v3", "Blake", 30, "Paris");
insert into proveedores values ("v4", "Clarke", 20, "Londres");
insert into proveedores values ("v5", "Adams", 30, "Atenas");

insert into partes values ("p1", "Tuerca",  "Rojo", "12", "Londres");
insert into partes values ("p2", "Perno",   "Verde", "17", "Paris");
insert into partes values ("p3", "Tornillo","Azul", "17", "Roma");
insert into partes values ("p4", "Tornillo","Rojo", "14", "Londres");
insert into partes values ("p5", "Leva",    "Azul", "12", "Paris");
insert into partes values ("p6", "Engranaje", "Rojo", "19", "Londres");

insert into proyectos values ("y1", "Clasificador", "Paris");
insert into proyectos values ("y2", "Monitor", "Roma");
insert into proyectos values ("y3", "OCR", "Atenas");
insert into proyectos values ("y4", "Consola", "Atenas");
insert into proyectos values ("y5", "RAID", "Londres");
insert into proyectos values ("y6", "EDS", "Oslo");
insert into proyectos values ("y7", "Cinta", "Londres");


insert into suministra values ("v1", "p1", "y1", 200);
insert into suministra values ("v1", "p1", "y4", 700);
insert into suministra values ("v2", "p3", "y1", 400);
insert into suministra values ("v2", "p3", "y2", 200);
insert into suministra values ("v2", "p3", "y3", 300);
insert into suministra values ("v2", "p3", "y4", 500);
insert into suministra values ("v2", "p3", "y5", 600);
insert into suministra values ("v2", "p3", "y6", 400);
insert into suministra values ("v2", "p3", "y7", 600);
insert into suministra values ("v2", "p5", "y2", 100);
insert into suministra values ("v3", "p3", "y1", 200);
insert into suministra values ("v3", "p4", "y2", 500);
insert into suministra values ("v4", "p6", "y3", 300);
insert into suministra values ("v4", "p6", "y7", 300);
insert into suministra values ("v5", "p2", "y2", 200);
insert into suministra values ("v5", "p2", "y4", 100);
insert into suministra values ("v5", "p5", "y5", 500);
insert into suministra values ("v5", "p6", "y2", 200);
insert into suministra values ("v5", "p1", "y4", 100);
insert into suministra values ("v5", "p3", "y4", 200);
insert into suministra values ("v5", "p4", "y4", 800);
insert into suministra values ("v5", "p5", "y4", 400);
insert into suministra values ("v5", "p6", "y4", 500);


