YouTube Video Downloader v2

Aplikacja konsolowa do pobierania wideo z YouTube w wysokiej rozdzielczosci
(do 1080p) przy uzyciu yt-dlp, ffmpeg i systemu PO Token.
Obsluguje standardowe wideo, Shorts, transmisje na zywo oraz playlisty.

Autor: Marcin Kepa
GitHub: https://github.com/kepamarcin/YTdownloader

================================================================================

Wymagania wstepne

Zanim zaczniesz, upewnij sie, ze masz zainstalowane niezbedne narzedzia.

1. Instalacja Git

Windows:
1. Pobierz instalator ze strony https://git-scm.com/download/win
2. Uruchom instalator i postepuj zgodnie z instrukcjami (domyslne ustawienia sa
   zazwyczaj wystarczajace).
3. Po instalacji otwórz terminal (CMD lub PowerShell) i wpisz git --version,
   aby sprawdzic poprawnosc instalacji.

Linux (Debian/Ubuntu):
    sudo apt update
    sudo apt install git

macOS:
Jesli masz zainstalowane Homebrew:
    brew install git

2. Instalacja Python (3.8+)

Windows:
1. Pobierz instalator ze strony https://www.python.org/
2. Wazne: Podczas instalacji zaznacz opcje "Add Python to PATH".
3. Kliknij "Install Now".

Linux/macOS:
Python jest zazwyczaj zainstalowany domyslnie. Sprawdz wersje wpisujac:
    python3 --version

3. Instalacja Node.js (20+)

Node.js jest wymagany do rozwiazywania zabezpieczen YouTube (n-challenge
oraz generowanie PO Token). Bez niego dostepna bedzie tylko jakosc 360p.

Windows:
Pobierz instalator ze strony https://nodejs.org/ (wersja LTS).
Po instalacji sprawdz:
    node --version

Linux (Debian/Ubuntu):
    curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
    sudo apt install -y nodejs

macOS:
    brew install node

================================================================================

Pobieranie repozytorium

Otwórz terminal w folderze, w którym chcesz zapisac projekt i wykonaj polecenie:
    git clone https://github.com/kepamarcin/YTdownloader.git
    cd YTdownloader

================================================================================

Instalacja i konfiguracja

1. Utwórz srodowisko wirtualne

Windows: W terminalu. Nie bac sie, nie gryzie.
    python -m venv venv
    # Jesli wystapi blad uprawnien, wykonaj: Set-ExecutionPolicy Bypass -Scope Process
    venv\Scripts\activate

Linux/macOS:
    python3 -m venv venv
    source venv/bin/activate

2. Zainstaluj zaleznosci

Upewnij sie, ze srodowisko wirtualne jest aktywne (powinienes widziec (venv)
w terminalu), a nastepnie zainstaluj biblioteki:
    pip install -r requirements.txt

3. Skonfiguruj PO Token (wymagane do HD)

YouTube wymaga tokenów PO (Proof of Origin) do udostepniania wideo w wysokiej
rozdzielczosci. Bez tego kroku dostepna bedzie tylko jakosc 360p.

Bedac w katalogu YTdownloader/ (dziala tak samo na Windows/macOS/Linux):
    git clone --single-branch --branch 1.3.1 https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git bgutil-ytdlp-pot-provider
    cd bgutil-ytdlp-pot-provider/server
    npm ci
    npx tsc
    cd ../..

UWAGA: Repozytorium bgutil jest klonowane do podkatalogu projektu
(./bgutil-ytdlp-pot-provider). Aplikacja automatycznie wykrywa skrypt
server/build/generate_once.js w tej lokalizacji i przekazuje jego sciezke
do yt-dlp, wiec dziala przenosnie na Windows, macOS i Linux.

================================================================================

Uruchomienie

Upewnij sie, ze jestes w katalogu projektu i masz aktywne srodowisko wirtualne.

Windows:
    python main.py

Linux/macOS:
    python3 main.py

Po zakonczeniu pracy — deaktywacja venv:
    deactivate

================================================================================

Uzycie

1. Uruchom aplikacje.
2. Wklej URL YouTube, gdy zostaniesz o to poproszony.
3. Poczekaj na pobranie (postep bedzie wyswietlany w konsoli).
4. Plik MP4 zostanie zapisany w katalogu downloads/
5. Wpisz q, aby wyjsc z programu.

Obslugiwane formaty URL:
  https://www.youtube.com/watch?v=XXXX  (standardowe wideo)
  https://youtu.be/XXXX                 (skrócony link)
  https://youtube.com/shorts/XXXX       (YouTube Shorts)
  https://youtube.com/live/XXXX         (transmisje na zywo)
  https://youtube.com/playlist?list=XXXX (playlisty)

================================================================================

Struktura katalogów

YTdownloader/
├── ffmpeg/                      <- Plik ffmpeg/ffmpeg.exe (dolaczony)
│   └── ffmpeg(.exe)
├── bgutil-ytdlp-pot-provider/   <- Sklonowane repo bgutil (krok 3)
├── downloads/                   <- Pobrane filmy (MP4)
├── venv/                        <- Srodowisko wirtualne
├── main.py                      <- Glówny plik aplikacji
├── requirements.txt             <- Lista zaleznosci
└── readme.txt                   <- Dokumentacja

================================================================================

Konfiguracja wewnetrzna

Aplikacja jest domyslnie skonfigurowana dla optymalnej wydajnosci:
  Format:       Najlepsza jakosc do 1080p w MP4
  Player client: Web + mWeb (z obsluga PO tokenów)
  JS Runtime:   Node.js (do rozwiazywania n-challenge YouTube)
  PO Token:     Automatyczne generowanie przez bgutil (tryb script)
  Geo bypass:   Wlaczony
  Retry:        10 prób przy bledach sieciowych
  Timeout:      30 sekund

================================================================================

Rozwiazywanie problemów

Problem                          | Rozwiazanie
---------------------------------|---------------------------------------------
"Nie znaleziono ffmpeg"          | Upewnij sie, ze plik ffmpeg(.exe) jest w folderze ffmpeg/
"ffmpeg is not installed" (HD)   | Sprawdz czy ffmpeg.exe (Win) lub ffmpeg (Linux) jest w folderze ffmpeg/
Tylko 360p, brak HD              | Sprawdz: 1) Node.js >= 20 (node --version), 2) bgutil sklonowany
                                 | i zbudowany w ./bgutil-ytdlp-pot-provider/server/ (w katalogu projektu)
WARNING: pot:bgutil:http         | Normalne ostrzezenie — plugin przechodzi na tryb script. Ignoruj.
"n challenge solving failed"     | Zainstaluj Node.js >= 20. Zaktualizuj: pip install -U "yt-dlp[default]"
"Sign in to confirm your age"    | Wideo wymaga cookies (nieobslugiwane w tej wersji)
"Video unavailable"              | Wideo zablokowane w regionie lub usuniete
Wolne pobieranie                 | YouTube throttling — normalne zachowanie
Bledy pobierania                 | Zaktualizuj: pip install -U "yt-dlp[default]" bgutil-ytdlp-pot-provider
