inp = open("1-1.txt", '+r')
i = 0
total = 0
# loop over input
for line in inp:
    line.strip
    print(f'{i} {line}')
    i=i+1
    numbers = []
    for c in line:
        if line.strip():
            #filter only numbers
            
            if c.isnumeric():
                numbers.append(c)
                
            #num = numbers[0] + numbers[-1]
            #print(num)
    num = numbers[0] + numbers[-1]
    print(num)
    total = total + int(num)
print('=====')
print(total)