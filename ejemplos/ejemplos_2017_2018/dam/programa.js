let i;
let texto_completo="";
let mensaje="";
let p_resultado= document.getElementById("resultado");
for ( i=0 ; i<=20 ; i++){
    if ( i % 2 == 0 ){
        mensaje=i + "<u> es par </u><br/>";
    } else {
        mensaje=i + "<i> es impar</i><br/>";
    }
    texto_completo = texto_completo + mensaje;
}
p_resultado.innerHTML=texto_completo;