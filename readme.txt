================================================================================
                    YOUTUBE VIDEO DOWNLOADER - DOKUMENTACJA
================================================================================

@author: Marcin Kępa
@github: https://github.com/kepamarcin/YTdownloader

OPIS:
Aplikacja konsolowa do pobierania wideo z YouTube przy użyciu najnowszej
wersji yt-dlp i ffmpeg. Zoptymalizowana pod kątem YouTube.

--------------------------------------------------------------------------------
WYMAGANIA:
--------------------------------------------------------------------------------
- Python 3.8 lub nowszy
- ffmpeg (plik wykonywalny w katalogu ffmpeg/)

--------------------------------------------------------------------------------
INSTALACJA:
--------------------------------------------------------------------------------

1. Utwórz środowisko wirtualne:

   Windows:
   > python -m venv venv
   > Set-ExecutionPolicy Bypass -Scope Process ## w razie problemów!
   > venv\Scripts\activate

   Linux/macOS:
   $ python3 -m venv venv
   $ source venv/bin/activate

2. Zainstaluj zależności (najnowsza wersja yt-dlp):
   
   (venv) > pip install -r requirements.txt
   
   lub
   
   (venv) $ pip install -r requirements.txt

3. Aktualizacja yt-dlp do najnowszej wersji:
   
   (venv) > pip install --upgrade yt-dlp

4. Dodaj plik ffmpeg do katalogu ffmpeg/:
   
   Windows: ffmpeg/ffmpeg.exe
   Linux/macOS: ffmpeg/ffmpeg (nadaj uprawnienia: chmod +x ffmpeg/ffmpeg)

--------------------------------------------------------------------------------
URUCHOMIENIE:
--------------------------------------------------------------------------------

Windows:
> venv\Scripts\activate
> python main.py

Linux/macOS:
$ source venv/bin/activate
$ python main.py

--------------------------------------------------------------------------------
UŻYCIE:
--------------------------------------------------------------------------------

1. Uruchom aplikację
2. Wklej URL YouTube, np.:
   - https://www.youtube.com/watch?v=dQw4w9WgXcQ
   - https://youtu.be/dQw4w9WgXcQ
   - https://youtube.com/shorts/XXXXX
3. Poczekaj na pobranie (wyświetlany jest postęp)
4. Plik MP4 zostanie zapisany w katalogu downloads/
5. Wpisz 'q' aby wyjść

--------------------------------------------------------------------------------
OBSŁUGIWANE FORMATY URL:
--------------------------------------------------------------------------------
- https://www.youtube.com/watch?v=XXXXX  (standardowe wideo)
- https://youtu.be/XXXXX                  (skrócony link)
- https://youtube.com/shorts/XXXXX        (YouTube Shorts)
- https://youtube.com/live/XXXXX          (transmisje na żywo)
- https://youtube.com/playlist?list=XXXXX (playlisty)

--------------------------------------------------------------------------------
STRUKTURA KATALOGÓW:
--------------------------------------------------------------------------------

video_downloader/
├── ffmpeg/           <- Tu umieść plik ffmpeg/ffmpeg.exe
│   └── ffmpeg(.exe)
├── downloads/        <- Tu będą zapisywane pobrane filmy (MP4)
├── venv/             <- Środowisko wirtualne
├── main.py           <- Główny plik aplikacji
├── requirements.txt  <- Lista zależności
└── readme.txt        <- Ten plik

--------------------------------------------------------------------------------
KONFIGURACJA YOUTUBE W APLIKACJI:
--------------------------------------------------------------------------------
- Format: najlepsza jakość do 1080p w MP4
- Player client: android + web (lepsza kompatybilność)
- Geo bypass: włączony
- Retry: 10 prób przy błędach
- Timeout: 30 sekund

--------------------------------------------------------------------------------
ROZWIĄZYWANIE PROBLEMÓW:
--------------------------------------------------------------------------------

Problem: "Nie znaleziono ffmpeg"
Rozwiązanie: Umieść plik ffmpeg w katalogu ffmpeg/

Problem: "Sign in to confirm your age"
Rozwiązanie: Wideo ma ograniczenie wiekowe - wymaga cookies

Problem: "Video unavailable"
Rozwiązanie: Wideo może być zablokowane w Twoim regionie

Problem: Wolne pobieranie
Rozwiązanie: YouTube może ograniczać prędkość - to normalne

Problem: Stara wersja yt-dlp
Rozwiązanie: pip install --upgrade yt-dlp

================================================================================