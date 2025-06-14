#Instalar: pip install yt-dlp

import yt_dlp
import os

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

def download_video(url):
    desktop_path = get_desktop_path()
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': f'{desktop_path}/video/%(title)s.%(ext)s',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Vídeo salvo na pasta: {os.path.join(desktop_path, 'video')}")

def download_audio(url):
    desktop_path = get_desktop_path()
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{desktop_path}/audio/%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [],  # sem conversão
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Áudio salvo na pasta: {os.path.join(desktop_path, 'audio')}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_video(url)
    download_audio(url)


