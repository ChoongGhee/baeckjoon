import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    dp0 = 1
    dp1 = 1
    dp2 = 1

    for i in range(2, N + 1):
        dp0 = dp2 + dp1
        dp1 = dp2 + (dp0 - dp2)
        dp2 = (dp1 - dp2) + (dp0 - dp2) + dp2

    print((dp2 + dp1 + dp0) % 9901)
