import sys
from collections import deque

input = sys.stdin.readline

MAXN = 401  # 정점의 최대 수, 필요에 따라 조정
INF = float('inf')

capacity = [[0] * MAXN for _ in range(MAXN)]
flow = [[0] * MAXN for _ in range(MAXN)]

def bfs(source, sink, parent):
    visited = [False] * MAXN  # 방문 여부 체크
    queue = deque([source])
    visited[source] = True
    parent[source] = -1  # 시작점의 부모는 없음을 의미

    while queue:
        here = queue.popleft()

        for there in range(MAXN):
            # 잔여 용량이 있고 방문하지 않은 노드
            if capacity[here][there] - flow[here][there] > 0 and not visited[there]:
                queue.append(there)
                visited[there] = True
                parent[there] = here
                if there == sink:
                    return True  # sink에 도달하면 경로 찾음

    return False  # 경로를 찾지 못함

def edmonds_karp(source, sink):
    total_flow = 0  # 총 유량 초기화
    parent = [-1] * MAXN  # 부모 노드 배열 초기화

    while bfs(source, sink, parent):  # 증가 경로가 있는 동안
        # 증가 경로의 최소 잔여 용량 찾기
        path_flow = INF
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]

        # 유량 업데이트
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow  # 정방향 유량 증가
            flow[v][u] -= path_flow  # 역방향 유량 감소
            v = parent[v]

        total_flow += path_flow  # 총 유량에 추가

    return total_flow



def main():
    N, P = map(int, input().split())

    for _ in range(P):
        a, b = map(int, input().split())
        capacity[a][b] += 1  # 간선의 용량을 1로 설정 (여러 번 추가할 경우 용량 증가)

    max_flow = edmonds_karp(1, 2)
    print(max_flow)

if __name__ == "__main__":
    main()