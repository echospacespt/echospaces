from fastapi import FastAPI

from app.core.supabase import supabase

import os

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok2"}


@app.get("/health/db")
def health_db():
    try:
        result = (
            supabase
            .table("users")
            .select("*")
            .limit(1)
            .execute()
        )

        return {
            "status": "ok",
            "database": "connected"
        }

    except Exception as ex:
        return {
            "status": "error",
            "message": str(ex)
        }


@app.get("/mp3")
def get_mp3():
    # List of approximate song names
    song_names = [
    "Bohemian Rhapsody Queen",
    "Shape of You Ed Sheeran",
    "Billie Jean Michael Jackson"
    ]

    # Custom folder to save MP3s
    output_folder = "downloaded_mp3s"

    # Create the folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Download each song using yt-dlp
    for song in song_names:
        command = (
            f"yt-dlp --extract-audio --audio-format mp3 "
            f"--output \"{output_folder}/%(title)s.%(ext)s\" "
            f"\"ytsearch1:{song}\""
        )
        print(f"Running: {command}")
        os.system(command)