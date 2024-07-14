def DFS(idx):
    if visited[idx] == False:
        visited[idx] = True
        print(idx, end=" ")
        for i in range(len(arr[idx])):
            DFS(arr[idx][i])
    else:
        return


def BFS(idx):
    queue.append(idx)
    visited[idx] = False
    while queue:
        current = queue.pop(0)
        print(current, end=" ")

        for i in arr[current]:
            if visited[i] == True:
                visited[i] = False
                queue.append(i)


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    N, M, V = map(int, input().split())

    arr = [[] for _ in range(N + 1)]  # N+1 크기로 변경

    for _ in range(M):
        key, value = map(int, input().split())
        if 1 <= key <= N:  # 유효한 키 범위 확인
            arr[key].append(value)
        if 1 <= value <= N:  # 유효한 키 범위 확인
            arr[value].append(key)

    for i in range(1, N + 1):
        arr[i].sort()

    visited = [True] + [False] * N

    queue = []
    DFS(V)
    print()
    BFS(V)
