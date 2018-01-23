function calcular(){
    let caja_salarios=document.getElementById(
                        "salario");
    let texto_salario=caja_salarios.value;
    let salario_anual=parseFloat(texto_salario);
    
    /* Calculamos los impuestos*/
    let impuestos=0;
     
    if ( (salario_anual>=20000) && (salario_anual<=30000) ){
        impuestos=salario_anual * 0.1;
    }
    
    if ( (salario_anual>=30001) && (salario_anual<=50000) ){
        impuestos=salario_anual * 0.2;
    }
    if (salario_anual>=50001){
        impuestos=salario_anual * 0.38;
    }
    
    /* Y ahora comprobamos si ha marcado
     * la casilla "con_hijos"*/
    let radio_con_hijos=document.getElementById(
                        "con_hijos");
    if (radio_con_hijos.checked) {
        impuestos=impuestos - 180;
        //code
    }
    /* Comprobamos si marcó la
     * bonificación B1*/
    let bonificacion_b1=document.getElementById(
        "bonificacion_b1");
    if (bonificacion_b1.checked) {
        impuestos=impuestos - 355;
    }
    /* Y comprobamos la bonificación B2*/
    let bonificacion_b2=document.getElementById(
        "bonificacion_b2");
    if (bonificacion_b2.checked) {
        impuestos=impuestos - 560;
    }
    
    /* Escribimos el resultado*/
    let div_mensajes=document.getElementById("mensajes");
    div_mensajes.innerHTML="Impuestos:"+impuestos;
    
    
}
