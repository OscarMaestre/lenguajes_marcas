function saludar(){
    let txt_nombre=$("#txt_nombre");
    let nombre_introducido=txt_nombre.val();
    alert ("Hola "+nombre_introducido);
    return false;
}
function error_pulsacion(){
    alert("Pulse el otro boton");
    return false;
}
function main(){
    let boton_saluda=$("#btn_saludo");
    boton_saluda.click ( saludar );
    
    let boton_adicional=$("#btn_adicional");
    boton_adicional.click ( error_pulsacion )
}
//Seleccionamos el objeto document
let objeto_documento=$(document)
/*Y ordenamos que cuando todo esté
 *listo se ejecute la función main
 *(recordemos que main se puede llamar
 *como queramos)*/

objeto_documento.ready(main)