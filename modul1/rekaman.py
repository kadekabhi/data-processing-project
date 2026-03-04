import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.AudioFile('rekaman.wav') as source:
        print("mendengarkan file audio...")
        audio_data = r.record(source)

        text = r.recognize_google(audio_data, language="id-ID")
        print("Transkripsi berhasil:")
        print(text)

except sr.UnknownValueError:
    print("Maaf, google speech recognition tidak dapat memahami audio.")
except sr.RequestError as e:
    print(f"Permintaan ke google speech recognition gagal; {e}")
except FileNotFoundError:
    print("File 'rekaman.wav' tidak ditemukan. Pastikan file ada di direktorat yang benar.")