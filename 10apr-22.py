string = 'Yo Yo Hi!! Bye!!'
b = string.split()
rev = []
for i in b:
    revers = i[:: -1]
    rev.append(revers)
print(" ".join(rev))