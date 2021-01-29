call make html
copiar.py
call make latex
cd _build\latex
rem call pdflatex ApuntesDeLenguajesDeMarcas.tex
rem call pdflatex ApuntesDeLenguajesDeMarcas.tex
cd ..
cd ..
copy _build\latex\*.pdf pdf
git add docs
call git commit -a --allow-empty-message -m ''
call git push

