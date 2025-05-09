# Realtime-Automation-SRT
A real-time voice assistant inspired by J.A.R.V.I.S., activated by custom wake words and trigger phrases. Controls system apps, answers casual questions, performs basic math, and more — all through your voice.
Great! Since you're uploading your real-time voice assistant project to GitHub, your `README.md` should clearly explain what the project does, how to use it, and what its key features are.

Here’s a well-structured `README.md` template for your project:

---

# Real-Time Voice Assistant (Friday)

A Python-based real-time voice assistant inspired by Tony Stark's J.A.R.V.I.S. system. This assistant listens for a custom wake-up command and responds to voice instructions to open/close apps, perform basic calculations, translate speech, and answer casual questions — all in real time using speech recognition and text-to-speech technology.

##  Features

*  **Voice Activated Wake Command**: Starts only when you say “Wake up buddy, welcome to daddy home”.
*  **Trigger Phrase Control**: After wake-up, uses "Friday" as the trigger word for commands (e.g., “Friday, open Chrome”).
*  **Casual Question Answering**: Responds to simple questions like “How are you?” or “Tell me a joke”.
*  **Basic Math Calculations**: Understands and solves math expressions like “What is 2 plus 2?”
*  **Speech Transcription & Translation**: Repeats what you said and can translate it to other languages.
*  **App Control**: Opens and closes system apps like Chrome or Notepad.
*  **Silent Execution**: Closes applications without showing process termination output.
*  **Female Voice (Zira)**: Uses Zira, a female voice, for all speech output (on supported systems).

##  Requirements

* Python 3.x
* Libraries:

  * `speechrecognition`
  * `pyttsx3`
  * `pyaudio`
  * `os`, `subprocess` (standard)
  * `googletrans` (optional, for translation)

Install required libraries:

```bash
pip install -r requirements.txt
```

*If you're using `googletrans` and run into issues, try using `googletrans==4.0.0-rc1`.*

##  How to Run

```bash
python app.py
```

Start by saying:

```
Wake up buddy, welcome to daddy home
```

Then use commands like:

```
Friday, open Chrome
Friday, close Notepad
Friday, what's your name?
Friday, what is 10 divided by 2?
```

## File Structure

```
Realtime-SRT-sys
 ┣ app.py
 ┣ README.md
 ┗ requirements.txt
```

## Future Improvements

* GUI interface for manual control
* Support for more system applications
* Integration with external APIs (weather, news, etc.)

 About Me
Name: R.hariharan
Project Title: Real time SRT system(or) support automation
GitHub: @hari_w8
Email: hari172003c@gmail.com
