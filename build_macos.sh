#!/bin/bash
# Skrypt budowania dla macOS
# Tworzy plik .app z wszystkimi zależnościami

set -e  # Zatrzymaj przy błędzie

echo "========================================"
echo "Media Downloader - Build Script (macOS)"
echo "========================================"
echo ""

# Kolory dla outputu
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Sprawdź czy Python jest zainstalowany
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[BŁĄD]${NC} Python3 nie jest zainstalowany!"
    echo "Zainstaluj Python: brew install python3"
    exit 1
fi

echo "[1/7] Sprawdzanie Pythona..."
python3 --version
echo ""

# Sprawdź czy Homebrew jest zainstalowany
if ! command -v brew &> /dev/null; then
    echo -e "${YELLOW}[UWAGA]${NC} Homebrew nie jest zainstalowany."
    echo "Zainstaluj Homebrew z: https://brew.sh"
fi

echo "[2/7] Tworzenie wirtualnego środowiska..."
if [ -d "venv" ]; then
    echo "Usuwanie starego venv..."
    rm -rf venv
fi
python3 -m venv venv
source venv/bin/activate
echo ""

echo "[3/7] Aktualizacja pip..."
pip install --upgrade pip
echo ""

echo "[4/7] Instalowanie zależności..."
pip install -r requirements.txt
echo ""

echo "[5/7] Instalowanie PyInstaller..."
pip install pyinstaller
echo ""

echo "[6/7] Czyszczenie poprzednich buildów..."
rm -rf build dist
echo ""

echo "[7/7] Budowanie aplikacji..."
echo "To może potrwać kilka minut..."
pyinstaller media_downloader.spec --clean
echo ""

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Budowanie zakończone!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Aplikacja znajduje się w: dist/MediaDownloader.app"
echo ""

echo -e "${YELLOW}[UWAGA] FFmpeg:${NC}"
echo "FFmpeg powinien być zainstalowany w systemie:"
echo "  brew install ffmpeg"
echo ""
echo "Lub skopiuj binarkę ffmpeg do:"
echo "  dist/MediaDownloader.app/Contents/MacOS/"
echo ""

echo "Aby stworzyć DMG:"
echo "  1. Zainstaluj create-dmg: brew install create-dmg"
echo "  2. Uruchom: ./create_dmg.sh"
echo ""

echo "Aby uruchomić aplikację:"
echo "  open dist/MediaDownloader.app"
echo ""
