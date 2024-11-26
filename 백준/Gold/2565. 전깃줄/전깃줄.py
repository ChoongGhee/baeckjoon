import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    info = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    
    dp = [1] * (n)

    for i in range(1,n):
        for j in range(i):
            if info[j][1] < info[i][1]:
                dp[i] = max(dp[i], dp[j]+1)

    print(n-max(dp))

