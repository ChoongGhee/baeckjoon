#### 1차 막힘. dp 배열을 어떻게 구성할지 고민. > 각 행이 중간다리의 갯수(집합 어딘진 모름)을 나타내도록 했음. > 아닌 것 같아 claude질문 비트마스킹?
#### 1차 해답 : Claude 피셜 비트마스킹 + top-down 접근으로 가능하다고 힌트 받음. + dp[cur][visited](해당 노드)(방문비트마스크)
#### 2차 막힘. 재귀함수의 계산이 어느 위치에서 해야할 지 모르겠음.
#### 2차 해답 : Claude 활용 내가 접근한게 맞음. 메모이제이션을 왜쓰는거지?
#### 3차 의문. 모든 경우의 수를 돌아야하는데 출발점 1개만 하는거지?
#### 3차 해답 : 순환하는 가장 최소의 경우를 찾는 것이므로 어느 지점에서 출발하든 최소의 경우의 수는 같은 경로를 그리며 그 경로의 값은 같기 때문.
import sys
input = sys.stdin.readline
N = 0
W = []
dp = []
INF = float('inf')

import sys
input = sys.stdin.readline
N = 0
W = []
dp = []
INF = float('inf')

def find_min(cur:int, visited:int):
   if visited == ((1<< N)-1):
       return W[cur][0] if W[cur][0] > 0 else INF
   
   if dp[cur][visited] != -1:
       return dp[cur][visited]
   
   dp[cur][visited] = INF
   for next in range(N):
       if visited & (1 << next) or W[cur][next] == 0:
           continue
       dp[cur][visited] = min(
           dp[cur][visited],
           W[cur][next] + find_min(next, visited | (1 << next))
       )
   
   return dp[cur][visited]

def main():
   global N, W, dp
   N = int(input())
   W = [list(map(int, input().split())) for _ in range(N)]
   dp = [[-1] * (1 << N) for _ in range(N)]
   
   print(find_min(0, 1))

main()