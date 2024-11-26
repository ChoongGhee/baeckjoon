import sys
import math

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

MAX_COLOR = math.ceil(math.log2(n)) # log2(100000) ≈ 16.6, so 17 colors are enough

def dfs(node, parent):
    # 이번 노드를 1 ~ MAX_COLOR까지 색칠할 때의 비용을 설정
    for color in range(1, MAX_COLOR + 1):
        dp[node][color] = color  # 현재 노드의 색칠 비용

    # 자식 노드들에 대해 DFS를 진행
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            # 현재 노드가 color로 칠해질 때 자식 노드들의 최소 비용을 더함
            for color in range(1, MAX_COLOR + 1):
                dp[node][color] += min(dp[child][c] for c in range(1, MAX_COLOR + 1) if c != color)

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dp[node][color]: node번 노드를 color로 칠할 때의 최소 비용
dp = [[0] * (MAX_COLOR + 1) for _ in range(n+1)]

# 1번 노드를 루트로 DFS 시작
dfs(1, 0)

# 루트 노드(1번)의 색칠 비용 중 가장 작은 값을 출력

min_cost = min(dp[1][1:])  # dp[1]에서 dp[1][1] ~ dp[1][MAX_COLOR] 중 최소값
print(min_cost)