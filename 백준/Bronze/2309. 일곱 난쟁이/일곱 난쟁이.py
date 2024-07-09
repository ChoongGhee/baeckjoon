height = []
for i in range(9):
    height.append(int(input()))

for i in range(8):
    for j in range(i + 1, 9):
        b = height.copy()
        del b[j]
        del b[i]
        if sum(b) == 100:
            b.sort()
            for h in b:
                print(h)
            exit()
