def TSP(start, now, sum, cnt):
    global ans
    if cnt == n:
        if W[now][start]:
            if ans == 0 or sum + W[now][start] < ans:
                ans = sum + W[now][start]
    for i in range(n):
        if not flag[i] and W[now][i]:
            flag[i] = True
            TSP(start, i, sum + W[now][i], cnt + 1)
            flag[i] = False


n = int(input())
W = []
for i in range(n):
    W.append(list(map(int, input().split())))

flag = [False] * n
ans = 0

for i in range(n):
    flag[i] = True
    TSP(i, i, 0, 1)
    flag[i] = False

print(ans)
