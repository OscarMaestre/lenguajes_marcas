let objeto_mapa=null;
function desplazar_mapa(){
    let objeto_latitud=$("#latitud");
    let objeto_longitud=$("#longitud");
    
    let contenido_latitud=objeto_latitud.val();
    let contenido_longitud=objeto_longitud.val();
    
    let nueva_latitud=parseFloat(contenido_latitud);
    let nueva_longitud=parseFloat(contenido_longitud);    
    let nuevas_coordenadas=new google.maps.LatLng(
                            nueva_latitud, nueva_longitud);
    objeto_mapa.panTo(nuevas_coordenadas);
    return false;
}

function viajar_ciudad(){
    let objeto_lista=$("#ciudad");
    let nuevas_coordenadas=null;
    if (objeto_lista.val()=="BE"){
        nuevas_coordenadas=new  google.maps.LatLng(52, 13);
    }
    if (objeto_lista.val()=="CR"){
        nuevas_coordenadas=new  google.maps.LatLng(38, -3);
    }
    if (objeto_lista.val()=="NY"){
        nuevas_coordenadas=new  google.maps.LatLng(40, -73);
    }
    
    objeto_mapa.panTo(nuevas_coordenadas);
    return false;
}

function main(){
    let div_mapa=document.getElementById("mapa");
    let latitud= 38;
    let longitud=-3;
    
    let objeto_coordenadas=new google.maps.LatLng(latitud, longitud);
    
    let parametros_mapa={
        center: objeto_coordenadas  ,  zoom:   8
    };
    
    objeto_mapa=new google.maps.Map(div_mapa, parametros_mapa);
    
    $("#viajar").click(desplazar_mapa);
    $("#viajar_ciudad").click(viajar_ciudad);
}
let objeto_documento=$(document)
objeto_documento.ready(main)