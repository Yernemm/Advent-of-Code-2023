
inp = open('3.txt', 'r')
# list of lines
text = inp.readlines()

total = 0


def isSymbol(char):
    return (not char.isnumeric()) and (not char == '.')

def isPartDigit(x, y):
    flag = False
    flag = flag or isSymbol(text[y-1][x-1])
    flag = flag or isSymbol(text[y-1][x])
    flag = flag or isSymbol(text[y-1][x+1])
    
    flag = flag or isSymbol(text[y][x-1])
    flag = flag or isSymbol(text[y][x+1])
    
    flag = flag or isSymbol(text[y+1][x-1])
    flag = flag or isSymbol(text[y+1][x])
    flag = flag or isSymbol(text[y+1][x+1])
    return flag

#pre-process input
for idx, line in enumerate(text):
    text[idx] = text[idx].strip()
    text[idx] = "." + text[idx] + "."

line = ''
for i in text[0]:
    line += '.'

text.insert(0,line)
text.append(line)

#check numbers
for y, line in enumerate(text):
    number = ""
    isPart = False
    for x, char in enumerate(line):
        if char.isnumeric():
            number += char
            isPart = isPart or isPartDigit(x, y)
        elif len(number) > 0:
            print(number) 
            if(isPart):
                total += int(number)
                isPart = False
            number = ""

print(text)
print(total)
