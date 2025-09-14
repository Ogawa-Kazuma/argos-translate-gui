@echo off
cd /d "%~dp0\.."
.venv\Scripts\python.exe src\argos_translate_gui_safe.py
pause
