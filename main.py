import math, random
from midiutil.MidiFile import MIDIFile

midi = MIDIFile(1)

scale = [
    59, # B - 0
    60, # C - 1
    62, # D - 2
    64, # E - 3
    65, # F - 4
    67, # G - 5
    69, # A - 6
    71, # B - 7
    72, # C - 8
    74]  # D - 9

totalscale = []

pattern = [0, 2, 4, 5, 7, 9, 11]

for octive in range(7):
    for note in range(7):
        totalscale.append((octive*12)+pattern[note])

beat = 0
scaleadd = 7

def addnote(index):
    global beat, midi

    note = scale[index]+scaleadd

    if beat % 4 == 0:
        midi.addNote(0, 0, note-24, beat+(random.randint(-20, 20)/400), 4, 90+random.randint(-8, 8))

        if note-scaleadd-17 in totalscale:
            midi.addNote(0, 0, note-17, beat+(random.randint(-20, 20)/400), 4, 90+random.randint(-8, 8))
        else:
            midi.addNote(0, 0, note-16, beat+(random.randint(-20, 20)/400), 4, 90+random.randint(-8, 8))
        
        midi.addNote(0, 0, note-12, beat+(random.randint(-20, 20)/400), 4, 90+random.randint(-8, 8))

    midi.addNote(0, 0, note, beat+(random.randint(-20, 20)/400), 1, 100)

    beat += 1

def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield n
            # insert period after first digit
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

text = ""

for i in calcPi(10000):
    text += str(i)

for char in text:
    addnote(int(char))

with open("output.mid", 'wb') as outf:
    midi.writeFile(outf)