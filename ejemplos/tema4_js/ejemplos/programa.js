function calcular() {
    let objeto_input=document.getElementById("salario");
    let valor=objeto_input.value;
    
    //Convertimos el "22000" a 22000
    let cantidad_numerica=parseFloat(valor);
    
    let impuestos=0;
    
    if((cantidad_numerica>=20001) &&  (cantidad_numerica<30000))
    {
       impuestos=cantidad_numerica*0.1; 
    }
    
    if (cantidad_numerica>=30001) {
        impuestos=cantidad_numerica * 0.2;
    }
    
    let div_mensajes=document.getElementById("mensajes");
    div_mensajes.innerHTML="Sus <i>impuestos</i>:"+impuestos;
}