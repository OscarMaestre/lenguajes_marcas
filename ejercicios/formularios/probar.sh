#!/bin/bash

./generador_ejercicios.py
pushd .
cd ..
cd ..
make html
abrowser _build/html/ejercicios/formularios/anexo_formularios.html
popd
