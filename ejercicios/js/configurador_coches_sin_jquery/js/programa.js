function esta_checked(id){
    if ($(id).prop("checked")){
        return true;
    } else {
        return false;
    }
}
function activar_checked(id){
    $(id).prop("checked", true);
}
function desactivar_checked(id){
    $(id).prop("checked", false);
}
function procesar_incompatibilidades(){
    $("#mensajes").html("");
    if ( esta_checked("#metalizada") ){
        if ( esta_checked("#negro") ){
            desactivar_checked("#negro");
            $("#mensajes").html(
              "No se puede metaliz+negro");
        }
        if ( esta_checked("#blanco") ){
            desactivar_checked("#blanco");
            $("#mensajes").html(
              "No se puede metaliz+blanco");
        }
        if ( esta_checked("#rojo") ){
            desactivar_checked("#rojo");
            $("#mensajes").html(
              "No se puede metaliz+rojo");
        }
    }
    
    if (esta_checked("#normal")){
        if (esta_checked("#aleron")){
            desactivar_checked("#aleron");
            $("#mensajes").html(
                "Aleron solo con metaliz" );
        }
    }
    if (esta_checked("#diesel")){
        if (esta_checked("#pot2300")){
            desactivar_checked("#pot2300");
            $("#mensajes").html(
                "Imposible diesel 2300cm3");
        }
    }

    if (esta_checked("#altavoces")){
        if (!esta_checked("#radio")){
            desactivar_checked("#altavoces");
            $("#mensajes").html(
                "Altavoces solo con RadioCD");
        }
    }
}

function mostrar_ejemplo_color(){
    let objeto_muestra_color;
    objeto_muestra_color=$("#muestra_color");
    if (esta_checked("#negro")){
        objeto_muestra_color.css(
            "background-color", "black" );
    }
    if (esta_checked("#rojo")){
        objeto_muestra_color.css(
            "background-color", "red" );
    }
}

function calcular(){
    procesar_incompatibilidades();
    //Ahora calculamos el precio
    let precio=0;
    
    if (esta_checked("#gasolina")){
        precio=precio+7000;
    }
    
    if (esta_checked("#diesel")){
        precio=precio+8200;
    }
    if (esta_checked("#pot1100")){
        precio=precio+800;
    }
    if (esta_checked("#pot1800")){
        precio=precio+1900;
    }
    if (esta_checked("#pot2300")){
        precio=precio+2500;
    }
    
    if (esta_checked("#normal")){
        precio=precio+750;
    }
    if (esta_checked("#metalizada")){
        precio=precio+1580;
    }
    
    if (esta_checked("#aleron")){
        precio=precio+190;
    }
    if (esta_checked("#radio")){
        precio=precio+230;
    }
    if (esta_checked("#altavoces")){
        precio=precio+320;
    }
    if (esta_checked("#gps")){
        precio=precio+520;
    }
    mostrar_ejemplo_color();    
    $("#precio").html("Su precio:"+precio);

}
function main(){
    $("#gasolina").click(calcular);
    $("#diesel").click(calcular);
    
    $("#pot1100").click(calcular);
    $("#pot1800").click(calcular);
    $("#pot2300").click(calcular);
    
    $("#normal").click(calcular);
    $("#metalizada").click(calcular);
    
    $("#negro").click(calcular);
    $("#blanco").click(calcular);
    $("#rojo").click(calcular);
    $("#azul").click(calcular);
    $("#verde").click(calcular);
    $("#gris").click(calcular);
    
    $("#aleron").click(calcular);
    $("#radio").click(calcular);
    $("#altavoces").click(calcular);
    $("#gps").click(calcular);
    
}
let objeto_documento=$(document)
objeto_documento.ready(main)
