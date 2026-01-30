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
                'player_client': ['android', 'web'],  # Klienty do pobierania
                'skip': ['dash', 'hls'],  # Pomijaj problematyczne formaty
            }
        },
        
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
        ydl_opts['ffmpeg_location'] = os.path.dirname(ffmpeg_path)
    
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

def main():
    print("=" * 50)
    print("       YOUTUBE VIDEO DOWNLOADER")
    print("         (yt-dlp + ffmpeg)")
    print("=" * 50)
    
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