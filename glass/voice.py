from PIL import Image
import pytesseract
from gtts import gTTS
import vlc
import os
def image_to_audio():
    img = Image.open('read.jpg')
    text = pytesseract.image_to_string(img)
    print(text)
    text_val = text  
    language = 'en'  
    obj = gTTS(text=text_val, lang=language, slow=False)  
    obj.save("exam1.mp3")
    p=vlc.MediaPlayer("exam1.mp3")
    p.play()
image_to_audio()
input()
