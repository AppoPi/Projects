w = []
with open('enable1.txt','r') as f:
    w = f.read().split('\n')

def b(s):
    for i in w:
        if set(s) == set(i):
            print i

b('plus')