

def stddev(s):
	print s
	nums = s.split(' ')
	sum = 0
	c = len(nums)
	for i in nums:
		sum += float(i)
	mean = sum * 1.0 / c
	# print 'Mean: %.4f' % mean
	sum = 0
	for i in nums:
		sum += (float(i) - float(mean)) ** 2
	# print 'Variance: ' + str(sum)
	print '%.4f' % ((sum * 1.0 / c) ** .5)

input = ['5 6 11 13 19 20 25 26 28 37', '37 81 86 91 97 108 109 112 112 114 115 117 121 123 141', '266 344 375 399 409 433 436 440 449 476 502 504 530 584 587', '809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 1187 1208 1215 1229 1241 1260 1373']

for i in input:
	stddev(i)