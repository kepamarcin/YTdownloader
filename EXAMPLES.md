# 📚 Przykłady użycia - Media Downloader

## 🎯 Podstawowe użycie

### 1. Pobieranie pojedynczego wideo (YouTube)

```
Link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Jakość: 1080p
Tylko audio: ☐
Katalog: C:\Users\Username\Downloads
```

**Wynik:** Plik MP4 w jakości 1080p

---

### 2. Pobieranie tylko audio (MP3)

```
Link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Jakość: (wyłączone)
Tylko audio: ☑️
Katalog: C:\Users\Username\Music
```

**Wynik:** Plik MP3 (192 kbps)

---

### 3. Pobieranie wielu wideo jednocześnie

```
Linki:
https://www.youtube.com/watch?v=video1
https://www.youtube.com/watch?v=video2
https://www.youtube.com/watch?v=video3

Jakość: 720p
Tylko audio: ☐
```

**Wynik:** 3 pliki MP4 w jakości 720p

---

## 🚀 Zaawansowane użycie

### 4. Pobieranie całej playlisty YouTube

```
Link: https://www.youtube.com/playlist?list=PLxxxxxxxxxx
Jakość: Najlepsza
```

**Wynik:** Wszystkie wideo z playlisty w najlepszej jakości

---

### 5. Pobieranie z różnych platform

```
Linki:
https://www.youtube.com/watch?v=xxxxx    (YouTube)
https://vimeo.com/123456789              (Vimeo)
https://www.dailymotion.com/video/xxxxx (DailyMotion)
https://soundcloud.com/artist/track     (SoundCloud)
```

**Wynik:** Pliki z różnych platform w jednym katalogu

---

### 6. Pobieranie wideo w niskiej jakości (oszczędność miejsca)

```
Link: https://www.youtube.com/watch?v=xxxxx
Jakość: 360p
```

**Wynik:** Mały plik MP4 (360p)

---

## 🎵 Przykłady dla muzyki

### 7. Pobieranie albumu muzycznego (SoundCloud)

```
Link: https://soundcloud.com/artist/sets/album-name
Tylko audio: ☑️
Katalog: D:\Music\Artist Name
```

**Wynik:** Wszystkie utwory z albumu w formacie MP3

---

### 8. Pobieranie koncertu live

```
Link: https://www.youtube.com/watch?v=concert
Jakość: Najlepsza
Tylko audio: ☑️
```

**Wynik:** Audio z koncertu w formacie MP3

---

## 📱 Pobieranie z social media

### 9. Instagram Video

```
Link: https://www.instagram.com/p/xxxxx/
Jakość: Najlepsza
```

**Wynik:** Wideo z Instagrama

---

### 10. TikTok Video

```
Link: https://www.tiktok.com/@user/video/xxxxx
Jakość: Najlepsza
```

**Wynik:** Wideo z TikToka (bez watermark gdy możliwe)

---

### 11. Twitter Video

```
Link: https://twitter.com/user/status/xxxxx
Jakość: Najlepsza
```

**Wynik:** Wideo z Twittera

---

## 🎓 Porady i tricki

### ✅ Dobre praktyki

1. **Organizuj pliki w folderach**
   ```
   Music\
   ├── Rock\
   ├── Pop\
   └── Classical\
   
   Videos\
   ├── Tutorials\
   ├── Entertainment\
   └── Documentaries
   ```

2. **Wybieraj odpowiednią jakość**
   - **4K/1080p**: Dla archiwizacji, duże ekrany
   - **720p**: Balans jakości i rozmiaru
   - **480p/360p**: Dla urządzeń mobilnych, oszczędność miejsca

3. **Tylko audio dla muzyki**
   - ☑️ Zaznacz "Tylko audio" dla piosenek
   - Oszczędzisz miejsce i czas pobierania
   - Format MP3 jest uniwersalny

4. **Batch downloading**
   - Kopiuj wszystkie linki do Excela/Notatnika
   - Wklej wszystkie naraz (każdy w nowej linii)
   - Pobieraj w nocy gdy internet jest szybszy

### ⚠️ Częste problemy i rozwiązania

**Problem**: "ERROR: Video unavailable"
**Rozwiązanie**: 
- Sprawdź czy wideo jest publiczne
- Spróbuj otworzyć link w przeglądarce
- Wideo może być zablokowane w Twoim kraju

---

**Problem**: "ERROR: ffmpeg not found"
**Rozwiązanie**:
```bash
# Windows
choco install ffmpeg

# macOS
brew install ffmpeg
```

---

**Problem**: Pobieranie bardzo wolne
**Rozwiązanie**:
- Wybierz niższą jakość
- Pobieraj po jednym pliku
- Sprawdź prędkość internetu

---

**Problem**: Aplikacja nie uruchamia się (macOS)
**Rozwiązanie**:
```bash
xattr -cr /Applications/MediaDownloader.app
```

---

## 🌐 Obsługiwane platformy - przykłady

### Video Streaming
- ✅ YouTube: `youtube.com/watch?v=xxxxx`
- ✅ Vimeo: `vimeo.com/123456789`
- ✅ DailyMotion: `dailymotion.com/video/xxxxx`
- ✅ Twitch (VODs): `twitch.tv/videos/123456789`

### Social Media
- ✅ Instagram: `instagram.com/p/xxxxx/`
- ✅ TikTok: `tiktok.com/@user/video/xxxxx`
- ✅ Twitter: `twitter.com/user/status/xxxxx`
- ✅ Facebook: `facebook.com/watch?v=xxxxx`
- ✅ Reddit: `reddit.com/r/subreddit/comments/xxxxx`

### Audio Platforms
- ✅ SoundCloud: `soundcloud.com/artist/track`
- ✅ Bandcamp: `artist.bandcamp.com/track/song-name`
- ✅ Mixcloud: `mixcloud.com/artist/mix-name`

### Inne
- ✅ Bilibili: `bilibili.com/video/BVxxxxx`
- ✅ VK: `vk.com/video-xxxxx`
- ✅ Naver: `tv.naver.com/v/xxxxx`

**...i 1000+ innych!**

Pełna lista: [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

---

## 💡 Pro Tips

### Tip #1: Automatyzacja z listą linków

Stwórz plik tekstowy z linkami:
```
links.txt:
https://youtube.com/watch?v=1
https://youtube.com/watch?v=2
https://youtube.com/watch?v=3
```

Kopiuj całą zawartość i wklej do aplikacji!

---

### Tip #2: Oszczędzanie miejsca

Dla podcast'ów i audiobook'ów:
- ☑️ Tylko audio
- Jakość: nie ma znaczenia (audio jest takie samo)
- Format: MP3 (mniejsze pliki niż M4A)

---

### Tip #3: Archiwizacja wideo

Dla ważnych wideo (np. edukacyjnych):
- Jakość: **Najlepsza**
- Katalog: Dysk zewnętrzny lub cloud
- Zachowaj oryginalne nazwy plików

---

### Tip #4: Prędkość pobierania

Aby przyspieszyć:
1. Zamknij inne aplikacje używające internetu
2. Połącz się Ethernetem zamiast Wi-Fi
3. Pobieraj w godzinach nocnych
4. Używaj niższej jakości (360p/480p)

---

## 📞 Potrzebujesz pomocy?

- 📧 Email: email@example.com
- 🐙 GitHub: github.com/username/media-downloader
- 📖 Dokumentacja: README.md

**Happy downloading! 🎉**
