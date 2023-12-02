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
    for round in rounds:
        
        plays = round.split(', ')
        for play in plays:
            
            s = play.split(' ');
            i = colors.index(s[1])
            if(int(s[0]) > amounts[i]):
                validGame = False;
    print(gameNum)            
    print(validGame)
    if(validGame):
        total += gameNum
        
print('======')
print(total)
            
            
    