import sys

def Topologi():
    # 시작 노드를 찾는 부분을 함수 시작 시 한 번만 수행
    for i in range(1, N + 1):
        if in_degree[i] == 0 and not visit[i]:
            queue.append(i)
    
    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        visit[current] = True
        
        for next_node in info_table[current]:
            in_degree[next_node] -= 1
            # 진입차수가 0이 되고 방문하지 않은 노드를 바로 큐에 추가
            if in_degree[next_node] == 0 and not visit[next_node]:
                queue.append(next_node)

if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    info_table = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)  # 변수명을 'in_degree'로 수정 (오타 수정)

    for _ in range(M):
        node, connect = map(int, input().split())
        info_table[node].append(connect)
        in_degree[connect] += 1

    queue = []
    visit = [False] * (N + 1)
    Topologi()