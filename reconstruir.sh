#!/bin/bash

make html
make html
./copiar.py
git add docs
git commit -a -m"Reconstruccion HTML"
#git push


