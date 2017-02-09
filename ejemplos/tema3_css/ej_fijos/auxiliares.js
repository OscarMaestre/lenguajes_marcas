function escribir_celda(texto){
  document.write("<td>" + texto + "</td>")
}

/* Se supone que el tiempo nos lo pasan
 * en AÑOS*/
function cuota ( capital, redito, tiempo ) {
  /*...*/
  var intereses = capital * redito * tiempo
  var total_a_pagar = capital + intereses
  var cuota_mensual = total_a_pagar / (tiempo * 12)
  return cuota_mensual
}

function get_value_numerico(id){
    var control=document.getElementById(id)
    var valor=control.value
    return parseFloat(valor)
}