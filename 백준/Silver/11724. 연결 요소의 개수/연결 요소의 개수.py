def DFS(idx):
    if visited[idx] == False:
        visited[idx] = True

        for i in range(len(arr[idx])):
            DFS(arr[idx][i])
    else:
        return


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    N, V = map(int, input().split())

    # 무향 그래프의 인접리스트 생성
    arr = [[] for _ in range(N + 1)]  # N+1 크기로 변경

    for i in range(V):
        key, value = map(int, input().split())
        arr[key].append(value)
        # if 1 <= value <= N:  # 유효한 키 범위 확인
        arr[value].append(key)

    for i in range(1, N + 1):
        arr[i].sort()

    # 부모 테이블 생성
    # parents_table = [0] * (N + 1)

    # for i in range(1, N + 1):
    #     parents_table[i] = i

    visited = [True] + [False] * N

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == False:
            DFS(i)
            cnt += 1

    print(cnt)
