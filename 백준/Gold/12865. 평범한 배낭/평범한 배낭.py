import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (K + 1)

    for weight, value in items:
        for i in range(K, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + value)

    print(dp[K])
