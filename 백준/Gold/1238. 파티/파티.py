import sys
import heapq

input = sys.stdin.readline
INF = float('inf')
graph = []

def dijkstra(start:int, end:int)->int:
    global graph

    if start == end:
        return 0
    
    costs = [INF] * len(graph)

    hq = [(0, start)]

    while hq:
        cur_cost, cur = heapq.heappop(hq)

        if cur == end:
            return cur_cost
        
        if cur_cost > costs[cur]:
            continue

        for next, cost in graph[cur]:
            sum_cost = cur_cost + cost

            if sum_cost < costs[next]:
                costs[next] = sum_cost
                heapq.heappush(hq, (sum_cost, next))
    
    return costs[end]

def main():
    global graph
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, cost = map(int, input().split())
        graph[start].append([end, cost])

    max_time = 0

    for i in range(1, N+1):
        go = dijkstra(i, X)
        back = dijkstra(X, i)
        max_time = max(max_time, go+back)

    print(max_time)

main()