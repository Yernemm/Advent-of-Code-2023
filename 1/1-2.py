inp = open("1-1.txt", 'r')

spelled = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i = 0
total = 0

# this one's a bit of a mess :^)

# loop over input
for line in inp:
    line.strip
    print(f'{i} {line}')
    i=i+1
    numbers = []
    
    lowestin = 999999
    highestin = -99999
    j = 0
    for c in line:
        if line:
            
            #filter only numbers         
            if c.isnumeric():
                numbers.append(c)
                if j < lowestin:
                    lowestin = j
                if j > highestin:
                    highestin = j
                
            #num = numbers[0] + numbers[-1]
            #print(num)
        j = j+1
    
    for n, word in enumerate(spelled):
        lower = line.find(word);
        if lower < lowestin and lower > -1:
            numbers.insert(0, str(n))
            lowestin = lower
        higher = line.rfind(word)
        if higher > highestin and higher > -1:
            numbers.append(str(n))
            highestin = higher
    
    num = numbers[0] + numbers[-1]
    print(num)
    total = total + int(num)
print('=====')
print(total)