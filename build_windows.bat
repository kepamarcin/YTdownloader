@echo off
REM Skrypt budowania dla Windows
REM Tworzy plik .exe z wszystkimi zależnościami

echo ========================================
echo Media Downloader - Build Script (Windows)
echo ========================================
echo.

REM Sprawdź czy Python jest zainstalowany
python --version >nul 2>&1
if errorlevel 1 (
    echo [BŁĄD] Python nie jest zainstalowany lub nie jest w PATH!
    echo Pobierz Python z: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/6] Sprawdzanie Pythona...
python --version
echo.

echo [2/6] Instalowanie zależności...
pip install -r requirements.txt
if errorlevel 1 (
    echo [BŁĄD] Nie udało się zainstalować zależności!
    pause
    exit /b 1
)
echo.

echo [3/6] Instalowanie PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo [BŁĄD] Nie udało się zainstalować PyInstaller!
    pause
    exit /b 1
)
echo.

echo [4/6] Czyszczenie poprzednich buildów...
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
echo.

echo [5/6] Budowanie aplikacji...
echo To może potrwać kilka minut...
pyinstaller media_downloader.spec --clean
if errorlevel 1 (
    echo [BŁĄD] Budowanie nie powiodło się!
    pause
    exit /b 1
)
echo.

echo [6/6] Kopiowanie FFmpeg...
echo.
echo UWAGA: Musisz ręcznie skopiować ffmpeg.exe do folderu dist/
echo Pobierz FFmpeg z: https://github.com/BtbN/FFmpeg-Builds/releases
echo Skopiuj ffmpeg.exe do: dist\MediaDownloader\_internal\
echo.

echo ========================================
echo Budowanie zakończone!
echo ========================================
echo.
echo Aplikacja znajduje się w folderze: dist\MediaDownloader.exe
echo.
echo Aby stworzyć instalator:
echo 1. Pobierz Inno Setup: https://jrsoftware.org/isdl.php
echo 2. Użyj pliku installer_windows.iss
echo.
pause
