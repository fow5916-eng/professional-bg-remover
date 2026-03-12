@echo off
title AI Image Background Remover
echo ----------------------------------------
echo         AI BACKGROUND REMOVER           
echo ----------------------------------------
echo.
set /p img="Drag and drop your image file here and press Enter: "
echo.
echo Processing... Please wait.
python main.py -i %img%
echo.
echo ----------------------------------------
pause
