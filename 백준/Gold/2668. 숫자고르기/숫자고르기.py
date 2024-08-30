import sys

input = sys.stdin.readline


def dfs(idx: int, cnt: int, idx_list: list, temp: list):
    if set(temp) == set(idx_list) and cnt > 1:
        for i in idx_list:
            result[i] = info[i]
        return

    if cnt == len(info) - 1:
        return

    idx_list.append(idx)
    temp.append(info[idx])
    dfs(info[idx], cnt + 1, idx_list, temp)


if __name__ == "__main__":
    N = int(input())

    info = [0]

    result = [0] * (N + 1)
    for i in range(1, N + 1):
        info.append(int(input()))
        if info[i] == i:
            result[i] = info[i]

    for i in range(1, N + 1):
        if result[i] == 0:
            dfs(i, 1, [], [])

    while 0 in result:
        result.remove(0)

    result.sort()

    print(len(result))

    for i in result:
        print(i)
