import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(idx: int, prev: int) -> int:
    sum = 1

    for i in range(len(info[idx])):
        if info[idx][i] == prev:
            continue
        else:
            sum += dfs(info[idx][i], idx)

    dp[idx] = sum
    return sum


if __name__ == "__main__":
    N, R, Q = map(int, input().split())
    info = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        info[a].append(b)
        info[b].append(a)

    dp = [0] * (N + 1)

    dfs(R, -1)

    for _ in range(Q):
        temp = int(input())
        print(dp[temp])
