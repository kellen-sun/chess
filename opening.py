with open("parsinggames.txt", "r") as f:
    content = f.readlines()

content = content
games = []
for i in content:
    if "[" in i or "]" in i:
        pass
    else:
        games.append(i)

gamess = [[]]
for i in games:
    if i=="" and gamess[-1]!=[]:
        gamess.append([])
    else:
        if "1."==i[:2]:
            gamess.append([])
            for j in i.split():
                if "." not in j:
                    gamess[-1].append(j)
        else:
            
            for j in i.split():
                if "." not in j:
                    gamess[-1].append(j)

print(len(gamess))
with open("parsed.txt", "w") as f:
    for game in gamess:
        f.write(" ".join(game)+"\n")