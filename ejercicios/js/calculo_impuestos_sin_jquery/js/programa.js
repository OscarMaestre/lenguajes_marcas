function limpiar_errores() {
    let objeto_diesel=document.getElementById("diesel");
    let objeto_pot2300=document.getElementById("pot2300");
    if ((objeto_diesel.checked) && (objeto_pot2300.checked)) {
        alert("Incompatibilidad diesel+2300");
        objeto_pot2300.checked=false;
    }
    
    let objeto_pintura_normal=document.getElementById("normal");
    let objeto_color_gris =document.getElementById("gris");
    let objeto_color_azul =document.getElementById("azul");
    let objeto_color_verde=document.getElementById("verde");
    
    if ( (objeto_pintura_normal.checked)
        && (objeto_color_gris.checked) ){
        alert("Incompatibilidad normal+gris");
        objeto_color_gris.checked=false;
    }
    if ( (objeto_pintura_normal.checked)
        && (objeto_color_azul.checked) ){
        alert("Incompatibilidad normal+azul");
        objeto_color_azul.checked=false;
    }
    if ( (objeto_pintura_normal.checked)
        && (objeto_color_verde.checked) ){
        alert("Incompatibilidad normal+verde");
        objeto_color_verde.checked=false;
    }
    
}
function calcular() {
    
    limpiar_errores();
    
    let precio=0;
    
    let objeto_gasolina=document.getElementById("gasolina");
    if (objeto_gasolina.checked) {
        precio=precio + 7000;
    }
    let objeto_diesel=document.getElementById("diesel");
    if (objeto_diesel.checked) {
        precio=precio + 8200;
    }
    
    let objeto_pot1100=document.getElementById("pot1100");
    if (objeto_pot1100.checked) {
        precio=precio + 800;
    }
    let objeto_pot1800=document.getElementById("pot1800");
    if (objeto_pot1800.checked) {
        precio=precio + 1900;
    }
    let objeto_pot2300=document.getElementById("pot2300");
    if (objeto_pot2300.checked) {
        precio=precio + 2500;
    }
    
    
    //Mostramos el precio final
    let objeto_mensajes=document.getElementById("mensajes");
    objeto_mensajes.innerHTML="Precio <u>final</u>"+precio;
}