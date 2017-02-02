function esta_checked(id){
    var control;
    control=document.getElementById(id);
    if (control.checked){
        return true;
    } else {
        return false;
    }
}

function calcular(){
    var preciototal   =0;
    var preciomodelo  =0;
    var preciomotor   =0;
    var precioextras  = 0;
    if ( (!esta_checked("modelo_a"))
        && (!esta_checked("modelo_b") ) ){
        alert("Debe marcar un modelo");
        return ;
    }
    if (esta_checked("modelo_a")){
        preciomodelo=7000;
    }
    if (esta_checked("modelo_b")){
        preciomodelo=9000;
    }
    if (esta_checked("gasolina")){
        preciomotor=2000;
    }
    if (esta_checked("diesel")){
        preciomotor=4000;
    }
    if (esta_checked("metalizada")){
        precioextras=1000;
    }
    if (esta_checked("sonido")){
        precioextras=precioextras+500;
    }
    if (esta_checked("seguridad")){
        precioextras=precioextras+1000;
    }
    preciototal=preciomodelo+preciomotor+precioextras;
    
    var zonaresultados;
    zonaresultados=document.getElementById(
        "zonaresultados");
    zonaresultados.innerHTML="Precio:"+preciototal;
    
}