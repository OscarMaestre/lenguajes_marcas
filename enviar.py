call reconstruir.bat
del apuntes.zip
set ZIP=.\7z\App\7-Zip\7z.exe
@echo Reconstruyendo directorio de apuntes
xcopy /S /Y _build\singlehtml\*.* LenguajesDeMarcas\html
copy /Y _build\latex\.pdf LenguajesDeMarcas\pdf
copy /Y *.rst LenguajesDeMarcas\txt
copy /Y *.png LenguajesDeMarcas\txt
copy /Y *.jpg LenguajesDeMarcas\txt
copy /Y *.py LenguajesDeMarcas\txt
@echo Generando apuntes...

%ZIP%  a apuntes.zip .\LenguajesDeMarcas\
@call enviar.py profesor.oscar.gomez@gmail.com atlantis_3031 marcas-maestre-2014.zip