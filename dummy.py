
import speech_recognition as sr
import moviepy.editor as mp
audioFile = sr.AudioFile(r"convt.wav")
recognizer = sr.Recognizer()
with audioFile as source:
    recognizer.adjust_for_ambient_noise(source)
    data = recognizer.record(source)
result = recognizer.recognize_google(data, language="pl")
print(result)
