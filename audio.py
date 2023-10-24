'''
Dependencies: gettext, playsound
installing
$ pip install gTTS pyttsx3 playsound soundfile transformers datasets sentencepiece
$ pip install playsound (may need to use "$ pip install --upgrade wheel" if install fails)
'''
import gtts
from playsound import playsound

with open("sample.ini") as fileDescriptor:
     data = fileDescriptor.read()

tts = gtts.gTTS(data)
tts.save("audioReader.mp3")
playsound("audioReader.mp3")
