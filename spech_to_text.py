import speech_recognition as sr 
import speak


def spech_to_text():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        return recognizer.recognize_google(audio)
    except (OSError, sr.WaitTimeoutError):
        speak.speak("I could not access the microphone")
        return None
    except sr.UnknownValueError:
        speak.speak("Sorry, I could not understand")
        return None
    except sr.RequestError:
        speak.speak("Speech recognition needs an internet connection")
        return None



