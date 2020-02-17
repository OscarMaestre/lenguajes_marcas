/*Esta función se ocupa de sacar un control, sacar el texto que hay dentro (recuérdese que es texto aunque "parezca" un número), convierte el texto a número y devuelve dicho número*/
function sacar_numero(id){
    let control=document.getElementById(id);
    /*Algunos controles tienen un "campo" value en el cual
    está el valor de lo que nos interesa, pero ¡está en forma de texto*/
    let texto=control.value;
    /* Convirtamos ese texto a número*/
    let numero=parseFloat(texto);
    /*Y devolvemos ese número a quien nos ejecutó*/
    return numero;
}

/*Dado un identificador está función devuelve "true" si ese elemento está marcado y "false" si no lo está*/
function esta_checked(id){
    let control=document.getElementById(id);
    if (control.checked){
        return true;
    } else {
        return false;
    }
}
/*Esta función toma un texto y lo inserta dentro del 
div resultado*/
function escribir_resultado(texto){
    let divresultado=document.getElementById("resultado");
    divresultado.innerHTML="Resultado:"+texto;
}

/*Esta es la función que se ejecuta cuando alguien "cambia" un número o cuando alguien "hace click en una operación"*/
function calcular(){
    let num1=sacar_numero("num1");
    let num2=sacar_numero("num2");
    let resultado=0;
    if (esta_checked("suma")){
        resultado=num1+num2;
    }
    if (esta_checked("resta")){
        resultado=num1-num2;
    }
    if (esta_checked("multiplicacion")){
        resultado=num1*num2;
    }
    if (esta_checked("division")){
        resultado=num1/num2;
    }
    escribir_resultado(resultado)

}