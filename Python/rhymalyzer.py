#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


ack = ["back", "lack", "pack", "rack", "sack", "tack", "yak", "black", "knack", "quack", "slack", "smack", "snack", "stack", "track", "whack", "attack"]
ail = ["bale", "fail", "hail", "mail", "male", "nail", "pail", "tale", "rail", "sail", "stale", "scale", "snail", "whale", "detail", "email"]
air = ["air", "bare", "care", "chair", "dare", "fair", "hair", "pair", "rare", "wear", "chair", "flare", "stare", "scare", "share", "spare", "square", "there", "where", "aware", "beware", "compare", "declare", "despair", "prepare", "repair", "unfair"]
ake = ["ache", "bake", "fake", "lake", "make", "rake", "take", "brake", "break", "flake", "quake", "snake", "steak", "awake", "mistake"]
all = ["all", "ball", "call", "doll", "hall", "fall", "tall", "crawl", "small", "baseball", "football"]
an = ["an", "can", "fan", "man", "pan", "ran", "tan", "van", "plan", "scan", "span", "began"]
annd = ["and", "band", "hand", "land", "sand", "bland", "command", "demand", "expand", "stand", "understand"]
ap = ["cap", "gap", "map", "nap", "tap", "zap", "chap", "clap", "flap", "slap", "snap", "strap", "trap", "wrap"]
ar = ["are", "bar", "car", "far", "jar", "tar", "star", "scar", "afar", "guitar"]
at = ["at", "bat", "fat", "mat", "pat", "rat", "sat", "flat", "that", "splat", "combat"]
ate = ["ate", "date", "fate", "mate", "late", "gate", "rate", "wait", "crate", "great", "plate", "skate", "slate", "state", "straight", "trait", "weight", "create"]
ed = ["bed", "dead", "fed", "head", "led", "read", "red", "said", "bread", "fled", "spread", "thread", "tread", "instead"]
ell = ["bell", "fell", "sell", "well", "yell", "shell", "smell", "spell", "farewell", "hotel", "motel"]
en = ["den", "hen", "men", "pen", "ten", "glen", "then", "when", "wren", "again"]
et = ["bet", "get", "jet", "let", "met", "pet", "set", "vet", "wet", "yet", "threat", "barrette", "reset", "upset"]
inn = ["bin", "chin", "in", "pin", "tin", "grin", "thin", "twin", "skin", "begin", "within"]
ing = ["king", "ring", "sing", "wing", "zing", "bring", "cling", "fling", "sling", "spring", "sting", "string", "swing", "thing"]
it = ["bit", "fit", "hit", "it", "kit", "lit", "pit", "sit", "flit", "knit", "quit", "skit", "slit", "spit", "split", "admit", "commit", "permit"]
ite = ["bite", "kite", "bright", "fight", "fright", "knight", "night", "might", "right", "tight", "white", "write", "delight", "tonight"]
oh = ["go", "hoe", "low", "mow", "row", "sew", "toe", "blow", "crow", "dough", "flow", "know", "glow", "grow", "know", "show", "slow", "snow", "stow", "though", "throw", "ago", "although", "below"]
ot = ["cot", "dot", "got", "hot", "lot", "not", "pot", "rot", "tot", "bought", "fought", "knot", "taught", "shot", "spot", "squat", "forgot"]
ound = ["crowned", "found", "ground", "hound", "mound", "pound", "round", "sound", "wound", "around", "surround"]
oze = ["bows", "hose", "nose", "rose", "toes", "blows", "flows", "froze", "grows", "those"]
ub = ["cub", "rub", "sub", "tub", "club", "stub", "scrub", "shrub"]
un = ["bun", "fun", "gun", "one", "run", "son", "sun", "ton", "won", "done", "none", "begun", "outdone", "undone"]


phonics = [ack, ail, air, ake, all, an, annd, ap, ar, at, ate, ed, ell, en, et, inn, ing, it, ite, oh, ot, ound, oze, ub, un]

input ='''
Thanks Anna for trying your hardest to make us sexy pole dancers.
It's not your fault, haha...
Watch more Anna! http://youtube.com/annaakana
'''




'''
A straggling few got up to go in deep despair. The rest
Clung to that hope which springs eternal in the human breast
They thought, if only Casey could get but a whack at that
They'd put up even money, now, with Casey at the bat
'''


'''
I ain't no scrub
I'll have some fun
I own a bun
but I choose gun
'''


'''
This is a rhyme
I've got no time
Poems blow
You're a hoe
'''


'''
If you want to smell a rose
You must put it to your nose.
If you want to eat some bread
You must not eat it in bed
Or I will eat your toes.
'''




def getPhonetic(str):
	for x,i in enumerate(phonics):
		if str in phonics[x]:
			return phonics[x]
	return None

def rhymesWith(str1, str2):
	if getPhonetic(str1) == None or getPhonetic(str2) == None:
		return False;
	return getPhonetic(str1) == getPhonetic(str2)

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

def getFormatted():
	format = []
	print input.split('\n')
	
	for i,c in enumerate(input.split('\n')):
		match = re.findall(r'[A-Za-z]+\W*\Z', i)
		if match:
			format[i] = match[0]
	
	
	print i
	'''
		str = i[i.rfind(' ')+1:]
		if str != '':
			format.append(str)
	
	for i, str in enumerate(format):
		format[i] = re.sub(r'\W', '', str)
	'''
	return format

format = getFormatted()
# print "--------Input--------", input
# print "--------Output--------"
# print format

# p = re.compile("[a-z]")
# for m in p.finditer('a1b2c3d4'):
    # print m.start(), m.group()


'''
char = ['A','B','C','D','E','F','G','H','I']
scheme = [None] * len(format)

letter = 0;
scheme[0] = char[letter]
for i in range(0, len(format)):
	if scheme[i] == None:
		scheme[i] = char[letter]
	for j in range(i,len(format)):
		if i != j:
			if rhymesWith(format[i], format[j]):
				scheme[j] = scheme[i]
	#letter += 1
print scheme



'''







