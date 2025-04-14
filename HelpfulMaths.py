def helpfulMath(s:str) -> str:
    number = s.split('+')
    number.sort()
    return '+'.join(number)

print(helpfulMath('1+2+3+6+2'))