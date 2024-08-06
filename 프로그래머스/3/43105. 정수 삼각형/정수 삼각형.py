def solution(triangle):
    n = len(triangle)

    for i in range(n):
        for j in range(i+1):
            if i == 0:
                continue
            elif i == 1:
                triangle[i][j] += triangle[i - 1][0]
            else:
                a = []
                for k in range(2):
                    if j == 0:
                        a.append(triangle[i - 1][0])
                    # a.append(triangle[i - 1][1])
                    elif j == i:
                    # a.append(triangle[i - 1][j - 2])
                        a.append(triangle[i - 1][j - 1])
                    else:
                        a.append(triangle[i - 1][j - 1])
                        a.append(triangle[i - 1][j])

                triangle[i][j] += max(a[0], a[1])

    answer = max(triangle[-1])
    return answer