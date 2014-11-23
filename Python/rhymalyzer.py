

#TODO: Add to rhyming dictionary

import re
import sys

ack = ["ack", "attack", "back", "black", "crack", "hack", "jack", "knack", "lack", "pack", "quack", "rack", "sack", "slack", "smack", "snack", "stack", "tack", "track", "whack", "yak"]
ail = ["ail", "bale", "fail", "hail", "mail", "male", "nail", "pail", "tale", "rail", "sail", "stale", "scale", "snail", "whale", "detail", "email"]
air = ["air", "bare", "care", "chair", "dare", "fair", "hair", "pair", "rare", "wear", "chair", "flare", "stare", "scare", "share", "spare", "square", "there", "where", "aware", "beware", "compare", "declare", "despair", "prepare", "repair", "unfair"]
ake = ["ake", "ache", "bake", "fake", "lake", "make", "rake", "take", "brake", "break", "flake", "quake", "snake", "steak", "awake", "mistake",'Blake','shake']
all = ["all", "ball", "call", "doll", "hall", "fall", "tall", "crawl", "small", "baseball", "football"]
an = ["an", "can", "fan", "man", "pan", "ran", "tan", "van", "plan", "scan", "span", "began"]
annd = ["and", "band", "hand", "land", "sand", "bland", "command", "demand", "expand", "stand", "understand"]
ap = ["ap", "cap", "gap", "map", "nap", "tap", "zap", "chap", "clap", "flap", "slap", "snap", "strap", "trap", "wrap"]
ar = ["ar", "are", "bar", "car", "far", "jar", "tar", "star", "scar", "afar", "guitar"]
at = ["at", "bat", "fat", "mat", "pat", "rat", "sat", "flat", "that", "splat", "combat"]
ate = ["ate", "date", "fate", "mate", "late", "gate", "rate", "wait", "crate", "great", "plate", "skate", "slate", "state", "straight", "trait", "weight", "create"]
ed = ["ed", "bed", "dead", "fed", "head", "led", "read", "red", "said", "bread", "fled", "spread", "thread", "tread", "instead"]
ell = ["ell", "bell", "fell", "sell", "well", "yell", "shell", "smell", "spell", "farewell", "hotel", "motel"]
en = ["en", "den", "hen", "men", "pen", "ten", "glen", "then", "when", "wren", "again"]
et = ["et", "bet", "get", "jet", "let", "met", "pet", "set", "vet", "wet", "yet", "threat", "barrette", "reset", "upset"]
inn = ["in", "bin", "chin", "inn", "pin", "tin", "grin", "thin", "twin", "skin", "begin", "within"]
ing = ["ing", "king", "ring", "sing", "wing", "zing", "bring", "cling", "fling", "sling", "spring", "sting", "string", "swing", "thing"]
it = ["it", "bit", "fit", "hit", "kit", "lit", "pit", "sit", "flit", "knit", "quit", "skit", "slit", "spit", "split", "admit", "commit", "permit"]
ite = ["ite", "bite", "kite", "bright", "fight", "fright", "knight", "night", "might", "right", "tight", "white", "write", "delight", "tonight"]
oh = ["oh", "go", "hoe", "low", "mow", "row", "sew", "toe", "blow", "crow", "dough", "flow", "know", "glow", "grow", "know", "show", "slow", "snow", "stow", "though", "throw", "ago", "although", "below"]
ot = ["ot", "cot", "dot", "got", "hot", "lot", "not", "pot", "rot", "tot", "bought", "fought", "knot", "taught", "shot", "spot", "squat", "forgot"]
ound = ["ound", "crowned", "found", "ground", "hound", "mound", "pound", "round", "sound", "wound", "around", "surround"]
oze = ["oze", "bows", "hose", "nose", "rose", "toes", "blows", "flows", "froze", "grows", "those"]
ub = ["ub", "cub", "rub", "sub", "tub", "club", "stub", "scrub", "shrub"]
un = ["un", "bun", "fun", "gun", "one", "run", "son", "sun", "ton", "won", "done", "none", "begun", "outdone", "undone"]
ay = ['ay','hay','day','play','lay','stray','decay','ray','say','stay','pray','slay']
ame = ['ame','same','dame','lame','fame','game','name','came']
est = ['est','rest','lest','nest','gest','breast']

phonics = [ack, ail, air, ake, all, an, annd, ap, ar, at, ate, ed, ell, en, et, inn, ing, it, ite, oh, ot, ound, oze, ub, un, ay, ame, est]

input ='''
The outlook wasn't brilliant for the Mudville Nine that day;
The score stood four to two, with but one inning more to play,
And then when Cooney died at first, and Barrows did the same,
A sickly silence fell upon the patrons of the game.

A straggling few got up to go in deep despair. The rest
Clung to that hope which springs eternal in the human breast;
They thought, if only Casey could get but a whack at that -
They'd put up even money, now, with Casey at the bat.

this weighs a ton
i had a lot of those
I'll bring you some bows
then go for a run
If you want to smell a rose
You must put it to your nose.
If you want to eat some bread
You must not eat it in bed
Or I will eat your toes.
I ain't no scrub
I'll have some fun
I own a club
You'll be outdone
'''

last_word_regex = '([A-Za-z\']+?)[^A-Za-z\']*$'


def getPhonetic(str):
	for x,i in enumerate(phonics):
		if str in phonics[x]:
			return phonics[x][0]
	return 'unknown'

def rhymesWith(str1, str2):
	if getPhonetic(str1) == None or getPhonetic(str2) == None:
		return False;
	return getPhonetic(str1) == getPhonetic(str2)

def getFormatted():
	pattern = re.compile(r'([A-Za-z\']+?)[^A-Za-z\']*$', re.M)
	match = re.findall(pattern, input)
	return [x.lower() for x in match]

format = getFormatted()

rhyme = [None] * len(format)
for i,v in enumerate(format):
	rhyme[i] = getPhonetic(v)


alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
bet = 0

scheme = [None] * len(format)
scheme[0] = alpha[bet]

last = rhyme[0]
used = False
changed = False

for index,value in enumerate(rhyme):
	for i,v in enumerate(rhyme):
		if value == v and index != i and scheme[i] == None:
			scheme[index] = alpha[bet]
			scheme[i] = alpha[bet]
			changed = True
	if changed:
		bet += 1
		changed = False

print input
# print format
# print rhyme
# print scheme

for i in scheme:
	sys.stdout.write(i)















