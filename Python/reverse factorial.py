

def rfactorial(num):
    output = []
    factorial = 1
    i = 0
    while i < num:
        i += 1
        factorial *= i
        if factorial == num:
            return str(num) + ' = ' + str(i) + '!'
        elif factorial > num:
            break 
    return str(num) + ' NONE'


print rfactorial(120)
print rfactorial(150)
print rfactorial(3628800)
print rfactorial(479001600)
print rfactorial(6)
print rfactorial(18)