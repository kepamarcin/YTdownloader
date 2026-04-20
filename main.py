#!/usr/bin/env python3
import os
import sys
import platform
import yt_dlp

def get_ffmpeg_path():
    """Zwraca ścieżkę do ffmpeg w zależności od systemu operacyjnego."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_dir = os.path.join(base_dir, 'ffmpeg')
    
    system = platform.system().lower()
    if system == 'windows':
        ffmpeg_path = os.path.join(ffmpeg_dir, 'ffmpeg.exe')
    else:
        ffmpeg_path = os.path.join(ffmpeg_dir, 'ffmpeg')
    
    if not os.path.exists(ffmpeg_path):
        print(f"UWAGA: Nie znaleziono ffmpeg w: {ffmpeg_path}")
        print("Upewnij się, że plik ffmpeg znajduje się w katalogu 'ffmpeg/'")
        return None
    
    return ffmpeg_path

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

def main():
    print("=" * 50)
    print("       YOUTUBE VIDEO DOWNLOADER")
    print("         (yt-dlp + ffmpeg)")
    print("=" * 50)

    if not check_pot_provider():
        print("\nUWAGA: Nie wykryto pluginu PO Token (bgutil-ytdlp-pot-provider).")
        print("Wysokie rozdzielczości mogą nie działać bez PO tokenów.")
        print("Instalacja: pip install bgutil-ytdlp-pot-provider")
        print("Szczegóły: https://github.com/yt-dlp/yt-dlp/wiki/PO-Token-Guide")
    elif not get_bgutil_script_path():
        print("\nUWAGA: Nie znaleziono skryptu bgutil (generate_once.js) w katalogu projektu.")
        print("Sklonuj i zbuduj repo w: ./bgutil-ytdlp-pot-provider/")
        print("Bez tego YouTube moze ograniczyc jakosc do 360p.")
    
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