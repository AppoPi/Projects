

def gameOfThree(num):
    ret = str(num) + ' '
    while(num > 1):
        if num % 3 == 1:
            num -= 1
            ret += '-1'
        elif num % 3 == 2:
            num += 1
            ret += '+1'
        else:
            ret += '0'
        num /= 3
        ret += '\n' + str(num) + ' '
    return ret
    
print gameOfThree(100)

print gameOfThree(31337357)