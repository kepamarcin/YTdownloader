#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Okno "O aplikacji" z informacjami o programie
"""

import customtkinter as ctk
import webbrowser


class AboutWindow(ctk.CTkToplevel):
    """
    Okno dialogowe z informacjami o aplikacji
    """

    def __init__(self, parent):
        super().__init__(parent)

        # Konfiguracja okna
        self.title("O aplikacji")
        self.geometry("600x700")
        self.resizable(False, False)

        # Ustaw okno na wierzchu
        self.transient(parent)
        self.grab_set()

        # Wyśrodkuj okno
        self.center_window()

        # Utwórz zawartość
        self.create_widgets()

    def center_window(self):
        """
        Wyśrodkowuje okno na ekranie
        """
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        """
        Tworzy widgety okna
        """
        # Główny kontener
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # === NAGŁÓWEK ===
        header_frame = ctk.CTkFrame(main_frame, fg_color="gray25", corner_radius=10)
        header_frame.pack(fill="x", pady=(0, 20))

        icon_label = ctk.CTkLabel(
            header_frame,
            text="🎬",
            font=("Arial", 60)
        )
        icon_label.pack(pady=(20, 10))

        title_label = ctk.CTkLabel(
            header_frame,
            text="Media Downloader",
            font=("Arial", 28, "bold")
        )
        title_label.pack()

        version_label = ctk.CTkLabel(
            header_frame,
            text="Wersja 1.0.0",
            font=("Arial", 14),
            text_color="gray"
        )
        version_label.pack(pady=(5, 20))

        # === OPIS ===
        description_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        description_frame.pack(fill="x", pady=(0, 20))

        desc_title = ctk.CTkLabel(
            description_frame,
            text="📝 Opis aplikacji",
            font=("Arial", 16, "bold"),
            anchor="w"
        )
        desc_title.pack(fill="x", pady=(0, 10))

        desc_text = ctk.CTkTextbox(
            description_frame,
            height=100,
            font=("Arial", 12),
            wrap="word"
        )
        desc_text.pack(fill="x")
        desc_text.insert("1.0",
            "Media Downloader to aplikacja do pobierania wideo i audio z platform "
            "streamingowych takich jak YouTube, Vimeo i wiele innych. \n\n"
            "Aplikacja pozwala na wybór jakości wideo, pobieranie samego audio w formacie MP3, "
            "oraz pobieranie wielu plików jednocześnie."
        )
        desc_text.configure(state="disabled")

        # === INFORMACJE O TWÓRCY ===
        creator_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        creator_frame.pack(fill="x", pady=(0, 20))

        creator_title = ctk.CTkLabel(
            creator_frame,
            text="👤 Informacje o twórcy",
            font=("Arial", 16, "bold"),
            anchor="w"
        )
        creator_title.pack(fill="x", pady=(0, 10))

        # Email
        email_frame = ctk.CTkFrame(creator_frame, fg_color="gray25", corner_radius=8)
        email_frame.pack(fill="x", pady=(0, 10))

        email_label = ctk.CTkLabel(
            email_frame,
            text="✉️ Email: email@example.com",
            font=("Arial", 12),
            anchor="w"
        )
        email_label.pack(padx=15, pady=10, fill="x")

        # GitHub
        github_frame = ctk.CTkFrame(creator_frame, fg_color="gray25", corner_radius=8)
        github_frame.pack(fill="x")

        github_button = ctk.CTkButton(
            github_frame,
            text="🔗 GitHub: github.com/username",
            font=("Arial", 12),
            anchor="w",
            fg_color="transparent",
            hover_color="gray30",
            command=lambda: webbrowser.open("https://github.com/username")
        )
        github_button.pack(padx=10, pady=10, fill="x")

        # === INSTRUKCJA URUCHOMIENIA ===
        instructions_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        instructions_frame.pack(fill="both", expand=True)

        instr_title = ctk.CTkLabel(
            instructions_frame,
            text="🚀 Instrukcja uruchomienia",
            font=("Arial", 16, "bold"),
            anchor="w"
        )
        instr_title.pack(fill="x", pady=(0, 10))

        instr_text = ctk.CTkTextbox(
            instructions_frame,
            font=("Courier", 11),
            wrap="word"
        )
        instr_text.pack(fill="both", expand=True)
        instr_text.insert("1.0",
            "1. Wklej linki do pobrania w pole tekstowe (każdy link w nowej linii)\n\n"
            "2. Wybierz jakość wideo lub zaznacz 'Tylko audio' dla plików MP3\n\n"
            "3. Wybierz katalog docelowy, w którym zostaną zapisane pliki\n\n"
            "4. Kliknij 'Pobierz' i poczekaj na zakończenie\n\n"
            "5. Pliki zostaną zapisane w wybranym katalogu\n\n"
            "📌 Obsługiwane platformy:\n"
            "   • YouTube\n"
            "   • Vimeo\n"
            "   • DailyMotion\n"
            "   • i wiele innych (ponad 1000+ stron)\n\n"
            "⚠️ Uwaga: Do konwersji audio wymagany jest FFmpeg (wbudowany w aplikację)"
        )
        instr_text.configure(state="disabled")

        # === PRZYCISK ZAMKNIJ ===
        close_button = ctk.CTkButton(
            self,
            text="Zamknij",
            font=("Arial", 14, "bold"),
            height=40,
            command=self.destroy
        )
        close_button.pack(side="bottom", pady=(0, 20), padx=30, fill="x")
