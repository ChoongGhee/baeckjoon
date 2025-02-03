import sys
import heapq
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]  # 선수 관계 저장
    indegree = [0] * (N+1)  # 각 노드로 들어오는 간선 수
    visit = [True] * (N+1)
    visit[0] = False

    for _ in range(M):
        easy, difficult = map(int, input().split())
        graph[easy].append(difficult)
        indegree[difficult] += 1

    hq = []
    for i in range(1, N+1):
        if indegree[i] == 0:  # 선행 조건이 없는 문제들
            heapq.heappush(hq, i)
    
    while hq:
        current = heapq.heappop(hq)
        print(current, end=' ')

        visit[current] = False
        
        # current를 풀고 난 후에 풀 수 있는 문제들 확인
        for next_problem in graph[current]:
            indegree[next_problem] -= 1
            if indegree[next_problem] == 0:  # 모든 선행 조건이 충족된 경우
                heapq.heappush(hq, next_problem)

        
main()