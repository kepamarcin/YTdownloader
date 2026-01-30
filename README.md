### YouTube Video Downloader

Aplikacja konsolowa do pobierania wideo z YouTube przy użyciu najnowszej wersji `yt-dlp` i `ffmpeg`. Zoptymalizowana pod kątem YouTube, obsługuje standardowe wideo, Shorts, transmisje na żywo oraz playlisty.

**Autor:** Marcin Kępa  
**GitHub:** [https://github.com/kepamarcin/YTdownloader](https://github.com/kepamarcin/YTdownloader)

---

#### 🚀 Wymagania wstępne

Zanim zaczniesz, upewnij się, że masz zainstalowane niezbędne narzędzia.

#### 1. Instalacja Git

**Windows:**
1. Pobierz instalator ze strony [git-scm.com](https://git-scm.com/download/win).
2. Uruchom instalator i postępuj zgodnie z instrukcjami (domyślne ustawienia są zazwyczaj wystarczające).
3. Po instalacji otwórz terminal (CMD lub PowerShell) i wpisz `git --version`, aby sprawdzić poprawność instalacji.

**Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install git
```

**macOS:**
Jeśli masz zainstalowane Homebrew:
```bash
brew install git
```

#### 2. Instalacja Python

**Windows:**
1. Pobierz instalator ze strony [python.org](https://www.python.org/).
2. **Ważne:** Podczas instalacji zaznacz opcję **"Add Python to PATH"**.
3. Kliknij "Install Now".

**Linux/macOS:**
Python jest zazwyczaj zainstalowany domyślnie. Sprawdź wersję wpisując:
```bash
python3 --version
```
Wymagana wersja: Python 3.8 lub nowszy.

---

#### 📥 Pobieranie repozytorium

Otwórz terminal w folderze, w którym chcesz zapisać projekt i wykonaj polecenie:
```bash
git clone https://github.com/kepamarcin/YTdownloader.git
cd YTdownloader
```

---

#### ⚙️ Instalacja i konfiguracja

#### 1. Utwórz środowisko wirtualne

**Windows:**
```powershell
python -m venv venv
# Jeśli wystąpi błąd uprawnień, wykonaj: Set-ExecutionPolicy Bypass -Scope Process
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. Zainstaluj zależności

Upewnij się, że środowisko wirtualne jest aktywne (powinieneś widzieć `(venv)` w terminalu), a następnie zainstaluj biblioteki:
```bash
pip install -r requirements.txt
```

Zaleca się również aktualizację `yt-dlp` do najnowszej wersji:
```bash
pip install --upgrade yt-dlp
```

#### 3. Konfiguracja FFmpeg

Aplikacja wymaga `ffmpeg` do łączenia strumieni wideo i audio.

1. Pobierz FFmpeg ze strony [ffmpeg.org](https://ffmpeg.org/).
2. Umieść plik wykonywalny w katalogu `ffmpeg/` wewnątrz projektu.
   - **Windows:** Plik `ffmpeg.exe` umieść w `ffmpeg/ffmpeg.exe`.
   - **Linux/macOS:** Plik binarny `ffmpeg` umieść w `ffmpeg/ffmpeg` (pamiętaj o nadaniu uprawnień: `chmod +x ffmpeg/ffmpeg`).

---

#### ▶️ Uruchomienie

Upewnij się, że jesteś w katalogu projektu i masz aktywne środowisko wirtualne.

**Windows:**
```powershell
python main.py
```

**Linux/macOS:**
```bash
python3 main.py
```

---

#### 📖 Użycie

1. Uruchom aplikację.
2. Wklej URL YouTube, gdy zostaniesz o to poproszony.
3. Poczekaj na pobranie (postęp będzie wyświetlany w konsoli).
4. Plik MP4 zostanie zapisany w katalogu `downloads/`.
5. Wpisz `q`, aby wyjść z programu.

**Obsługiwane formaty URL:**
* `https://www.youtube.com/watch?v=XXXX` (standardowe wideo)
* `https://youtu.be/XXXX` (skrócony link)
* `https://youtube.com/shorts/XXXX` (YouTube Shorts)
* `https://youtube.com/live/XXXX` (transmisje na żywo)
* `https://youtube.com/playlist?list=XXXX` (playlisty)

---

#### 📂 Struktura katalogów

```text
video_downloader/
├── ffmpeg/           <- Tu umieść plik ffmpeg/ffmpeg.exe
│   └── ffmpeg(.exe)
├── downloads/        <- Tu będą zapisywane pobrane filmy (MP4)
├── venv/             <- Środowisko wirtualne
├── main.py           <- Główny plik aplikacji
├── requirements.txt  <- Lista zależności
└── readme.txt        <- Oryginalna dokumentacja
```

---

#### 🔧 Konfiguracja wewnętrzna

Aplikacja jest domyślnie skonfigurowana dla optymalnej wydajności:
* **Format:** Najlepsza jakość do 1080p w MP4.
* **Player client:** Android + Web (dla lepszej kompatybilności).
* **Geo bypass:** Włączony.
* **Retry:** 10 prób przy błędach sieciowych.
* **Timeout:** 30 sekund.

---

#### ❓ Rozwiązywanie problemów

| Problem | Rozwiązanie |
| :--- | :--- |
| "Nie znaleziono ffmpeg" | Upewnij się, że plik `ffmpeg` (lub `ffmpeg.exe`) znajduje się w folderze `ffmpeg/`. |
| "Sign in to confirm your age" | Wideo ma ograniczenie wiekowe i wymaga plików cookies (obecnie nieobsługiwane w tej wersji). |
| "Video unavailable" | Wideo może być zablokowane w Twoim regionie lub usunięte. |
| Wolne pobieranie | YouTube może ograniczać prędkość (throttling) - jest to normalne zachowanie serwisu. |
| Błędy pobierania | Spróbuj zaktualizować bibliotekę: `pip install --upgrade yt-dlp`. |
