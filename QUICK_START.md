# 🚀 Szybki Start - Media Downloader

## Dla użytkowników końcowych

### ⬇️ Pobranie aplikacji

1. Przejdź do zakładki [Releases](https://github.com/username/media-downloader/releases)
2. Pobierz najnowszą wersję dla swojego systemu:
   - **Windows**: `MediaDownloader-Setup-1.0.0.exe` (instalator) lub `MediaDownloader.exe` (standalone)
   - **macOS**: `MediaDownloader-1.0.0-macOS.dmg`

### 📝 Instrukcja użytkowania

#### 1. Instalacja

**Windows:**
- Jeśli pobrałeś instalator: Uruchom i postępuj zgodnie z instrukcjami
- Jeśli pobrałeś standalone: Po prostu uruchom plik .exe

**macOS:**
1. Otwórz plik .dmg
2. Przeciągnij aplikację do folderu Applications
3. Uruchom aplikację (przy pierwszym uruchomieniu: Ctrl+kliknij → Otwórz)

#### 2. Pierwsze użycie

```
┌────────────────────────────────────────────┐
│ 🎬 Media Downloader                        │
├────────────────────────────────────────────┤
│ 1. Wklej link(i) w pole tekstowe           │
│    Przykład: https://youtube.com/watch?v=..│
│                                             │
│ 2. Wybierz opcje:                          │
│    ✓ Jakość wideo: 1080p                   │
│    ☐ Tylko audio (MP3)                     │
│                                             │
│ 3. Wybierz katalog zapisu                  │
│                                             │
│ 4. Kliknij "Pobierz"                       │
│                                             │
│ 5. Poczekaj na zakończenie                 │
└────────────────────────────────────────────┘
```

#### 3. Wsadowe pobieranie

Aby pobrać wiele plików naraz:

```
https://youtube.com/watch?v=video1
https://vimeo.com/video2
https://dailymotion.com/video3
```

Każdy link w nowej linii!

### ❓ Najczęstsze pytania

**Q: Gdzie znajdują się pobrane pliki?**
A: W katalogu, który wybrałeś w opcjach. Domyślnie: `Downloads`

**Q: Aplikacja nie pobiera wideo**
A: Sprawdź:
- Czy link jest prawidłowy
- Czy wideo jest dostępne publicznie
- Czy masz połączenie z internetem

**Q: Jak pobrać tylko dźwięk?**
A: Zaznacz checkbox "🎵 Tylko audio (MP3)"

**Q: Jakie platformy są obsługiwane?**
A: YouTube, Vimeo, DailyMotion, Facebook, Instagram, TikTok, Twitter i 1000+ innych!

**Q: Czy to jest legalne?**
A: Pobieranie może naruszać regulaminy niektórych platform. Używaj odpowiedzialnie i zgodnie z prawem lokalnym.

### 🆘 Pomoc

Problemy? Skontaktuj się:
- 📧 Email: email@example.com
- 🐙 GitHub Issues: github.com/username/media-downloader/issues

---

## Dla developerów

### 🔨 Szybka instalacja

```bash
# Sklonuj
git clone https://github.com/username/media-downloader.git
cd media-downloader

# Zainstaluj
pip install -r requirements.txt

# Uruchom
python main.py
```

### 📦 Szybkie budowanie

**Windows:**
```bash
build_windows.bat
```

**macOS:**
```bash
./build_macos.sh
```

Więcej w [README.md](README.md)

---

**Made with ❤️ and Python**
