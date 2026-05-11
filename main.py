#!/usr/bin/env python3
import os
import sys
import shutil
import platform
import subprocess
import yt_dlp

def print_ffmpeg_install_hint():
    """Wyświetla instrukcję instalacji ffmpeg dla aktualnego systemu."""
    system = platform.system().lower()
    print("\nffmpeg nie jest zainstalowany w systemie ani dostępny w katalogu 'ffmpeg/'.")
    print("Proponowana instalacja dla Twojego systemu:")
    if system == 'windows':
        print("  - winget install --id=Gyan.FFmpeg -e")
        print("  - lub Chocolatey: choco install ffmpeg")
        print("  - lub pobierz ręcznie: https://www.gyan.dev/ffmpeg/builds/")
        print("    i umieść plik 'ffmpeg.exe' w katalogu 'ffmpeg/' obok main.py")
    elif system == 'darwin':
        print("  - brew install ffmpeg")
        print("  - lub MacPorts: sudo port install ffmpeg")
    elif system == 'linux':
        print("  - Debian/Ubuntu: sudo apt update && sudo apt install ffmpeg")
        print("  - Fedora:        sudo dnf install ffmpeg")
        print("  - Arch:          sudo pacman -S ffmpeg")
    else:
        print(f"  - Nieznany system ({system}). Zobacz: https://ffmpeg.org/download.html")

def get_ffmpeg_path():
    """Zwraca ścieżkę do ffmpeg: najpierw z PATH, potem z katalogu projektu."""
    system_ffmpeg = shutil.which('ffmpeg')
    if system_ffmpeg:
        return system_ffmpeg

    base_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_dir = os.path.join(base_dir, 'ffmpeg')

    if platform.system().lower() == 'windows':
        local_ffmpeg = os.path.join(ffmpeg_dir, 'ffmpeg.exe')
    else:
        local_ffmpeg = os.path.join(ffmpeg_dir, 'ffmpeg')

    if os.path.exists(local_ffmpeg):
        return local_ffmpeg

    print_ffmpeg_install_hint()
    return None

def get_downloads_path():
    """Zwraca ścieżkę do katalogu downloads."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    downloads_dir = os.path.join(base_dir, 'downloads')

    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
        print(f"Utworzono katalog: {downloads_dir}")

    return downloads_dir

def get_bgutil_script_path():
    """Zwraca ścieżkę do generate_once.js w katalogu projektu lub None."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(
        base_dir, 'bgutil-ytdlp-pot-provider', 'server', 'build', 'generate_once.js'
    )
    return script_path if os.path.exists(script_path) else None

def download_video(url):
    """Pobiera wideo z YouTube."""
    ffmpeg_path = get_ffmpeg_path()
    downloads_path = get_downloads_path()
    
    ydl_opts = {
        # Format specyficzny dla YouTube - najlepsza jakość
        'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/bestvideo[ext=webm][height<=1080]+bestaudio[ext=webm]/best[height<=1080]/best',
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
        
        # Ustawienia specyficzne dla YouTube
        'extractor_args': {
            'youtube': {
                'player_client': ['web', 'mweb'],  # Klienty z obsługą PO tokenów
            }
        },

        # JavaScript runtime do rozwiązywania n-challenge YouTube
        'js_runtimes': {'node': {}},
        
        # Opcje YouTube
        'writesubtitles': False,
        'writeautomaticsub': False,
        'subtitleslangs': ['pl', 'en'],
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        
        # Opcje ogólne
        'ignoreerrors': False,
        'no_warnings': False,
        'quiet': False,
        'no_color': False,
        'geo_bypass': True,
        'nocheckcertificate': True,
        
        # Retry i timeout
        'retries': 10,
        'fragment_retries': 10,
        'socket_timeout': 30,
        
        # Ograniczenie prędkości (opcjonalne - odkomentuj jeśli potrzebne)
        # 'ratelimit': 5000000,  # 5MB/s
    }
    
    if ffmpeg_path:
        ydl_opts['ffmpeg_location'] = ffmpeg_path

    bgutil_script = get_bgutil_script_path()
    if bgutil_script:
        ydl_opts['extractor_args']['youtubepot-bgutilscript'] = {
            'script_path': [bgutil_script]
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nPobieram informacje o wideo z YouTube...")
            info = ydl.extract_info(url, download=False)
            
            print(f"\n{'='*50}")
            print(f"Tytuł: {info.get('title', 'Nieznany')}")
            print(f"Kanał: {info.get('channel', info.get('uploader', 'Nieznany'))}")
            print(f"Czas trwania: {info.get('duration', 0)} sekund")
            print(f"Wyświetlenia: {info.get('view_count', 'N/A')}")
            print(f"{'='*50}")
            
            print(f"\nRozpoczynam pobieranie...\n")
            ydl.download([url])
            print(f"\n✓ Pobieranie zakończone!")
            print(f"Plik zapisano w: {downloads_path}")
    except yt_dlp.utils.DownloadError as e:
        print(f"\n✗ Błąd pobierania z YouTube: {e}")
    except Exception as e:
        print(f"\n✗ Nieoczekiwany błąd: {e}")

def progress_hook(d):
    """Wyświetla postęp pobierania."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rPostęp: {percent} | Prędkość: {speed} | ETA: {eta}    ", end='', flush=True)
    elif d['status'] == 'finished':
        print(f"\nPobieranie pliku zakończone, przetwarzanie...")

def validate_youtube_url(url):
    """Sprawdza czy URL jest prawidłowym linkiem YouTube."""
    youtube_patterns = [
        'youtube.com/watch',
        'youtu.be/',
        'youtube.com/shorts/',
        'youtube.com/live/',
        'youtube.com/playlist',
    ]
    return any(pattern in url for pattern in youtube_patterns)

def check_pot_provider():
    """Sprawdza czy plugin PO Token jest zainstalowany."""
    try:
        import yt_dlp_plugins.extractor.getpot_bgutil
        return True
    except ImportError:
        return False

def print_node_install_hint():
    """Wyświetla instrukcję instalacji Node.js dla aktualnego systemu."""
    system = platform.system().lower()
    print("  Proponowana instalacja Node.js:")
    if system == 'windows':
        print("    - winget install OpenJS.NodeJS.LTS")
        print("    - lub pobierz: https://nodejs.org/")
    elif system == 'darwin':
        print("    - brew install node")
        print("    - lub pobierz: https://nodejs.org/")
    elif system == 'linux':
        print("    - Debian/Ubuntu: sudo apt update && sudo apt install nodejs")
        print("    - Fedora:        sudo dnf install nodejs")
        print("    - Arch:          sudo pacman -S nodejs")
    else:
        print(f"    - {system}: https://nodejs.org/")

def verify_bgutil():
    """Sprawdza czy bgutil-ytdlp-pot-provider faktycznie działa."""
    print("\n--- Sprawdzanie bgutil-ytdlp-pot-provider ---")

    if not check_pot_provider():
        print("[X] Plugin Pythona (bgutil-ytdlp-pot-provider) nie jest zainstalowany.")
        print("    Instalacja: pip install bgutil-ytdlp-pot-provider")
        print("    Szczegóły:  https://github.com/yt-dlp/yt-dlp/wiki/PO-Token-Guide")
        print("    Bez PO tokenów YouTube może ograniczyć jakość do 360p.")
        return False
    print("[OK] Plugin Pythona zainstalowany.")

    node_path = shutil.which('node')
    if not node_path:
        print("[X] Brak Node.js w PATH — bgutil go wymaga.")
        print_node_install_hint()
        return False
    print(f"[OK] Node.js znaleziony: {node_path}")

    script_path = get_bgutil_script_path()
    if not script_path:
        print("[X] Brak skryptu generate_once.js w katalogu projektu.")
        print("    Sklonuj i zbuduj w ./bgutil-ytdlp-pot-provider/:")
        print("      git clone https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git")
        print("      cd bgutil-ytdlp-pot-provider/server")
        print("      yarn install --frozen-lockfile && npx tsc")
        return False
    print(f"[OK] Skrypt znaleziony: {script_path}")

    print("[..] Smoke test (uruchamiam generate_once.js, max 20s)...")
    try:
        result = subprocess.run(
            [node_path, script_path],
            capture_output=True, text=True, timeout=20,
        )
    except subprocess.TimeoutExpired:
        print("[X] Timeout — generate_once.js nie odpowiedział w 20s.")
        print("    Sprawdź połączenie sieciowe lub przebuduj projekt (npx tsc).")
        return False
    except Exception as e:
        print(f"[X] Błąd uruchomienia node: {e}")
        return False

    out = (result.stdout or '') + (result.stderr or '')
    if result.returncode == 0 and 'poToken' in out:
        print("[OK] bgutil działa — PO Token wygenerowany pomyślnie.")
        return True

    print(f"[X] generate_once.js zwrócił kod {result.returncode} bez PO tokenu.")
    if result.stderr:
        print(f"    stderr: {result.stderr.strip()[:300]}")
    print("    Możliwe rozwiązania:")
    print("    - przebuduj projekt: cd bgutil-ytdlp-pot-provider/server && npx tsc")
    print("    - upewnij się, że zależności są zainstalowane: yarn install --frozen-lockfile")
    print("    - zaktualizuj Node.js do wersji LTS")
    return False

def main():
    print("=" * 50)
    print("       YOUTUBE VIDEO DOWNLOADER")
    print("         (yt-dlp + ffmpeg)")
    print("=" * 50)

    verify_bgutil()
    
    while True:
        print("\nWpisz 'q' aby wyjść")
        url = input("\nPodaj URL YouTube: ").strip()
        
        if url.lower() == 'q':
            print("Do widzenia!")
            break
        
        if not url:
            print("Nie podano URL. Spróbuj ponownie.")
            continue
        
        if not url.startswith(('http://', 'https://')):
            print("Nieprawidłowy URL. Upewnij się, że zaczyna się od http:// lub https://")
            continue
        
        if not validate_youtube_url(url):
            print("To nie wygląda na link YouTube. Obsługiwane formaty:")
            print("  - https://www.youtube.com/watch?v=XXXXX")
            print("  - https://youtu.be/XXXXX")
            print("  - https://youtube.com/shorts/XXXXX")
            continue
        
        download_video(url)

if __name__ == "__main__":
    main()