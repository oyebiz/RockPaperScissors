import random

rps = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}

options = list(rps)

while True:
    Player = input('Choose one, "R" for rock, "P" for paper, "S" for scissors: ')
    CPU = random.choice(options)

    if Player not in options:
        print("Error!!! Please choose a vaild option.")
    elif Player == CPU:
        print("Tie!!! Play again.")
    else:
        print('Player ({}) : CPU ({})'.format( rps[Player], rps[CPU]))
        
        result = Player + CPU

        if result in ['RS', 'PR', 'SP']:
            print('Player beats CPU')
        elif win in ['SR', 'RP', 'PS']:
            print('CPU beats Player')

        break
