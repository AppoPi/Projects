

def convert(str1, str2):
    print str1
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print str2[:i+1] + str1[i+1:]

print '--'
convert('floor', 'brake')
print '--'
convert('wood', 'book')
print '--'
convert('a fall to the floor', 'braking the door in')