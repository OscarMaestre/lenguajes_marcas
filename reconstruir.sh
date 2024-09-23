#!/bin/bash

make html
make html
make latexpdf
make latexpdf
./copiar.py
git add docs
git commit -a -m"Reconstruccion HTML"
git push


