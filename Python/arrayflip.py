list = [1,3,1,3,2]

def arrayflip(list):
	for i in range(len(list)/2):
		list[i] += list[len(list)-i-1]

	for i in range(len(list)/2, len(list)):
		if i != len(list)-i-1:
			list[i] = list[len(list)-i-1] - list[i]
			list[len(list)-i-1] -= list[i]
	return list

print list
print arrayflip(list)