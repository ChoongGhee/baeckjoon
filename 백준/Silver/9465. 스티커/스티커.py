import sys
import heapq

input = sys.stdin.readline


def dp(column):
    if column == 1:
        return max(matrix[0][0], matrix[1][0])

    dp = matrix

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, column):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

    return max(dp[0][column - 1], dp[1][column - 1])


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        column = int(input())
        matrix = [list(map(int, input().split())) for _ in range(2)]

        print(dp(column))
