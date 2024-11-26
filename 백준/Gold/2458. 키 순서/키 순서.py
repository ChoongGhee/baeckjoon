import sys

input = sys.stdin.readline
INF = float("inf")

if __name__ == "__main__":
    n, m= map(int, input().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]


    for i in range(1, n+1):
        graph[i][i] = 0

    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    
    cnt = 0
    for a in range(1, n + 1):
        can = True
        for b in range(1, n + 1):
            if a == b:
                continue
            if graph[a][b] == INF and graph[b][a] == INF:
                can = False
                break
        if can:
            cnt += 1

    print(cnt)
