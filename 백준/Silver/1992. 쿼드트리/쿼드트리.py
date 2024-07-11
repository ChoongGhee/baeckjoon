n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().strip())))

result = []


def divide(y, x, n):
    start = matrix[y][x]
    uniform = True

    for i in range(n):
        for j in range(n):
            if matrix[y + i][x + j] != start:
                uniform = False
                break
        if not uniform:
            break

    if uniform:
        return str(start)
    else:
        return f"({divide(y, x, n // 2)}{divide(y, x + n // 2, n // 2)}{divide(y + n // 2, x, n // 2)}{divide(y + n // 2, x + n // 2, n // 2)})"


print(divide(0, 0, n))
