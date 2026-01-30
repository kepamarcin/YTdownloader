# 🎬 Media Downloader

**Cross-platform aplikacja desktopowa do pobierania multimediów z YouTube i innych platform streamingowych**

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📋 Spis treści

- [Opis](#-opis)
- [Funkcjonalności](#-funkcjonalności)
- [Wymagania](#-wymagania)
- [Instalacja dla developerów](#-instalacja-dla-developerów)
- [Uruchomienie aplikacji](#-uruchomienie-aplikacji)
- [Budowanie aplikacji standalone](#-budowanie-aplikacji-standalone)
  - [Windows (.exe)](#windows-exe)
  - [macOS (.app / .dmg)](#macos-app--dmg)
- [Instalacja FFmpeg](#-instalacja-ffmpeg)
- [Struktura projektu](#-struktura-projektu)
- [Obsługiwane platformy](#-obsługiwane-platformy)
- [FAQ](#-faq)
- [Licencja](#-licencja)
- [Kontakt](#-kontakt)

---

## 📖 Opis

**Media Downloader** to nowoczesna, cross-platform aplikacja desktopowa stworzona w Pythonie, która umożliwia łatwe pobieranie wideo i audio z ponad 1000+ platform streamingowych, w tym:

- YouTube
- Vimeo
- DailyMotion
- Facebook
- Twitter
- Instagram
- i wiele innych!

Aplikacja oferuje intuicyjny GUI (CustomTkinter) oraz zaawansowane opcje pobierania, takie jak wybór jakości wideo, konwersja do MP3, oraz pobieranie wielu plików jednocześnie.

---

## ✨ Funkcjonalności

### 🎯 Główne funkcje

- ✅ **Nowoczesny GUI** - Ciemny motyw, intuicyjny interfejs
- ✅ **Pobieranie z wielu platform** - Ponad 1000+ obsługiwanych stron
- ✅ **Wsadowe pobieranie** - Wklej wiele linków jednocześnie
- ✅ **Wybór jakości wideo** - Najlepsza, 1080p, 720p, 480p, 360p
- ✅ **Konwersja do MP3** - Pobieraj tylko audio w wysokiej jakości
- ✅ **Pasek postępu** - Zobacz status pobierania w czasie rzeczywistym
- ✅ **Logi szczegółowe** - Śledź każdy krok procesu
- ✅ **Cross-platform** - Działa na Windows i macOS
- ✅ **Standalone** - Wszystkie zależności wbudowane

### 🖼️ Interface

```
┌─────────────────────────────────────────┐
│   🎬 Media Downloader                   │
│   Pobieraj wideo i audio                │
├─────────────────────────────────────────┤
│ 📎 Linki do pobrania:                   │
│ ┌─────────────────────────────────────┐ │
│ │ https://youtube.com/watch?v=...    │ │
│ │ https://vimeo.com/...              │ │
│ └─────────────────────────────────────┘ │
├─────────────────────────────────────────┤
│ ⚙️ Opcje:                               │
│ Jakość: [1080p ▼]  ☑️ Tylko audio      │
│ Katalog: /Users/downloads [Wybierz]    │
├─────────────────────────────────────────┤
│ [⬇️ Pobierz]           [ℹ️ O aplikacji]│
├─────────────────────────────────────────┤
│ 📊 Postęp: ████████░░ 80%              │
│ 📝 Logi: Pobieranie 2/3...             │
└─────────────────────────────────────────┘
```

---

## 🔧 Wymagania

### Dla użytkowników końcowych

**Aplikacja standalone nie wymaga instalacji Pythona ani innych zależności!**

- **Windows**: Windows 10/11 (64-bit)
- **macOS**: macOS 10.13+ (High Sierra lub nowszy)

### Dla developerów

- Python 3.8 lub nowszy
- pip (menedżer pakietów Python)
- FFmpeg (dla konwersji audio/wideo)

---

## 💻 Instalacja dla developerów

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/username/media-downloader.git
cd media-downloader
```

### 2. Utwórz wirtualne środowisko (opcjonalne, ale zalecane)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Zainstaluj zależności

```bash
pip install -r requirements.txt
```

### 4. Zainstaluj FFmpeg (wymagane do konwersji audio)

Zobacz sekcję [Instalacja FFmpeg](#-instalacja-ffmpeg).

---

## 🚀 Uruchomienie aplikacji

### Tryb deweloperski

Po zainstalowaniu zależności, uruchom aplikację:

```bash
python main.py
```

lub

```bash
python3 main.py
```

---

## 📦 Budowanie aplikacji standalone

### Windows (.exe)

#### Krok 1: Zainstaluj zależności

```bash
pip install -r requirements.txt
pip install pyinstaller
```

#### Krok 2: Uruchom skrypt buildowania

```bash
build_windows.bat
```

Lub manualnie:

```bash
pyinstaller media_downloader.spec --clean
```

#### Krok 3: Wbuduj FFmpeg

1. Pobierz FFmpeg z [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
2. Rozpakuj archiwum
3. Skopiuj `ffmpeg.exe` do `dist\MediaDownloader\_internal\`

#### Krok 4: Testuj aplikację

```bash
dist\MediaDownloader.exe
```

#### Krok 5 (Opcjonalnie): Stwórz instalator

Użyj [Inno Setup](https://jrsoftware.org/isdl.php):

1. Zainstaluj Inno Setup
2. Otwórz `installer_windows.iss`
3. Skompiluj instalator
4. Instalator zostanie stworzony w `dist\installer\`

**Wynik:**
- Pojedynczy plik EXE: `dist\MediaDownloader.exe`
- Instalator: `dist\installer\MediaDownloader-Setup-1.0.0.exe`

---

### macOS (.app / .dmg)

#### Krok 1: Nadaj uprawnienia wykonania skryptom

```bash
chmod +x build_macos.sh
chmod +x create_dmg.sh
```

#### Krok 2: Uruchom skrypt buildowania

```bash
./build_macos.sh
```

Ten skrypt automatycznie:
- Tworzy wirtualne środowisko
- Instaluje zależności
- Buduje aplikację .app

#### Krok 3: Wbuduj FFmpeg

**Opcja A - Zainstaluj systemowo (zalecane):**

```bash
brew install ffmpeg
```

**Opcja B - Wbuduj w aplikację:**

```bash
# Pobierz FFmpeg
curl -O https://evermeet.cx/ffmpeg/ffmpeg-5.1.2.zip
unzip ffmpeg-5.1.2.zip

# Skopiuj do aplikacji
cp ffmpeg dist/MediaDownloader.app/Contents/MacOS/
```

#### Krok 4: Testuj aplikację

```bash
open dist/MediaDownloader.app
```

#### Krok 5 (Opcjonalnie): Stwórz DMG

```bash
# Zainstaluj create-dmg
brew install create-dmg

# Stwórz DMG
./create_dmg.sh
```

**Wynik:**
- Aplikacja: `dist/MediaDownloader.app`
- DMG: `dist/MediaDownloader-1.0.0-macOS.dmg`

---

## 🎥 Instalacja FFmpeg

FFmpeg jest wymagany do konwersji audio/wideo.

### Windows

#### Metoda 1: Automatyczna (Chocolatey)

```bash
choco install ffmpeg
```

#### Metoda 2: Manualna

1. Pobierz z [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
2. Rozpakuj archiwum
3. Dodaj `bin\` do zmiennej środowiskowej PATH
4. Lub skopiuj `ffmpeg.exe` do folderu z aplikacją

### macOS

#### Metoda 1: Homebrew (zalecana)

```bash
brew install ffmpeg
```

#### Metoda 2: MacPorts

```bash
sudo port install ffmpeg
```

### Weryfikacja instalacji

```bash
ffmpeg -version
```

Powinieneś zobaczyć informację o wersji FFmpeg.

---

## 📁 Struktura projektu

```
media-downloader/
│
├── main.py                      # Główny plik aplikacji
├── downloader.py                # Moduł pobierania (yt-dlp)
├── about_window.py              # Okno "O aplikacji"
├── requirements.txt             # Zależności Python
│
├── media_downloader.spec        # Konfiguracja PyInstaller
├── build_windows.bat            # Skrypt budowania (Windows)
├── build_macos.sh               # Skrypt budowania (macOS)
├── create_dmg.sh                # Skrypt tworzenia DMG (macOS)
├── installer_windows.iss        # Konfiguracja Inno Setup
│
├── .gitignore                   # Ignorowane pliki Git
├── LICENSE.txt                  # Licencja MIT
└── README.md                    # Ten plik
```

---

## 🌐 Obsługiwane platformy

Media Downloader wykorzystuje **yt-dlp**, który obsługuje ponad 1000+ platform, w tym:

### 🎬 Wideo
- YouTube
- Vimeo
- DailyMotion
- Twitch
- Facebook Video
- Instagram Video
- Twitter Video
- TikTok
- Reddit Video

### 🎵 Audio
- SoundCloud
- Bandcamp
- Mixcloud
- Spotify (wymaga premium)

### 📺 Streaming
- Twitch VODs
- YouTube Live
- Facebook Live

### 🌍 Międzynarodowe
- Bilibili (Chiny)
- Youku (Chiny)
- VK (Rosja)
- Naver (Korea)
- Niconico (Japonia)

**...i setki innych!**

Pełna lista: [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

---

## ❓ FAQ

### 1. Aplikacja nie uruchamia się na macOS - "nie można otworzyć"

macOS blokuje aplikacje od nieznanych developerów. Rozwiązanie:

```bash
xattr -cr dist/MediaDownloader.app
```

Lub przytrzymaj Ctrl + kliknij na aplikację → Otwórz.

### 2. Brak konwersji do MP3 - "ffmpeg not found"

Zainstaluj FFmpeg:
- **Windows**: `choco install ffmpeg` lub pobierz z [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
- **macOS**: `brew install ffmpeg`

### 3. Pobieranie kończy się błędem "ERROR: Unable to download"

Sprawdź:
- Czy link jest prawidłowy
- Czy wideo jest dostępne publicznie
- Czy masz połączenie z internetem
- Aktualizuj yt-dlp: `pip install --upgrade yt-dlp`

### 4. Jak pobierać playlisty?

Wklej link do playlisty w pole tekstowe - wszystkie wideo zostaną pobrane automatycznie.

### 5. Aplikacja pobiera wolno

- Wybierz niższą jakość wideo
- Sprawdź prędkość internetu
- Niektóre platformy mają ograniczenia prędkości

### 6. Czy mogę pobierać z platform dla dorosłych?

Tak, yt-dlp obsługuje wiele platform. Aplikacja nie posiada żadnych ograniczeń.

### 7. Jak zaktualizować yt-dlp w aplikacji standalone?

Przebuduj aplikację z najnowszą wersją yt-dlp:

```bash
pip install --upgrade yt-dlp
pyinstaller media_downloader.spec --clean
```

---

## 🛠️ Rozwój projektu

### Uruchomienie testów

```bash
python -m pytest tests/
```

### Formatowanie kodu

```bash
pip install black
black .
```

### Linting

```bash
pip install pylint
pylint *.py
```

---

## 🐛 Zgłaszanie błędów

Znalazłeś błąd? Otwórz issue na GitHubie:

[https://github.com/username/media-downloader/issues](https://github.com/username/media-downloader/issues)

Dołącz:
- Opis problemu
- Kroki do reprodukcji
- Logi z aplikacji
- System operacyjny i wersja

---

## 🤝 Wkład w projekt

Contributions are welcome! 

1. Fork repozytorium
2. Stwórz branch (`git checkout -b feature/AmazingFeature`)
3. Commit zmiany (`git commit -m 'Add some AmazingFeature'`)
4. Push do brancha (`git push origin feature/AmazingFeature`)
5. Otwórz Pull Request

---

## 📜 Licencja

Ten projekt jest licencjonowany na licencji **MIT** - zobacz plik [LICENSE.txt](LICENSE.txt) dla szczegółów.

---

## 📧 Kontakt

**Twórca:** Your Name

- 📧 Email: [email@example.com](mailto:email@example.com)
- 🐙 GitHub: [github.com/username](https://github.com/username)

---

## 🎉 Podziękowania

Ten projekt wykorzystuje:

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Nowoczesny GUI framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Potężne narzędzie do pobierania
- [FFmpeg](https://ffmpeg.org/) - Konwersja multimediów
- [PyInstaller](https://pyinstaller.org/) - Pakowanie aplikacji

---

## 🌟 Star History

Jeśli podoba Ci się ten projekt, zostaw gwiazdkę ⭐ na GitHubie!

---

**Made with ❤️ and Python**
