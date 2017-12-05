let multiplicador=42;

let multiplicando=1;

document.write("<table border=1>")
for (multiplicando=1;multiplicando<=1000;multiplicando++){
    let resultado=multiplicando * multiplicador ;
    document.write("<tr>")
    document.write("<td>")
    document.write(multiplicando)
    document.write("</td>")
    document.write("<td>")
    document.write(multiplicador)
    document.write("</td>")
    document.write("<td>")
    document.write(resultado)
    document.write("</td>")
    document.write("</tr>")
}
document.write("</table>")