
# def scrabble(rack, word):
    # for i in word:
        # f = rack.find(i)
        # if f != -1:
            # rack = rack[:f] + rack[f+1:]
        # else:
            # return False
    # return True
    
def scrabble(rack, word):
    count = 0
    for i in word:
        f = rack.find(i)
        if f != -1:
            rack = rack[:f] + rack[f+1:]
        else:
            count += 1
    if rack.count('?') >= count:
        return True
    else:
        return False

print scrabble('ladilmy', 'daily')
print scrabble('eerriin', 'eerie')
print scrabble('orrpgma', 'program')
print scrabble('orppgma', 'program')
print scrabble("pizza??", "pizzazz")
print scrabble("piizza?", "pizzazz")
print scrabble("a??????", "program")
print scrabble("b??????", "program")