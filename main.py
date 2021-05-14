#import libraries
import random
import warnings
warnings.filterwarnings("ignore") #ignore ffmpeg warning
from pydub import AudioSegment
from pydub.playback import play
import tkinter as tk
from tkinter import messagebox
#solfege definitions
diatonic = [1,3,5,6,8,10,12,13,15,17,18,20,22,24,25]
chromatic = [2,4,7,9,11,14,16,19,21,23]
solfege = ["ti","do","ra","re","me","mi","fa","fi","so","le","la","te","ti","do","ra","re","me","mi","fa","fi","so","le","la","te","ti","do"]
#set up settings
numOptions = [2,3,4,5,6,7,8,9]
chromOptions = [0,1,2,3,4,5,6,7,8,9]
answer=""
#generate audio and answers
def generate():
    #reset answer
    answer = ""
    #get settings
    numPref=numPick.get()
    chromPref=chromPick.get()
    #check for invalid settings
    if chromPref>numPref:
        messagebox.showerror("Error", "You cannot have more chromatics than notes!")
        return
    #generate diatonics and chromatics
    dia=numPref-chromPref
    chrom=chromPref
    diaNotes=random.sample(diatonic, dia)
    chromNotes=random.sample(chromatic, chrom)
    #combine and sort notes
    global chord
    chord = diaNotes + chromNotes
    chord.sort()
    #generate answer string
    global mix
    global key
    keyModifier = random.randint(0,11)
    for note in chord:
        answer+=solfege[note]+" "
    #load key signature
    key = AudioSegment.from_file("assets/keys/" + str(1 + keyModifier) + ".wav")
    #initalize root of chord
    mix = AudioSegment.from_file("assets/notes/"+str(chord[0]+keyModifier)+".wav")
    chord.pop(0)
    #generate chord audio
    for note in chord:
        file = AudioSegment.from_file("assets/notes/"+str(note+keyModifier)+".wav")
        mix = mix.overlay(file)
def playKey():
    play(key)
def playMix():
    play(mix)

#setup window
window = tk.Tk()
window.resizable(False,False)
#setup tkinter variables
numPick = tk.IntVar()
chromPick = tk.IntVar()
numPick.set(3)
chromPick.set(1)

numMenu = tk.OptionMenu(window, numPick, *numOptions)
chromMenu = tk.OptionMenu(window, chromPick, *chromOptions)
generateButton = tk.Button(window,text="new chord",command=generate)
keyButton = tk.Button(window,text="play key",command = playKey)
chordButton = tk.Button(window,text="play chord",command = playMix)
numLabel = tk.Label(window,text="Notes:")
chromLabel = tk.Label(window,text="Chromatics:")








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numLabel.grid(column=1,row=1, sticky='nesw')
    numMenu.grid(column=2,row=1, sticky='nesw')
    chromLabel.grid(column=3,row=1, sticky='nesw')
    chromMenu.grid(column=4,row=1, sticky='nesw')
    generateButton.grid(column=6,row=1, sticky='nesw')
    keyButton.grid(column=6,row=3, sticky='nesw')
    chordButton.grid(column=6,row=4, sticky='nesw')


    for i in range(0,6):
        window.grid_columnconfigure(i, weight=1, minsize=30)
    window.grid_columnconfigure(100, weight=1, minsize=30)
    for i in range(0,5):
       window.grid_rowconfigure(i, weight=1, minsize=30)
    window.grid_rowconfigure(100, weight=1, minsize=30)
    generate()
    window.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
