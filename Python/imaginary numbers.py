class ComplexNumber:
	real, imag = 0, '0i'
	
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
	
	def __add__(self, x):
		return ComplexNumber(self.real + x.real,
		str(int(self.imag[:-1]) + int(x.imag[:-1])) + 'i')

	def __sub__(self, x):
		return ComplexNumber(self.real - x.real,
		str(int(self.imag[:-1]) - int(x.imag[:-1])) + 'i')
	
	def getConjugate(self):
		return ComplexNumber(self.real, str(-1 * int(self.imag[:-1]))+'i')
	
	def __str__(self):
		if self.imag[0] == '-':
			if self.real == 0:
				if self.imag == '0i':
					return '0'
				elif self.imag == '1i':
					return 'i'
				else:
					return self.imag
			else:
				if self.imag == '1i':
					return str(self.real) + '-' + 'i'
				elif self.imag != '0i':
					return str(self.real) + '-' + str(self.imag)[1:]
		
		if self.real == 0:
			if self.imag == '0i':
				return '0'
			elif self.imag == '1i':
				return 'i'
			else:
				return self.imag
		else:
			if self.imag == '1i':
				return str(self.real) + '+' + 'i'
			elif self.imag != '0i':
				return str(self.real) + '+' + self.imag
			else:
				return str(self.real)

i = ComplexNumber(0, '3i')
print i
i = ComplexNumber(0, '0i')
print i
j = ComplexNumber(3, '1i')
print j
j = ComplexNumber(3, '0i')
print j
i = ComplexNumber(0, '-4i')
print i
i = ComplexNumber(-5, '0i')
print i
i = ComplexNumber(5, '-5i')
print i
i = ComplexNumber(-3, '-7i')
print i

