inp = open('4.txt', 'r')
# list of lines
text = inp.readlines()

def parseNums(numString):
    numList = set()
    while(len(numString) > 0):
        numList.add(int(numString[0:3]))
        numString = numString[3:]
    return numList
    
total = 0

cardNums = []

#pre-process input
for idx, line in enumerate(text):
    text[idx] = text[idx].strip()
    cardNums.append(1)

for idx, line in enumerate(text):
    text1 = line.split(": ")[1]
    nums = text1.split(" | ")
    
    winningSet = parseNums(nums[0])
    haveSet = parseNums(nums[1])
    
    intersect = winningSet.intersection(haveSet)
    print(intersect)
    
    #value = 0 if len(intersect) == 0 else pow(2, len(intersect) -1)
    value = len(intersect)
    
    for i in range(0,value):
        if(idx + i + 1 < len(cardNums)):
            cardNums[idx + i + 1] += cardNums[idx]
    
    
    
    total += value
    
    print(value)
    
total = sum(cardNums)
print(cardNums)
print(total)
    
    