call make html
copiar.py
call make latex
cd _build\latex

otros_scripts\scripts_archivos_ejemplos_aulas.py descargas\Ejemplos_2023_2024 > tema9descargas.rst
rem call pdflatex ApuntesDeLenguajesDeMarcas.tex
rem call pdflatex ApuntesDeLenguajesDeMarcas.tex
cd ..
cd ..
copy _build\latex\*.pdf pdf
git add docs
call git commit -a -m"Reconstruccion"	
call git push

