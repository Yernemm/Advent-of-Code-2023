
inp = open('3.txt', 'r')
# list of lines
text = inp.readlines()

total = 0

gearMap = {}


def isSymbol(char):
    return char == '*'

def isPartDigit(x, y):
    flag = False
    coords = set()
    
    for xx in range(-1, 2):
        for yy in range(-1, 2):
            print(f'{x+xx}-{y+yy}')
            if(isSymbol(text[y+yy][x+xx])):
               flag = True
               coords.add(f'{x+xx}-{y+yy}')
               

    return flag, coords

#pre-process input
for idx, line in enumerate(text):
    text[idx] = text[idx].strip()
    text[idx] = "." + text[idx] + "."

line = ''
for i in text[0]:
    line += '.'

text.insert(0,line)
text.append(line)

#check numbers, generate gearmap
for y, line in enumerate(text):
    number = ""
    isPart = False
    coordsSet = set()
    for x, char in enumerate(line):
        if char.isnumeric():
            number += char
            flag, coords = isPartDigit(x, y)
            coordsSet.update(coords)
            isPart = isPart or flag
        elif len(number) > 0:
            #end of number
            print(number) 
            print("")
            if(isPart):
                # part number
                #total += int(number)
                isPart = False
                for coord in coordsSet:
                    if not coord in gearMap:
                        gearMap[coord] = set()
                    gearMap[coord].add(int(number))
            number = ""
            coordsSet = set()

#print(text)
print(gearMap)

productTotal = 0

#process gear map
for gear in gearMap:
    parts = gearMap[gear]
    if(len(parts) == 2):
        print(f'{gear} {parts}')
        part1 = parts.pop()
        part2 = parts.pop()
        productTotal += part1 * part2
        
print(productTotal)

#10953711
#72553319