function getFloat ( identificador ){
    let objeto_control=$(identificador);
    let cadena_control=objeto_control.val();
    let cantidad=parseFloat(cadena_control);
    return cantidad;
}

function calcular(){
    let salario_anual=getFloat("#salario");
    alert("Calculando para "+salario_anual);
}
function main(){
    let boton=$("#calcular");
    boton.click ( calcular );
    
}
let objeto_documento=$(document)
objeto_documento.ready(main)