

equation = '(a(b(c)))'

def isBalanced(equation):
    list = []
    for i in equation:
        if i in '([{':
            list.append('(')
        elif i in ')]}':
            try:
                if list[-1] == '(' and i == ')':
                    list.pop()
                elif list[-1] == '[' and i == ']':
                    list.pop()
                elif list[-1] == '{' and i == '}':
                    list.pop()
                else:
                    print list[-1]
                    print i
                    return 'Punch'
            except Exception as e:
                print e
    return not list

print isBalanced(equation)
print int(ord('{'))
print int(ord('}'))