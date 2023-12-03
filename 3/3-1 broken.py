# FIRST ATTEMPT -- THIS ONE DOESNT WORK


inp = open('3.txt', 'r')
# list of lines
text = inp.readlines()

total = 0


def isSymbol(char):
    return (not char.isnumeric()) and (not char == '.')

for idx, line in enumerate(text):
    debug1 = ""
    debug2 = ""
    debug3 = ""
    text[idx] = text[idx].strip()
    text[idx] = "." + text[idx] + "."
    print(text[idx])
    runningNumber = ""
    partNumber = False
    for jdx, char in enumerate(text[idx]):
        if(char.isnumeric()):
            #checking number
            #print(char)
            if len(runningNumber) == 0:
                #first digit of number
                if jdx > 0:
                    #check previous column if this is not the first column
                    
                    #same row, left
                    partNumber = partNumber or (isSymbol(text[idx][jdx-1]))
                    #print(partNumber)
                    #top-left         
                    partNumber = partNumber or (idx > 0 and isSymbol(text[idx-1][jdx-1]))
                    #print(partNumber)
                    #bottom-left
                    partNumber = partNumber or (idx < (len(text)-1) and isSymbol(text[idx+1][jdx-1]))
                    #print(partNumber)
                    
                    #debug1 += text[idx-1][jdx-1] if idx > 0 else ""
                    #debug2 += text[idx][jdx-1]
                    #debug3 += text[idx+1][jdx-1] if idx < (len(text)-1) else ""
                    
            #above
            partNumber = partNumber or (idx > 0 and isSymbol(text[idx-1][jdx]))
            #print(partNumber)
            #below
            partNumber = partNumber or (idx < (len(text)-1) and isSymbol(text[idx+1][jdx]))
            #print(partNumber)
            
            runningNumber += char
            
            #debug1 += text[idx-1][jdx] if idx > 0 else ""
            #debug2 += text[idx][jdx]
            #debug3 += text[idx+1][jdx] if idx < (len(text)-1) else ""
            
        else:
            #not number
            if len(runningNumber) > 0:
                #number just ended
                
                #above
                partNumber = partNumber or (idx > 0 and isSymbol(text[idx-1][jdx]))
                #print(partNumber)
                #below
                partNumber = partNumber or (idx < (len(text)-1) and isSymbol(text[idx+1][jdx]))
                #print(partNumber)
                #middle
                partNumber = partNumber or (isSymbol(text[idx][jdx]))
                #print(partNumber)
                
                #debug1 += text[idx-1][jdx] if idx > 0 else ""
                #debug2 += text[idx][jdx]
                #debug3 += text[idx+1][jdx] if idx < (len(text)-1) else ""
                    
                
                if(partNumber):
                    #print(f'{idx+1}:{jdx+1} - {runningNumber}')
                    #print("")
                    #print(debug1)
                    #print(debug2)
                    #print(debug3)
                    #print(runningNumber)
                    total += int(runningNumber)
                    a = 0
                else:
                    a =0
                #print("-----------------")
                partNumber = False
                runningNumber = ""
                debug1 = ""
                debug2 = ""
                debug3 = ""
            
print('===================')
print(total)