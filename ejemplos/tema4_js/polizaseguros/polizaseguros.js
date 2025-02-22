/*Dado un identificador está función devuelve "true" si ese elemento está marcado y "false" si no lo está*/
function esta_checked(id){
    let control=document.getElementById(id);
    if (control.checked){
        return true;
    } else {
        return false;
    }
}
function calcular(){
    let precio=0;

    let divresultado=document.getElementById("resultado");
    divresultado.innerHTML="Precio:"+precio;
}