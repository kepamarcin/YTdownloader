#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moduł odpowiedzialny za pobieranie multimediów
Wykorzystuje yt-dlp do pobierania wideo i audio
"""

import yt_dlp
import os
from pathlib import Path


class MediaDownloader:
    """
    Klasa obsługująca pobieranie multimediów z platform streamingowych
    """

    def __init__(self):
        """
        Inicjalizuje downloader
        """
        pass

    def get_quality_format(self, quality):
        """
        Konwertuje wybraną jakość na format yt-dlp

        Args:
            quality (str): Wybrana jakość (Najlepsza, 1080p, 720p, 480p, 360p)

        Returns:
            str: Format string dla yt-dlp
        """
        quality_map = {
            "Najlepsza": "bestvideo+bestaudio/best",
            "1080p": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "720p": "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "480p": "bestvideo[height<=480]+bestaudio/best[height<=480]",
            "360p": "bestvideo[height<=360]+bestaudio/best[height<=360]"
        }
        return quality_map.get(quality, "bestvideo+bestaudio/best")

    def download(self, url, output_path, quality="Najlepsza", audio_only=False, progress_hook=None):
        """
        Pobiera multimedia z podanego URL

        Args:
            url (str): URL do pobrania
            output_path (str): Ścieżka do zapisu pliku
            quality (str): Jakość wideo
            audio_only (bool): Czy pobierać tylko audio
            progress_hook (callable): Funkcja callback dla postępu

        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Utwórz katalog jeśli nie istnieje
            Path(output_path).mkdir(parents=True, exist_ok=True)

            # Podstawowa konfiguracja yt-dlp
            ydl_opts = {
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
                'progress_hooks': [progress_hook] if progress_hook else [],
            }

            if audio_only:
                # Opcje dla audio
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })
            else:
                # Opcje dla wideo
                video_format = self.get_quality_format(quality)
                ydl_opts.update({
                    'format': video_format,
                    'merge_output_format': 'mp4',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',
                    }],
                })

            # Pobierz plik
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

                # Jeśli to audio, zmień rozszerzenie na mp3
                if audio_only:
                    filename = os.path.splitext(filename)[0] + '.mp3'

                return True, f"Pobrano: {os.path.basename(filename)}"

        except yt_dlp.utils.DownloadError as e:
            return False, f"Błąd pobierania: {str(e)}"
        except Exception as e:
            return False, f"Nieoczekiwany błąd: {str(e)}"

    def get_video_info(self, url):
        """
        Pobiera informacje o wideo bez pobierania

        Args:
            url (str): URL wideo

        Returns:
            dict: Informacje o wideo lub None w przypadku błędu
        """
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown'),
                    'formats': len(info.get('formats', [])),
                }
        except Exception as e:
            return None
