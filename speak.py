import threading

import pyttsx3


_speech_lock = threading.Lock()


def _speak_worker(text):
    try:
        with _speech_lock:
            engine = pyttsx3.init()
            rate = engine.getProperty("rate")
            engine.setProperty("rate", rate - 70)
            engine.say(str(text))
            engine.runAndWait()
            engine.stop()
    except Exception:
        pass


def speak(text):
    threading.Thread(target=_speak_worker, args=(text,), daemon=True).start()

