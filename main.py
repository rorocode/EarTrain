# This is a sample Python script.
import random
import warnings
warnings.filterwarnings("ignore")
from pydub import AudioSegment
from pydub.playback import play
import tkinter as tk
diatonic = [1,3,5,6,8,10,12,13,15,17,18,20,22,24,25]
chromatic = [2,4,7,9,11,14,16,19,21,23]
solfege = ["ti","do","ra","re","me","mi","fa","fi","so","le","la","te","ti","do","ra","re","me","mi","fa","fi","so","le","la","te","ti","do"]
chord = []
numPref = 2
chromPref = 0
answer=""
def generate():
    global answer
    answer = ""
    dia=numPref-chromPref
    chrom=chromPref
    diaNotes=random.sample(diatonic, dia)
    chromNotes=random.sample(chromatic, chrom)
    chord = diaNotes + chromNotes
    chord.sort()
    global mix
    global key
    keyModifier = random.randint(0,11)
    for note in chord:
        answer+=solfege[note]+";"

    mix = AudioSegment.from_file("assets/notes/"+str(chord[0]+keyModifier)+".wav")
    chord.pop(0)
    for note in chord:
        file = AudioSegment.from_file("assets/notes/"+str(note+keyModifier)+".wav")
        key = AudioSegment.from_file("assets/keys/"+str(1+keyModifier)+".wav")
        mix = mix.overlay(file)
def playKey():
    play(key)
def playMix():
    play(mix)


window = tk.Tk()
generateButton = tk.Button(window,text="new",command=generate)
keyButton = tk.Button(window,text="key",command = playKey)
chordButton = tk.Button(window,text="chord",command = playMix)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    generateButton.pack()
    keyButton.pack()
    chordButton.pack()
    generate()
    window.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
