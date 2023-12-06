inp = open('input.txt', 'r')
# list of lines
text = inp.readlines()

for idx, line in enumerate(text):
    text[idx] = text[idx].strip()

seeds = []
maps = []
curerntMap = []

seeds = text[0].split(": ")[1].split(" ")
text = text[2:]

#makes the parser work easier
text.append("map")

#parse
for idx, line in enumerate(text):
    
    if(line.find("map") >= 0):
        maps.append(curerntMap)
        curerntMap = []
        
    elif(len(line) == 0):
        pass
    else:
        #map parsing
        curerntMap.append(line.split(" "))
    
    
print(seeds)
for map in maps:
    print("=========")
    print(map)
    
    
lowestLocation = 99999999999999999999999
currentLocation = 0

for seed in seeds:
    journey = f'{seed}'
    currentLocation = int(seed)
    for map in maps:
        found = -1
        for mapping in map:
            print(mapping)
            if currentLocation >= int(mapping[1]) and currentLocation < int(mapping[1]) + int(mapping[2]):
                #successfully found mapping
                found = (currentLocation - int(mapping[1])) + int(mapping[0])
                print(f'found {found}')
                print(f'{currentLocation} - {mapping[1]} + {mapping[0]} = {found}')
        if found == -1:
            found = currentLocation
            print(f'not found {found}')
        journey = f'{journey}->{found}'
        print('h')
        currentLocation = found #I was missing this line all along which is why it wasn't working aaaaaaaaaaaaa
    lowestLocation = currentLocation if currentLocation < lowestLocation else lowestLocation
    print(currentLocation)
    print(journey)
    
print(lowestLocation)
                