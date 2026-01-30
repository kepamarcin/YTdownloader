#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Media Downloader - Aplikacja do pobierania wideo i audio z platform streamingowych
Autor: email@example.com
GitHub: github.com/username
Wersja: 1.0.0
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
import sys
from pathlib import Path
from downloader import MediaDownloader
from about_window import AboutWindow

# Ustawienia CustomTkinter
ctk.set_appearance_mode("dark")  # "dark" lub "light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


class MediaDownloaderApp(ctk.CTk):
    """
    Główna klasa aplikacji Media Downloader
    Obsługuje GUI i interakcje użytkownika
    """

    def __init__(self):
        super().__init__()

        # Konfiguracja okna głównego
        self.title("Media Downloader - Pobieraj wideo i audio")
        self.geometry("900x700")
        self.minsize(800, 600)

        # Inicjalizacja zmiennych
        self.download_path = str(Path.home() / "Downloads")
        self.downloader = MediaDownloader()
        self.is_downloading = False

        # Tworzenie GUI
        self.create_widgets()

    def create_widgets(self):
        """
        Tworzy wszystkie widgety GUI
        """
        # Główny kontener z paddingiem
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # === NAGŁÓWEK ===
        header_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))

        title_label = ctk.CTkLabel(
            header_frame,
            text="🎬 Media Downloader",
            font=("Arial", 28, "bold")
        )
        title_label.pack()

        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Pobieraj wideo i audio z YouTube i innych platform",
            font=("Arial", 12),
            text_color="gray"
        )
        subtitle_label.pack()

        # === SEKCJA LINKÓW ===
        links_frame = ctk.CTkFrame(main_container)
        links_frame.pack(fill="x", pady=(0, 15))

        links_label = ctk.CTkLabel(
            links_frame,
            text="📎 Linki do pobrania (każdy link w nowej linii):",
            font=("Arial", 14, "bold"),
            anchor="w"
        )
        links_label.pack(fill="x", padx=15, pady=(15, 5))

        # Pole tekstowe na linki
        self.links_textbox = ctk.CTkTextbox(
            links_frame,
            height=120,
            font=("Arial", 12),
            wrap="word"
        )
        self.links_textbox.pack(fill="x", padx=15, pady=(0, 15))

        # === OPCJE POBIERANIA ===
        options_frame = ctk.CTkFrame(main_container)
        options_frame.pack(fill="x", pady=(0, 15))

        options_label = ctk.CTkLabel(
            options_frame,
            text="⚙️ Opcje pobierania:",
            font=("Arial", 14, "bold"),
            anchor="w"
        )
        options_label.pack(fill="x", padx=15, pady=(15, 10))

        # Kontener na opcje (siatka 2x2)
        options_grid = ctk.CTkFrame(options_frame, fg_color="transparent")
        options_grid.pack(fill="x", padx=15, pady=(0, 15))

        # Jakość wideo
        quality_label = ctk.CTkLabel(
            options_grid,
            text="Jakość wideo:",
            font=("Arial", 12)
        )
        quality_label.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)

        self.quality_var = ctk.StringVar(value="Najlepsza")
        self.quality_dropdown = ctk.CTkOptionMenu(
            options_grid,
            values=["Najlepsza", "1080p", "720p", "480p", "360p"],
            variable=self.quality_var,
            width=200
        )
        self.quality_dropdown.grid(row=0, column=1, sticky="w", pady=5)

        # Checkbox tylko audio
        self.audio_only_var = ctk.BooleanVar(value=False)
        self.audio_checkbox = ctk.CTkCheckBox(
            options_grid,
            text="🎵 Tylko audio (MP3)",
            variable=self.audio_only_var,
            font=("Arial", 12),
            command=self.toggle_quality_dropdown
        )
        self.audio_checkbox.grid(row=1, column=0, columnspan=2, sticky="w", pady=5)

        # Katalog docelowy
        path_label = ctk.CTkLabel(
            options_grid,
            text="Katalog zapisu:",
            font=("Arial", 12)
        )
        path_label.grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)

        path_display_frame = ctk.CTkFrame(options_grid, fg_color="transparent")
        path_display_frame.grid(row=2, column=1, sticky="ew", pady=5)

        self.path_label = ctk.CTkLabel(
            path_display_frame,
            text=self.download_path,
            font=("Arial", 10),
            anchor="w",
            text_color="gray"
        )
        self.path_label.pack(side="left", fill="x", expand=True)

        browse_button = ctk.CTkButton(
            path_display_frame,
            text="Wybierz",
            width=80,
            command=self.browse_directory
        )
        browse_button.pack(side="right", padx=(10, 0))

        options_grid.columnconfigure(1, weight=1)

        # === PRZYCISKI AKCJI ===
        buttons_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=(0, 15))

        self.download_button = ctk.CTkButton(
            buttons_frame,
            text="⬇️ Pobierz",
            font=("Arial", 16, "bold"),
            height=50,
            command=self.start_download
        )
        self.download_button.pack(side="left", fill="x", expand=True, padx=(0, 5))

        about_button = ctk.CTkButton(
            buttons_frame,
            text="ℹ️ O aplikacji",
            font=("Arial", 14),
            height=50,
            width=150,
            fg_color="gray30",
            hover_color="gray40",
            command=self.show_about
        )
        about_button.pack(side="right", padx=(5, 0))

        # === PASEK POSTĘPU ===
        progress_frame = ctk.CTkFrame(main_container)
        progress_frame.pack(fill="x", pady=(0, 15))

        progress_label = ctk.CTkLabel(
            progress_frame,
            text="📊 Postęp pobierania:",
            font=("Arial", 14, "bold"),
            anchor="w"
        )
        progress_label.pack(fill="x", padx=15, pady=(15, 5))

        self.progress_bar = ctk.CTkProgressBar(progress_frame)
        self.progress_bar.pack(fill="x", padx=15, pady=(0, 10))
        self.progress_bar.set(0)

        self.progress_text = ctk.CTkLabel(
            progress_frame,
            text="Gotowy do pobierania",
            font=("Arial", 11),
            anchor="w"
        )
        self.progress_text.pack(fill="x", padx=15, pady=(0, 15))

        # === LOGI ===
        logs_frame = ctk.CTkFrame(main_container)
        logs_frame.pack(fill="both", expand=True)

        logs_label = ctk.CTkLabel(
            logs_frame,
            text="📝 Logi:",
            font=("Arial", 14, "bold"),
            anchor="w"
        )
        logs_label.pack(fill="x", padx=15, pady=(15, 5))

        self.logs_textbox = ctk.CTkTextbox(
            logs_frame,
            font=("Courier", 10),
            wrap="word"
        )
        self.logs_textbox.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    def toggle_quality_dropdown(self):
        """
        Włącza/wyłącza dropdown jakości wideo gdy zaznaczono "tylko audio"
        """
        if self.audio_only_var.get():
            self.quality_dropdown.configure(state="disabled")
        else:
            self.quality_dropdown.configure(state="normal")

    def browse_directory(self):
        """
        Otwiera okno dialogowe wyboru katalogu
        """
        directory = filedialog.askdirectory(initialdir=self.download_path)
        if directory:
            self.download_path = directory
            self.path_label.configure(text=self.download_path)
            self.log(f"✓ Zmieniono katalog zapisu: {self.download_path}")

    def log(self, message):
        """
        Dodaje wiadomość do logów
        """
        self.logs_textbox.insert("end", f"{message}\n")
        self.logs_textbox.see("end")

    def update_progress(self, value, text=""):
        """
        Aktualizuje pasek postępu i tekst
        """
        self.progress_bar.set(value)
        if text:
            self.progress_text.configure(text=text)

    def start_download(self):
        """
        Rozpoczyna proces pobierania w osobnym wątku
        """
        if self.is_downloading:
            messagebox.showwarning(
                "Pobieranie w toku",
                "Poczekaj na zakończenie bieżącego pobierania."
            )
            return

        # Pobierz linki
        links_text = self.links_textbox.get("1.0", "end").strip()
        if not links_text:
            messagebox.showerror(
                "Błąd",
                "Wklej przynajmniej jeden link do pobrania!"
            )
            return

        # Podziel linki
        links = [link.strip() for link in links_text.split("\n") if link.strip()]

        if not links:
            messagebox.showerror(
                "Błąd",
                "Nie znaleziono poprawnych linków!"
            )
            return

        # Pobierz opcje
        quality = self.quality_var.get()
        audio_only = self.audio_only_var.get()

        # Reset UI
        self.logs_textbox.delete("1.0", "end")
        self.update_progress(0, "Rozpoczynanie pobierania...")
        self.download_button.configure(state="disabled", text="⏳ Pobieranie...")
        self.is_downloading = True

        # Uruchom pobieranie w osobnym wątku
        thread = threading.Thread(
            target=self.download_thread,
            args=(links, quality, audio_only),
            daemon=True
        )
        thread.start()

    def download_thread(self, links, quality, audio_only):
        """
        Wątek pobierania - wykonuje faktyczne pobieranie
        """
        try:
            total_links = len(links)
            self.log(f"📥 Rozpoczynam pobieranie {total_links} plików...\n")

            for idx, link in enumerate(links, 1):
                # Aktualizuj postęp
                progress = (idx - 1) / total_links
                self.after(0, self.update_progress, progress, f"Pobieranie {idx}/{total_links}...")

                self.log(f"[{idx}/{total_links}] Pobieram: {link}")

                # Callback do aktualizacji postępu
                def progress_hook(d):
                    if d['status'] == 'downloading':
                        try:
                            percent_str = d.get('_percent_str', '0%').strip()
                            speed = d.get('_speed_str', 'N/A').strip()
                            eta = d.get('_eta_str', 'N/A').strip()

                            # Oblicz postęp wewnątrz obecnego pliku
                            file_progress = float(percent_str.replace('%', '')) / 100
                            overall_progress = ((idx - 1) + file_progress) / total_links

                            status_text = f"[{idx}/{total_links}] {percent_str} | Prędkość: {speed} | ETA: {eta}"
                            self.after(0, self.update_progress, overall_progress, status_text)
                        except:
                            pass
                    elif d['status'] == 'finished':
                        self.after(0, self.log, f"✓ Zakończono pobieranie: {d.get('filename', 'plik')}")

                # Pobierz plik
                success, message = self.downloader.download(
                    url=link,
                    output_path=self.download_path,
                    quality=quality,
                    audio_only=audio_only,
                    progress_hook=progress_hook
                )

                if success:
                    self.log(f"✓ Sukces: {message}\n")
                else:
                    self.log(f"✗ Błąd: {message}\n")

            # Zakończono wszystkie pobierania
            self.after(0, self.update_progress, 1.0, f"✓ Zakończono! Pobrano {total_links} plików.")
            self.log(f"\n🎉 Wszystkie pliki zostały pobrane!")
            self.log(f"📁 Lokalizacja: {self.download_path}")

        except Exception as e:
            self.log(f"\n❌ Błąd krytyczny: {str(e)}")
            self.after(0, self.update_progress, 0, "Błąd podczas pobierania")

        finally:
            # Resetuj stan
            self.is_downloading = False
            self.after(0, self.download_button.configure, {"state": "normal", "text": "⬇️ Pobierz"})

    def show_about(self):
        """
        Wyświetla okno "O aplikacji"
        """
        AboutWindow(self)


def main():
    """
    Funkcja główna - uruchamia aplikację
    """
    app = MediaDownloaderApp()
    app.mainloop()


if __name__ == "__main__":
    main()
