### YouTube Video Downloader v2

Aplikacja konsolowa do pobierania wideo z YouTube w wysokiej rozdzielczosci (do 1080p) przy uzyciu `yt-dlp`, `ffmpeg` i systemu PO Token. Obsluguje standardowe wideo, Shorts, transmisje na zywo oraz playlisty.

**Autor:** Marcin Kepa  
**GitHub:** [https://github.com/kepamarcin/YTdownloader](https://github.com/kepamarcin/YTdownloader)

---

#### Wymagania wstepne

Zanim zaczniesz, upewnij sie, ze masz zainstalowane niezbedne narzedzia.

#### 1. Git

**Windows:**
1. Pobierz instalator ze strony [git-scm.com](https://git-scm.com/download/win).
2. Uruchom instalator i postepuj zgodnie z instrukcjami (domyslne ustawienia sa zazwyczaj wystarczajace).
3. Po instalacji otwórz terminal (CMD lub PowerShell) i wpisz `git --version`, aby sprawdzic poprawnosc instalacji.

**Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install git
```

**macOS:**
```bash
brew install git
```

#### 2. Python (3.8+)

**Windows:**
1. Pobierz instalator ze strony [python.org](https://www.python.org/).
2. **Wazne:** Podczas instalacji zaznacz opcje **"Add Python to PATH"**.
3. Kliknij "Install Now".

**Linux/macOS:**
Python jest zazwyczaj zainstalowany domyslnie. Sprawdz wersje:
```bash
python3 --version
```

#### 3. Node.js (20+)

Node.js jest wymagany do rozwiazywania zabezpieczen YouTube (n-challenge oraz generowanie PO Token).

**Windows:**
Pobierz instalator ze strony [nodejs.org](https://nodejs.org/) (wersja LTS). Po instalacji sprawdz:
```powershell
node --version
```

**Linux (Debian/Ubuntu):**
```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

**macOS:**
```bash
brew install node
```

---

#### Pobieranie repozytorium

Otwórz terminal w folderze, w którym chcesz zapisac projekt i wykonaj polecenie:
```bash
git clone https://github.com/kepamarcin/YTdownloader.git
cd YTdownloader
```

---

#### Instalacja i konfiguracja

#### 1. Utwórz srodowisko wirtualne

**Windows:**
```powershell
python -m venv venv
# Jesli wystapi blad uprawnien, wykonaj: Set-ExecutionPolicy Bypass -Scope Process
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. Zainstaluj zaleznosci

Upewnij sie, ze srodowisko wirtualne jest aktywne (powinienes widziec `(venv)` w terminalu), a nastepnie zainstaluj biblioteki:
```bash
pip install -r requirements.txt
```

#### 3. Skonfiguruj PO Token (wymagane do HD)

YouTube wymaga tokenów PO (Proof of Origin) do udostepniania wideo w wysokiej rozdzielczosci. Bez tego kroku dostepna bedzie tylko jakosc 360p.

Bedac w katalogu `YTdownloader/`, wykonaj (dziala tak samo na Windows/macOS/Linux):

```bash
git clone --single-branch --branch 1.3.1 https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git bgutil-ytdlp-pot-provider
cd bgutil-ytdlp-pot-provider/server
npm ci
npx tsc
cd ../..
```

> **Uwaga:** Repozytorium bgutil jest klonowane do podkatalogu projektu (`./bgutil-ytdlp-pot-provider`). Aplikacja automatycznie wykrywa skrypt `server/build/generate_once.js` w tej lokalizacji i przekazuje jego sciezke do yt-dlp, wiec dziala przenosnie na Windows, macOS i Linux.

---

#### Uruchomienie

Upewnij sie, ze jestes w katalogu projektu i masz aktywne srodowisko wirtualne.

**Windows:**
```powershell
python main.py
```

**Linux/macOS:**
```bash
python3 main.py
```

**Po zakonczeniu pracy — deaktywacja venv:**
```bash
deactivate
```

---

#### Uzycie

1. Uruchom aplikacje.
2. Wklej URL YouTube, gdy zostaniesz o to poproszony.
3. Poczekaj na pobranie (postep bedzie wyswietlany w konsoli).
4. Plik MP4 zostanie zapisany w katalogu `downloads/`.
5. Wpisz `q`, aby wyjsc z programu.

**Obslugiwane formaty URL:**
* `https://www.youtube.com/watch?v=XXXX` (standardowe wideo)
* `https://youtu.be/XXXX` (skrócony link)
* `https://youtube.com/shorts/XXXX` (YouTube Shorts)
* `https://youtube.com/live/XXXX` (transmisje na zywo)
* `https://youtube.com/playlist?list=XXXX` (playlisty)

---

#### Struktura katalogów

```text
YTdownloader/
├── ffmpeg/                      <- Plik ffmpeg/ffmpeg.exe (dolaczony)
│   └── ffmpeg(.exe)
├── bgutil-ytdlp-pot-provider/   <- Sklonowane repo bgutil (krok 3)
├── downloads/                   <- Pobrane filmy (MP4)
├── venv/                        <- Srodowisko wirtualne
├── main.py                      <- Glówny plik aplikacji
├── requirements.txt             <- Lista zaleznosci
└── README.md                    <- Dokumentacja
```

---

#### Konfiguracja wewnetrzna

Aplikacja jest domyslnie skonfigurowana dla optymalnej wydajnosci:
* **Format:** Najlepsza jakosc do 1080p w MP4.
* **Player client:** Web + mWeb (z obsluga PO tokenów).
* **JS Runtime:** Node.js (do rozwiazywania n-challenge YouTube).
* **PO Token:** Automatyczne generowanie przez bgutil (tryb script).
* **Geo bypass:** Wlaczony.
* **Retry:** 10 prób przy bledach sieciowych.
* **Timeout:** 30 sekund.

---

#### Rozwiazywanie problemów

| Problem | Rozwiazanie |
| :--- | :--- |
| "Nie znaleziono ffmpeg" | Upewnij sie, ze plik `ffmpeg` (lub `ffmpeg.exe`) znajduje sie w folderze `ffmpeg/`. |
| "ffmpeg is not installed" przy HD | Sprawdz czy w folderze `ffmpeg/` jest plik `ffmpeg.exe` (Windows) lub `ffmpeg` (Linux/macOS). |
| Tylko 360p, brak HD | Sprawdz czy bgutil jest sklonowany i zbudowany w `./bgutil-ytdlp-pot-provider/server/` (w katalogu projektu). Sprawdz czy Node.js >= 20 jest zainstalowany: `node --version`. |
| WARNING: pot:bgutil:http | To normalne ostrzezenie — plugin automatycznie przechodzi na tryb script. Mozna zignorowac. |
| "n challenge solving failed" | Zainstaluj Node.js >= 20 i upewnij sie, ze jest w PATH. Zaktualizuj yt-dlp: `pip install -U "yt-dlp[default]"`. |
| "Sign in to confirm your age" | Wideo ma ograniczenie wiekowe i wymaga plików cookies (obecnie nieobslugiwane w tej wersji). |
| "Video unavailable" | Wideo moze byc zablokowane w Twoim regionie lub usuniete. |
| Wolne pobieranie | YouTube moze ograniczac predkosc (throttling) — jest to normalne zachowanie serwisu. |
| Bledy pobierania | Spróbuj zaktualizowac: `pip install -U "yt-dlp[default]" bgutil-ytdlp-pot-provider`. |
