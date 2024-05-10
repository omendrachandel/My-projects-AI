import tkinter as tk
import pyttsx3

def convert_text_to_speech():
    text = entry.get()
    engine = pyttsx3.init()

  
    if selected_voice.get() == "Female":
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    else:
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

    speed = speed_slider.get() 
    engine.setProperty('rate', speed)

    engine.say(text)
    engine.runAndWait()


root = tk.Tk()
root.title("TextSpeech AI")


entry = tk.Entry(root, width=50)
entry.pack(pady=10)


selected_voice = tk.StringVar(value="Male")
male_voice_radio = tk.Radiobutton(root, text="Male", variable=selected_voice, value="Male")
male_voice_radio.pack(pady=5)
female_voice_radio = tk.Radiobutton(root, text="Female", variable=selected_voice, value="Female")
female_voice_radio.pack(pady=5)


speed_slider = tk.Scale(root, from_=50, to=300, orient=tk.HORIZONTAL, label="Speed", length=150)
speed_slider.set(150)  # Default speed
speed_slider.pack(pady=5)


convert_button = tk.Button(root, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack(pady=5)


exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=1)

root.mainloop()
