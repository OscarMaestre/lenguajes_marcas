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


function calcular_desv_media(vector_pasado){
    let media=calcular_media(vector_pasado);
    let pos=0;
    let vector_desviaciones=new Array();
    for (pos=0; pos<vector_pasado.length;pos++){
        let diferencia=vector_pasado[pos]-media;
        vector_desviaciones[pos]=Math.abs(diferencia);
    } //Fin del for
    let desv_media=calcular_media(vector_desviaciones);
    return desv_media;
}
let sueldos=new Array();
sueldos=[1000, 870, 500, 690, 1300, 1590, 950];
let media=calcular_media(sueldos);
let desv=calcular_desv_media(sueldos);

anadir_mensaje("mensajes", "La media es:"+media+"<br/>");
anadir_mensaje("mensajes", "La desv es:"+desv+"<br/>");

