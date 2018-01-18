function calcular(){
    let txt_salario=document.getElementById("salario");
    let cad_salario=txt_salario.value;
    let cantidad_salario=parseFloat(cad_salario);
    
    let impuestos=0;
    if ( (cantidad_salario>=20000) && (cantidad_salario<30000) ){
        impuestos=cantidad_salario * 0.1;
    }
    if (cantidad_salario>=30001){
        impuestos=cantidad_salario * 0.2;
    }
    
    let div_mensajes=document.getElementById("mensajes");
    div_mensajes.innerHTML="Debe Vd pagar:"+impuestos;
    
}