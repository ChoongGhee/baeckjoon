def solution(triangle):
    n = len(triangle)

    dp = [[0]] + triangle

    for i in range(1, n + 1):
        for j in range(i):
            if i == 1:
                continue
            elif i == 2:
                dp[i][j] += dp[i - 1][0]
            else:
                a = []
                for k in range(2):
                    if j == 0:
                        a.append(dp[i - 1][0])
                        # a.append(dp[i - 1][1])
                    elif j == i - 1:
                        # a.append(dp[i - 1][j - 2])
                        a.append(dp[i - 1][j - 1])
                    else:
                        a.append(dp[i - 1][j - 1])
                        a.append(dp[i - 1][j])

                dp[i][j] += max(a[0], a[1])

    answer = max(dp[n])
    return answer