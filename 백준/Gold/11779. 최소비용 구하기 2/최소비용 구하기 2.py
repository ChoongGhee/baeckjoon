import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

graph = []
distance = []

def dijkstra(start):
    global distance, graph

    hq = []
    heapq.heappush(hq, [0, start, [start]])

    while hq:
        current_cost, current_node, current_list = heapq.heappop(hq)

        if distance[current_node][0] < current_cost:
            continue
        
        for adjacent, weight in graph[current_node]:
            modify_cost = current_cost + weight

            if modify_cost < distance[adjacent][0]:
                new_path = current_list[:] + [adjacent]  # 새로운 경로 생성
                distance[adjacent] = [modify_cost, new_path]
                heapq.heappush(hq, [modify_cost, adjacent, new_path])
    

def main():
    global visited, distance, graph

    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        st, en, cost = map(int, input().split())
        graph[st].append((en, cost))
    
    start, end = map(int, input().split())

    distance = [[INF, []] for _ in range(n+1)]  # [비용, 경로] 형태로 초기화

    dijkstra(start)

    print(distance[end][0])
    print(len(distance[end][1]))
    print(*distance[end][1])
    

    
main()