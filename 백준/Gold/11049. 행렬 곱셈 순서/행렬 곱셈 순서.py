import sys
input = sys.stdin.readline

def matrix_chain():
    N = int(input())
    
    if N == 1:
        print(0)
        return
        
    # 행렬 정보 저장
    arr = [0] * (N+1)
    for i in range(N):
        r, c = map(int, input().split())
        arr[i] = r
        if i == (N-1):
            arr[i+1] = c
            
    # dp[i][j]: i부터 j까지 행렬을 곱하는데 필요한 최소 연산 횟수
    dp = [[0] * N for _ in range(N)]
    
    # 구간 길이 (2부터 N까지)
    for diagonal in range(1, N):
        # 시작점 i
        for i in range(N - diagonal):
            j = i + diagonal
            dp[i][j] = float('inf')
            # 분할점 k
            for k in range(i, j):
                dp[i][j] = min(dp[i][j],
                             dp[i][k] + dp[k+1][j] + arr[i] * arr[k+1] * arr[j+1])
    
    print(dp[0][N-1])

matrix_chain()