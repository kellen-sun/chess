with open("Games.txt", "r") as f:
    games = f.readlines()

for i in range(len(games)):
    game = games[i].split()
    for j in range(len(game)):
        move = game[j]
        if "Q" not in move and "R" not in move and "N" not in move and "x" in move and move!="O-O" and move!="O-O-O" and "B" not in move and move!="1-0" and move!="0-1" and move!="1/2-1/2" and "K" not in move:
            print(move)