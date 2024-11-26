import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n, d = map(int, input().split())

    info = [[] for _ in range(d+1)] 

    for _ in range(n):
        a, b, cost = map(int, input().split())
        if b - a < cost or b > d:
            continue

        info[a].append([b, cost]) 

    hq = []
    dijkstra = [float("inf")] * (d+1)
    heapq.heappush(hq, (0, 0))
    
    dijkstra[0] = 0
    while hq:
        cost, now = heapq.heappop(hq)
        if dijkstra[now] < cost:
            continue
        
        if now == d:
            break
        
        if not info[now]:
            next_node = now + 1
            if cost + (next_node - now) < dijkstra[next_node]:
                dijkstra[next_node] = cost + (next_node - now)
                heapq.heappush(hq, (dijkstra[next_node], next_node))
        else:
            for end, edge_cost in info[now]:
                if cost + edge_cost < dijkstra[end]:
                    dijkstra[end] = cost + edge_cost
                    heapq.heappush(hq, (dijkstra[end], end))
        
        # 현재 노드에서 다음 연속된 노드로의 이동
        next_node = now + 1
        if next_node <= d and cost + 1 < dijkstra[next_node]:
            dijkstra[next_node] = cost + 1
            heapq.heappush(hq, (dijkstra[next_node], next_node))
    
    print(dijkstra[d])