function extraer_numero(id){
    var control;
    control=document.getElementById(id);
    var valor=control.value;
    var numero=parseInt(valor);
    return numero;
}

function precio_mes_empresa_a(minutos){
    //Primero vemos si se pasa
    if (minutos<1000){
        //Si no se pasa, el precio es 20
        return 20;
    }
    //Si llegamos aquí, es porque sí se pasa
    
    //Calculamos cuantos minutos se pasa
    var exceso=minutos-1000;
    //Y ese exceso es a 8 centimos/minutos
    var precio_exceso=exceso*0.08
    //El precio de ese mes es
    //20 euros más lo que cueste el exceso
    var precio_mes=20+precio_exceso;
    //Devolvemos el calculo a quien lo pidiese
    return precio_mes
}

function precio_mes_empresa_a(minutos){
    //Primero vemos si se pasa
    if (minutos<500){
        //Si no se pasa, el precio es 10
        return 10;
    }
    //Si llegamos aquí, es porque sí se pasa
    
    //Calculamos cuantos minutos se pasa
    var exceso=minutos-500;
    //Y ese exceso es a 12 centimos/minutos
    var precio_exceso=exceso*0.12
    //El precio de ese mes es
    //10 euros más lo que cueste el exceso
    var precio_mes=10+precio_exceso;
    //Devolvemos el calculo a quien lo pidiese
    return precio_mes
}

function calcular(){
    var minutos_mes1;
    minutos_mes1=extraer_numero("mes1")
    var minutos_mes2;
    minutos_mes2=extraer_numero("mes2")
    var minutos_mes3;
    minutos_mes3=extraer_numero("mes3")
    
    var coste_mes1_empresa_a;
    coste_mes1_empresa_a=precio_mes_empresa_a(
        minutos_mes1);
    coste_mes2_empresa_a=precio_mes_empresa_a(
        minutos_mes2);
    coste_mes3_empresa_a=precio_mes_empresa_a(
        minutos_mes3);
    //Calculamos el precio que costaria
    //esos minutos en la empresa A
    var coste_total_a;
    coste_total_a=coste_mes1_empresa_a+coste_mes2_empresa_a+coste_mes3_empresa_a;
    
    //Repetimos el proceso para la empresa B
    var coste_mes1_empresa_b;
    coste_mes1_empresa_b=precio_mes_empresa_b(
        minutos_mes1);
    coste_mes2_empresa_b=precio_mes_empresa_b(
        minutos_mes2);
    coste_mes3_empresa_b=precio_mes_empresa_b(
        minutos_mes3);
    //Calculamos ahora el precio que costaria
    //esos minutos en la empresa B
    var coste_total_b;
    coste_total_b=coste_mes1_empresa_b+coste_mes2_empresa_b+coste_mes3_empresa_b;
    var zonaresultados;
    
    zonaresultados=document.getElementById("zonaresultados");
    zonaresultados.innerHTML="Con la A el precio es:" coste_total_a;
    zonaresultados.innerHTML+="Con la B el precio es:" coste_total_b;
    
}