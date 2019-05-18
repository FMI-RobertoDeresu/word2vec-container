@echo off
:: echo Seting virtual environment
:: env/scripts/activate.bat

echo Set current directory
cd /d %~dp0 

echo Running application
.\env\scripts\python main.py

echo All done!
pause