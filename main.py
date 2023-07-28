import gtts
import playsound
text = input("Enter Input:")
sound = gtts.gTTS(text, lang='en')
sound.save("sample.mp3")
playsound.playsound('sample.mp3')

