call make html
copiar.py
call make latex
cd _build\latex
call pdflatex ApuntesDeLenguajesDeMarcas.tex
call pdflatex ApuntesDeLenguajesDeMarcas.tex
cd ..
cd ..
copy _build\latex\*.pdf pdf
git add docs
call git commit -a --allow-empty-message -m ''
call git push

