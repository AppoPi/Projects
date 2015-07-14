

def printSnake(str):
	words = str.split(' ')
	i = 0
	prevLength = 1
	for i in range(len(words)):
		if i == 0:
			print words[i]
			prevLength += len(words[i]) - 1
		elif i % 2 == 0:
			print ' ' * (prevLength - 1) + words[i]
			prevLength += len(words[i]) - 1
		else:
			for j in range(1, len(words[i])):
				print ' ' * (prevLength - 1) + words[i][j]
			
				
# printSnake('TEST TEST TEST TEST')
printSnake('SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE')
printSnake('DELOREAN NEUTER RAMSHACKLE EAR RUMP PALINDROME EXEMPLARY YARD')
printSnake('CAN NINCOMPOOP PANTS SCRIMSHAW WASTELAND DIRK KOMBAT TEMP PLUNGE ESTER REGRET TOMBOY')
printSnake('NICKEL LEDERHOSEN NARCOTRAFFICANTE EAT TO OATS SOUP PAST TELEMARKETER RUST THINGAMAJIG GROSS SALTPETER REISSUE ELEPHANTITIS')