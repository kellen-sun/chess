with open('Games.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

to_add = ['(', ')'] * 1000
towrite = []
for line in text:
    movelist = line.split()[:-1]
    newmovelist = []
    for i in range(len(movelist)):
        newmovelist.append(to_add[i])
        newmovelist.append(movelist[i])
    towrite.append("\n"+"".join(newmovelist))

f = open("Games2.txt", "a")
f.writelines(towrite)
f.close()