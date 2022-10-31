from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import moviepy.editor as mp
import os
from pydub import AudioSegment

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        recognizer = sr.Recognizer()

        if file:
            if "mp4" in file.filename:
                clip = mp.VideoFileClip(r"slutter.mp4")
                clip.audio.write_audiofile(r"convt.wav")
                audio = sr.AudioFile("convt.wav")
                with audio as source:
                    audio_file = recognizer.record(source)
                transcript = recognizer.recognize_google(audio_file)
            return render_template('index.html', transcript=transcript)
        if file:

            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source, duration=10)
            transcript = recognizer.recognize_google(data)

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
