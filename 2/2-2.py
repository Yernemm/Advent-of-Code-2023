inp = open('2.txt', 'r')
colors = ['red', 'green', 'blue']
amounts = [12, 13, 14]

total = 0

for line in inp:
    line = line.strip()
    game = line.split(': ')[1]
    gameNum = int(line.split(': ')[0][4:])
    rounds = game.split('; ')
    validGame = True
    print(game)
    maxColors = [0,0,0]
    for round in rounds:
        
        plays = round.split(', ')
        for play in plays:
            
            s = play.split(' ');
            i = colors.index(s[1])
            if maxColors[i] < int(s[0]):
                maxColors[i] = int(s[0])

    print(maxColors)
    total += maxColors[0] * maxColors[1] * maxColors[2]
        
print('======')
print(total)
            
            
    