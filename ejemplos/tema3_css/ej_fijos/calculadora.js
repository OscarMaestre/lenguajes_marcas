function get_value_numerico(id){
    var control=document.getElementById(id)
    var valor=control.value
    return parseFloat(valor)
}
function calcular(){
  var n1=get_value_numerico("num1")
  var n2=get_value_numerico("num2")
  var c_operacion=document.getElementById("operacion")
  var operacion=c_operacion.value;
  if (operacion=="sumar"){
    var total=n1+n2;
    var zonaresultados;
    zonaresultados=document.getElementById(
                    "zonaresultados");
    zonaresultados.innerHTML="<i>Total:"+total+"</i>";
    
  }
  if (operacion=="restar"){
    var total=n1-n2;
    var zonaresultados;
    zonaresultados=document.getElementById(
                    "zonaresultados");
    zonaresultados.innerHTML="<i>Total:"+total+"</i>";
  }
  
  
}