# 🎨 Assets - Ikony aplikacji

Ten folder zawiera ikony aplikacji używane podczas pakowania.

## 📋 Wymagane pliki

### Windows
- **icon.ico** - Ikona aplikacji (256x256 px, format .ico)

### macOS
- **icon.icns** - Ikona aplikacji (format .icns z różnymi rozdzielczościami)

## 🛠️ Jak stworzyć ikony

### Metoda 1: Użyj generatora online

1. Stwórz logo 1024x1024 px w formacie PNG
2. Użyj [icoconvert.com](https://icoconvert.com/) dla .ico
3. Użyj [cloudconvert.com](https://cloudconvert.com/png-to-icns) dla .icns

### Metoda 2: Użyj narzędzi lokalnych

#### Windows (.ico)
Użyj ImageMagick:
```bash
magick convert icon.png -define icon:auto-resize=256,128,64,48,32,16 icon.ico
```

#### macOS (.icns)
Użyj narzędzia `iconutil`:
```bash
# Stwórz folder z ikonami
mkdir icon.iconset

# Wygeneruj różne rozmiary
sips -z 16 16 icon.png --out icon.iconset/icon_16x16.png
sips -z 32 32 icon.png --out icon.iconset/icon_16x16@2x.png
sips -z 32 32 icon.png --out icon.iconset/icon_32x32.png
sips -z 64 64 icon.png --out icon.iconset/icon_32x32@2x.png
sips -z 128 128 icon.png --out icon.iconset/icon_128x128.png
sips -z 256 256 icon.png --out icon.iconset/icon_128x128@2x.png
sips -z 256 256 icon.png --out icon.iconset/icon_256x256.png
sips -z 512 512 icon.png --out icon.iconset/icon_256x256@2x.png
sips -z 512 512 icon.png --out icon.iconset/icon_512x512.png
sips -z 1024 1024 icon.png --out icon.iconset/icon_512x512@2x.png

# Konwertuj do .icns
iconutil -c icns icon.iconset
```

## 📝 Uwagi

- Jeśli nie dodasz ikon, aplikacja będzie używać domyślnych ikon systemowych
- Ikony nie są wymagane do działania aplikacji
- Dla profesjonalnego wyglądu, zalecane jest dodanie własnych ikon
