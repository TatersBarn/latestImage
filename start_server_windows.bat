@echo off

REM Check if python command is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is required but not found. Please install Python.
    exit /b 1
)

REM Start the server
python latest_image_server.py

