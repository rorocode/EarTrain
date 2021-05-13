# This is a sample Python script.
import random
import warnings
warnings.filterwarnings("ignore")
from pydub import AudioSegment
from pydub.playback import play

diatonic = [1,3,5,6,8,10,12,13,15,17,18,20,22,24,25]
chromatic = [2,4,7,9,11,14,16,19,21,23]
solfege = ["ti","do","ra","re","me","mi","fa","fi","so","le","la","te","ti","do","ra","re","me","mi","fa","fi","so","le","la","te","ti","do"]
chord = []
answer = ""
numPref = 3
chromPref = 0

def generate(total,chrom):
    dia=total-chrom
    diaNotes=random.sample(diatonic, dia)
    chromNotes=random.sample(chromatic, chrom)
    chord = diaNotes + chromNotes
    chord.sort()
    global answer
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











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate(numPref,chromPref)
    play(key)
    play(mix)
    print("answer: "+answer)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
