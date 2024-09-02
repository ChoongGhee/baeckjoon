import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(idx, parent):
    for i in range(len(info[idx])):
        next_node = info[idx][i][0]
        cost = info[idx][i][1]

        if next_node == parent:
            continue

        temp = dfs(next_node, idx) + cost

        # 첫 번째로 큰 값과 두 번째로 큰 값 업데이트
        if temp > dp[idx][0]:
            dp[idx][1] = dp[idx][0]
            dp[idx][0] = temp
        elif temp > dp[idx][1]:
            dp[idx][1] = temp

    return dp[idx][0]


if __name__ == "__main__":
    N = int(input())

    info = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        pa, ch, cost = map(int, input().split())
        info[pa].append([ch, cost])
        info[ch].append([pa, cost])

    dp = [[0, 0] for _ in range(N + 1)]

    dfs(1, -1)

    max_val = 0
    for i in range(1, N + 1):
        sum = dp[i][0] + dp[i][1]
        if sum > max_val:
            max_val = sum

    print(max_val)
