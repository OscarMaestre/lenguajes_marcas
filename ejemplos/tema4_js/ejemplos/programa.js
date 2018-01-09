let div_mensajes=document.getElementById("mensajes");
div_mensajes.innerHTML="<u>Hola mundo</u>";


let multiplicando=5;
let i=0;
for (i=0; i<=10; i=i+1){
    let resultado = multiplicando * i;
    let mensaje= multiplicando +"*" + i+"="+resultado + "<br/>";
    div_mensajes.innerHTML= div_mensajes.innerHTML + mensaje;
}