import sys
import heapq


def Dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    cost_table[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if cost_table[node] < cost:
            continue
        for child in info_table[node]:
            cost = cost_table[node] + child[0]
            if cost < cost_table[child[1]]:
                cost_table[child[1]] = cost
                heapq.heappush(q, [cost, child[1]])


if __name__ == "__main__":

    input = sys.stdin.readline

    INF = int(1e9)

    N = int(input())
    M = int(input())

    info_table = [[] for _ in range(N + 1)]  # N+1 크기로 변경

    for _ in range(M):
        start, goal, cost = map(int, input().split())
        info_table[start].append([cost, goal])

    origin, destination = map(int, input().split())

    cost_table = [INF] * (N + 1)

    Dijkstra(origin)

    if cost_table[destination] == INF:
        print("도달불가")
    else:
        print(cost_table[destination])
