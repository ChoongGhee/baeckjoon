n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

W = 0
B = 0


def divide(x, y, n):
    global W, B
    start = matrix[x][y]

    is_same_inside = True
    for i in range(n):
        for j in range(n):
            if matrix[x + i][y + j] != start:
                is_same_inside = False
                break
        if not is_same_inside:
            break

    if is_same_inside:
        if start == 0:
            W += 1
        else:
            B += 1
    else:

        divide(x, y, n // 2)
        divide(x + n // 2, y, n // 2)
        divide(x, y + n // 2, n // 2)
        divide(x + n // 2, y + n // 2, n // 2)


divide(0, 0, n)
print(W)
print(B)