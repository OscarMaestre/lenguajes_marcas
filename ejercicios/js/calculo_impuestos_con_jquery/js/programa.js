function getFloat ( identificador ){
    let objeto_control=$(identificador);
    let cadena_control=objeto_control.val();
    let cantidad=parseFloat(cadena_control);
    return cantidad;
}
function isChecked ( identificador ){
    let objeto_control=$(identificador);
    /*Comprobamos si el control
    tiene la propiedad checked*/
    if (objeto_control.prop("checked")){
        return true;
    }
    /* Si no tiene la propiedad checked
    es que no está marcado*/
    return false;
}
function calcular(){
    let salario_anual=getFloat("#salario");    
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
    if (isChecked("#con_hijos")){
        impuestos = impuestos - 180;
    }
    if (isChecked("#bonificacion_b1")){
        impuestos = impuestos - 245;
    }
    if (isChecked("#bonificacion_b2")){
        impuestos = impuestos - 535;
    }
    
    let div_mensajes=$("#mensajes");
    div_mensajes.html("Sus <b>impuestos</b> son:"+impuestos);
    return false;
    
}
function main(){
    let boton=$("#calcular");
    boton.click ( calcular );
    
}
let objeto_documento=$(document);
objeto_documento.ready(main);