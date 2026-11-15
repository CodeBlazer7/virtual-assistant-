import datetime
import os
import platform
import random
import shutil
import sys
import urllib.parse
import webbrowser

import speak
import weather
from chess_game import launch_chess


def _speak_and_return(message):
    speak.speak(message)
    return message


def _system_specs():
    memory = "RAM unavailable"
    if hasattr(shutil, "get_terminal_size"):
        try:
            import ctypes

            class MemoryStatus(ctypes.Structure):
                _fields_ = [("length", ctypes.c_ulong), ("memory_load", ctypes.c_ulong),
                            ("total", ctypes.c_ulonglong), ("available", ctypes.c_ulonglong),
                            ("total_page", ctypes.c_ulonglong), ("available_page", ctypes.c_ulonglong),
                            ("total_virtual", ctypes.c_ulonglong), ("available_virtual", ctypes.c_ulonglong),
                            ("available_extended", ctypes.c_ulonglong)]

            status = MemoryStatus()
            status.length = ctypes.sizeof(MemoryStatus)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))
            memory = f"{status.total / (1024 ** 3):.1f} GB RAM"
        except (AttributeError, OSError):
            memory = "RAM unavailable"
    return f"OS: {platform.platform()} | CPU: {platform.processor() or 'unknown'} | {memory}"


def _open_youtube_search(query):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)
    webbrowser.open(url)
    return url


def _open_google_search(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    webbrowser.open(url)
    return url


def _random_reply(replies):
    return _speak_and_return(random.choice(replies))


JOKES = [
    "Why did the computer go to the doctor? It had a byte of a fever.",
    "I tried to tell a UDP joke, but I am not sure you got it.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
]

ANIME_RECOMMENDATIONS = [
    "Try Jujutsu Kaisen for supernatural battles and excellent chaos.",
    "Try Erased for a gripping mystery with time travel and heart.",
    "Try Fullmetal Alchemist Brotherhood for adventure, emotion, and a perfect story arc.",
    "Try Attack on Titan if you want mystery, strategy, and extremely high stakes.",
    "Try Spy x Family for wholesome espionage and a suspiciously powerful family.",
]


STUDY_REPLIES = [
    "That is okay. The textbook will wait patiently while your procrastination achieves its final form.",
    "I support your break. Please make it a short break, not a three-season anime commitment.",
    "You do not want to study? Even your notes are asking for character development.",
]


SILLY_REPLIES = [
    "I would do your homework, but then we would both have to explain my handwriting.",
    "That command has been forwarded to the Department of Technically Possible but Emotionally Questionable.",
    "I ran the calculation. The answer is 42, plus a small service fee for dramatic effect.",
]




def Action(send, parent=None):
    data_btn = (send or "").lower().strip()

    if "what is your name" in data_btn:
        return _speak_and_return("my name is Hershey")
    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn:
        return _speak_and_return("Hey sir, How can I help you?")
    elif "how are you" in data_btn:
        return _speak_and_return("I am doing great these days sir")
    elif "who is the principal" in data_btn and "himalaya" in data_btn:
        return _speak_and_return("The principal of Himalaya Public School is Aruna Sivaraj.")
    elif "who is the head boy" in data_btn or "head boy of the school" in data_btn:
        return _speak_and_return("The head boy of Himalaya Public School is Himank Gupta.")
    elif "information about himalaya" in data_btn or "himalaya public school" in data_btn or "himalaya school" in data_btn:
        _open_google_search("Himalaya Public Senior Secondary School Sector 7 Rohini Delhi")
        return _speak_and_return("Himalaya Public Senior Secondary School is in Sector 7, Rohini, Delhi. I opened Google for the latest public school information.")
    elif "tell me a joke" in data_btn or "make me laugh" in data_btn or data_btn == "joke":
        return _random_reply(JOKES)
    elif "recommend an anime" in data_btn or "suggest an anime" in data_btn or data_btn in ("anime", "anime recommendation"):
        return _random_reply(ANIME_RECOMMENDATIONS)
    elif "don't want to study" in data_btn or "do not want to study" in data_btn or "i hate studying" in data_btn:
        return _random_reply(STUDY_REPLIES)
    elif "do my homework" in data_btn or "are you stupid" in data_btn or "what is 2 plus 2" in data_btn:
        return _random_reply(SILLY_REPLIES)
    elif "play chess with me" in data_btn or data_btn == "chess":
        launch_chess(parent)
        return _speak_and_return("Chess is ready. You play White, and I will play Black.")
    elif "play a movie" in data_btn or "play baahubali" in data_btn or "baahubali movie" in data_btn:
        _open_youtube_search("Baahubali full movie Hindi official")
        return _speak_and_return("I found Baahubali on YouTube. Enjoy the epic battle.")
    elif "flip a coin" in data_btn or data_btn == "coin toss":
        return _speak_and_return(f"The coin says {random.choice(['heads', 'tails'])}.")
    elif "rock paper scissors" in data_btn:
        return _speak_and_return(f"I choose {random.choice(['rock', 'paper', 'scissors'])}. Your move!")
    elif "surprise me" in data_btn:
        return _random_reply(JOKES + ANIME_RECOMMENDATIONS)
    elif "thanku" in data_btn or "thank" in data_btn:
        return _speak_and_return("It is my pleasure to stay with you")
    elif "good morning" in data_btn:
        return _speak_and_return("Good morning sir, I think you might need some help")
    elif "time now" in data_btn or "what is the time" in data_btn:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return _speak_and_return(f"The time is {current_time}")
    elif "what's the date" in data_btn or "what is the date" in data_btn or "today's date" in data_btn:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return _speak_and_return(f"Today is {today}")
    elif "open task manager" in data_btn:
        os.system("start taskmgr")
        return _speak_and_return("Task Manager is open")
    elif "show system specs" in data_btn or "system specs" in data_btn:
        return _speak_and_return(_system_specs())
    elif "roll a die" in data_btn or "roll the die" in data_btn:
        return _speak_and_return(f"You rolled a {random.randint(1, 6)}")
    elif "find sql tutorial videos" in data_btn or "sql tutorial videos" in data_btn:
        _open_youtube_search("SQL tutorial for beginners introduction to SQL queries")
        return _speak_and_return("I found SQL tutorial videos on YouTube")
    elif "human knowledge" in data_btn and "sophia isla" in data_btn:
        _open_youtube_search("Human Knowledge Sophia Isla")
        return _speak_and_return("Playing Human Knowledge by Sophia Isla")
    elif "shutdown" in data_btn or "quit" in data_btn or "go offline" in data_btn:
        speak.speak("ok sir")
        raise SystemExit

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        return _speak_and_return("gaana.com is now ready for you, enjoy your music")


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        return _speak_and_return("Google open")

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        return _speak_and_return("YouTube open")
    
    elif "weather" in data_btn:
        ans = weather.Weather()
        return _speak_and_return(ans)

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        return _speak_and_return("songs playing...")

    else :
        return _speak_and_return("I am unable to understand that")

