@echo off
echo CTI Analysis Pipeline Runner
echo ===========================

REM Check if running on Windows with PowerShell available
where powershell >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    REM Check if WSL is available for better cross-platform compatibility
    powershell -Command "Get-Command wsl.exe -ErrorAction SilentlyContinue" >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        REM WSL is available, check if run_pipeline.sh exists
        if exist run_pipeline.sh (
            echo Using cross-platform script for better compatibility...
            bash run_pipeline.sh %*
            goto :eof
        )
    )
)

if "%1"=="" (
    echo Usage: run_pipeline.bat [demo^|api^|process^|test]
    echo.
    echo demo    - Run the demo
    echo api     - Start the API server
    echo process - Process a CTI report file
    echo test    - Run unit tests
    goto :eof
)

if "%1"=="demo" (
    echo Running demo...
    python src/main.py --mode demo
) else if "%1"=="api" (
    echo Starting API server...
    echo API will be available at http://localhost:5000
    python src/main.py --mode api
) else if "%1"=="process" (
    if "%2"=="" (
        echo Please specify a file to process
        echo Usage: run_pipeline.bat process ^<file_path^>
        goto :eof
    )
    echo Processing file: %2
    python src/main.py --mode process --input %2
) else if "%1"=="test" (
    echo Running unit tests...
    python -m unittest src/tests/test_pipeline.py
) else (
    echo Unknown command: %1
    echo Usage: run_pipeline.bat [demo^|api^|process^|test]
)

:eof