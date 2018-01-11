let pepito=document.getElementById("mensajes");

let peso=20;

let mensaje="  El peso es de " + peso + "   kg";
pepito.innerHTML=mensaje;

if (peso < 30 ) {
    let peso_incrementado=peso+1;
    pepito.innerHTML=mensaje +
        "El peso antes era"+peso+
        "y ahora es " + peso_incrementado;
}