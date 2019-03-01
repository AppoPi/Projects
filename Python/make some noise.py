import winsound

dict = {
'C' : 262,
'D' : 294,
'E' : 330,
'F' : 349,
'G' : 392,
'A' : 440,
'B' : 494}

duration = 250
str = 'C1 D1 E1 F1 G1 A1 B1'

def play(str):
    notes = str.split(' ')
    for i in notes:
        winsound.Beep(dict[i[0]], duration * int(i[1]))

# play(str)

play('C0 D0 E0')