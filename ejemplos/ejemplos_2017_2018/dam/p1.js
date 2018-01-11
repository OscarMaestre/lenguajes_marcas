function calcular_media(vector_pasado){
    let pos;
    let suma=0;
    for (pos=0;pos<vector_pasado.length; pos++ ){
        suma = suma+vector_pasado[pos];
    }
    let media=suma/vector_pasado.length;
    return media;
}

function anadir_mensaje(id_html, texto_pasado){
    let div=document.getElementById(id_html);
    let texto_anterior=div.innerHTML;
    div.innerHTML=texto_anterior + texto_pasado;
}

let vector=new Array();
vector[0]=61;
vector[1]=65;
vector[2]=58;
vector=[67,98,32,44];
let media=calcular_media(vector);
let otro_vector=[56,33, 61, 87, 21, 90, 71];
let otra_media=calcular_media(otro_vector);
anadir_mensaje("mensajes", "La media primera es:"+media);
anadir_mensaje("mensajes", "La otra es:"+otra_media);

