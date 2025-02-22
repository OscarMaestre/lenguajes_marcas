function get_value_numerico(id){
    var control=document.getElementById(id)
    var valor=control.value
    return parseFloat(valor)
}
function calcular_cuota(){
    var capital=get_value_numerico("capital")
    var redito =get_value_numerico("redito")
    var tiempo =get_value_numerico("tiempo")
    
    redito=redito/100
    
    var c_tiempo=document.getElementById("tiempo")
    var tiempo=parseInt(c_tiempo.value) 
    
    document.write("<h1>Total a pagar</h1>")
    document.write("<table border='1'>")
    var cuota_mensual= cuota(capital, redito, tiempo)
    for (var mes=1; mes<=tiempo*12; mes++)
    {
        document.write("<tr>")
        escribir_celda("Mes "+mes)
        escribir_celda("Cuota "+cuota_mensual)
        document.write("</tr>")
    }
    document.write("</table>")
}