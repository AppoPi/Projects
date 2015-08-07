import re

symbols = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cg In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta  W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Uut Lv Uus Uuo'.lower().split()

def bb(s):
	global symbols
	
	for i in range(len(s)):
		if s[i] in symbols:
			print s[:i] + '[' + s[i].capitalize() + ']' + s[i+1:]
		if i < len(s) - 1:
			if s[i:i+2] in symbols:
				print s[:i] + '[' + s[i:i+2].capitalize() + ']' + s[i+3:]

bb('dailyprogrammer')
bb('helium')
bb('test')
bb('petroleum jelly today')