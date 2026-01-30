#!/bin/bash
# Skrypt tworzący DMG dla macOS

set -e

echo "========================================"
echo "Tworzenie DMG dla Media Downloader"
echo "========================================"
echo ""

APP_NAME="MediaDownloader"
VERSION="1.0.0"
DMG_NAME="${APP_NAME}-${VERSION}-macOS"

# Sprawdź czy aplikacja istnieje
if [ ! -d "dist/${APP_NAME}.app" ]; then
    echo "[BŁĄD] Nie znaleziono dist/${APP_NAME}.app"
    echo "Najpierw uruchom: ./build_macos.sh"
    exit 1
fi

# Sprawdź czy create-dmg jest zainstalowany
if ! command -v create-dmg &> /dev/null; then
    echo "[BŁĄD] create-dmg nie jest zainstalowane"
    echo "Zainstaluj: brew install create-dmg"
    exit 1
fi

echo "[1/3] Usuwanie starego DMG..."
rm -f "dist/${DMG_NAME}.dmg"
echo ""

echo "[2/3] Tworzenie DMG..."
create-dmg \
  --volname "${APP_NAME}" \
  --volicon "assets/icon.icns" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "${APP_NAME}.app" 200 190 \
  --hide-extension "${APP_NAME}.app" \
  --app-drop-link 600 185 \
  "dist/${DMG_NAME}.dmg" \
  "dist/${APP_NAME}.app"
echo ""

echo "[3/3] Gotowe!"
echo ""
echo "========================================"
echo "DMG utworzony: dist/${DMG_NAME}.dmg"
echo "========================================"
echo ""
