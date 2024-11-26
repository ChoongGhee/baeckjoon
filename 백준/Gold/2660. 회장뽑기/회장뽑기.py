import sys

input = sys.stdin.readline
INF = float("inf")

if __name__ == "__main__":
    n = int(input())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]


    for i in range(1, n+1):
        graph[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break

        graph[a][b] = 1
        graph[b][a] = 1
        

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(n + 1):
        for b in range(n + 1):
            if graph[a][b] == INF:
                graph[a][b] = 0

    max_list = [INF] * (n+1)

    for i in range(1, n+1):
        max_list[i] = max(graph[i])

    chirman_val = min(max_list)
    print(chirman_val, max_list.count(chirman_val))
    
    for i in range(1, n+1):
        if chirman_val == max_list[i]:
            print(i, end=" ")