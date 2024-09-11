import sys
from itertools import combinations

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    info = [list(map(int, input().split())) for _ in range(n)]

    combi = list(combinations(range(n), n // 2))

    so_min = 100

    for i in combi:
        remain = []
        for j in range(n):
            if j not in i:
                remain.append(j)
        comcombi = list(combinations(i, 2))
        com_remain = list(combinations(remain, 2))

        start = 0
        link = 0
        for i in range(len(comcombi)):
            start += (
                info[comcombi[i][0]][comcombi[i][1]]
                + info[comcombi[i][1]][comcombi[i][0]]
            )
            link += (
                info[com_remain[i][0]][com_remain[i][1]]
                + info[com_remain[i][1]][com_remain[i][0]]
            )

        temp = abs(start - link)
        if so_min > temp:
            so_min = temp

    print(so_min)
