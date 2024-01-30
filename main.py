import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(True, True)
root.configure(bg="#305065")

engine = pyttsx3.init()

def setvoice(selected_language, text, selected_gender, selected_speed):
    voices = engine.getProperty('voices')

    print("Available voices:")
    for voice in voices:
        print("Voice:", voice.name)

    language_keywords = {
        'english': ['microsoft david desktop', 'microsoft zira desktop'],
        'hindi': ['hindi', 'hin'],
        'bengali': ['bengali', 'bn', 'ben'],
        'telugu': ['telugu', 'te', 'tel'],
        'tamil': ['tamil', 'ta', 'tam'],
        'marathi': ['marathi', 'mr', 'mar'],
        'urdu': ['urdu', 'ur'],
        'gujarati': ['gujarati', 'gu', 'guj'],
        'kannada': ['kannada', 'kn', 'kan'],
        'malayalam': ['malayalam', 'ml', 'mal'],
        'punjabi': ['punjabi', 'pa', 'pan'],
        'odia': ['odia', 'or', 'odi'],
        'assamese': ['assamese', 'as', 'asm'],
        'kashmiri': ['kashmiri', 'ks', 'kas'],
        'konkani': ['konkani', 'knk', 'kok'],
        'nepali': ['nepali', 'ne', 'nep'],
    }

    language_voice_index = None
    for lang, keywords in language_keywords.items():
        if selected_language == lang:
            language_voice_index = next((i for i, voice in enumerate(voices) if any(keyword in voice.name.lower() for keyword in keywords)), None)
            print(f"Voice index for {lang}: {language_voice_index}")
            break

    if language_voice_index is not None:
        selected_gender = selected_gender.lower()  # Convert gender to lowercase

        if selected_gender == 'female':
            # Adjust voice index for female voice
            language_voice_index += 1

        engine.setProperty('voice', voices[language_voice_index].id)

        # Set the speed
        speed_dict = {'fast': 300, 'normal': 200, 'slow': 100}
        speed = speed_dict.get(selected_speed.lower(), 200)  # Default to normal speed if not recognized
        engine.setProperty('rate', speed)
    else:
        print(f"Voice for {selected_language} not found. Using default English voice.")
        # Set a default English voice or handle it in application
        engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

def speaknow():
    text = text_area.get(1.0, END)
    selected_language = language_combobox.get().lower()
    selected_gender = gender_combobox.get()
    selected_speed = speed_combobox.get()

    if text:
        setvoice(selected_language, text, selected_gender, selected_speed)

def download():
    text = text_area.get(1.0, END)
    selected_language = language_combobox.get().lower()
    selected_gender = gender_combobox.get()
    selected_speed = speed_combobox.get()

    if text:
        setvoice(selected_language, text, selected_gender, selected_speed)
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            filename = 'text.mp3'
            engine.save_to_file(text, filename)
            engine.runAndWait()

# Language Combobox
language_combobox = Combobox(root, values=['English', 'Hindi', 'Bengali', 'Telugu', 'Tamil', 'Marathi', 'Urdu', 'Gujarati', 'Kannada', 'Malayalam', 'Punjabi', 'Odia', 'Assamese', 'Punjabi', 'Kashmiri', 'Konkani', 'Nepali'], font="arial 14", state="r", width=10)
language_combobox.place(x=550, y=240)
language_combobox.set('English')  # Set a default language

# Text area and other UI elements
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=760, y=160)

# Other UI elements and buttons...
image_icon = PhotoImage(file="speech.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="speak1.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="white", fg="black").place(x=100, y=20)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state="r", width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state="r", width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

image_icon = PhotoImage(file="speak1.png")
btn = Button(root, text="Speak", image=image_icon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

image_icon2 = PhotoImage(file="download.png")
save = Button(root, text="Save", image=image_icon2, width=130, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=730, y=280)

root.mainloop()
