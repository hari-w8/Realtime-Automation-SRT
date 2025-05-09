import speech_recognition as sr
import pyttsx3
import os
import subprocess  # Import subprocess module for silent process termination

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Friday: {text}")  # Print the response to the console
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm listening, sir.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

def execute_command(command):
    # Opening Applications
    if "open chrome" in command:
        speak("Opening Google Chrome.")
        os.system("start chrome")
    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("start notepad")

    # Closing Applications Silently (No success message printed)
    elif "close chrome" in command:
        speak("Closing Chrome.")
        subprocess.run(["taskkill", "/f", "/im", "chrome.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif "close notepad" in command:
        speak("Closing Notepad.")
        subprocess.run(["taskkill", "/f", "/im", "notepad.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # System shutdown
    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")

    # Exit program
    elif "exit" in command or "quit" in command:
        speak("Goodbye, sir.")
        exit()

    # Respond to casual questions
    elif "what's up" in command or "how are you" in command:
        speak("I'm doing great, thank you for asking! How can I assist you today?")
    
    elif "what would you do for me" in command:
        speak("I can help you with opening applications, closing them, answering questions, and even shutting down your system!")

    # New Casual Questions and Answers
    elif "what's your name" in command:
        speak("I am your personal assistant, created to make your tasks easier.")

    elif "tell me a joke" in command:
        speak("Why don't scientists trust atoms? Because they make up everything!")

    elif "which colour do you like" in command:
        speak("I don't have a favorite color, but I think blue is a nice color for an assistant.")

    elif "how old are you" in command:
        speak("I'm timeless. I was created to assist you whenever you need.")

    elif "can you help me with coding" in command:
        speak("Of course! I can help you with coding, debugging, and even providing examples.")

    else:
        speak("Command not recognized.")

if __name__ == "__main__":
    while True:
        command = listen_command()
        if command:
            execute_command(command)
