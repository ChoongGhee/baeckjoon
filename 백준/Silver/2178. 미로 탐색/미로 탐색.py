import sys


def BFS(y: int, x: int) -> None:
    queue.append([y, x])

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 1:
                queue.append([ny, nx])
                matrix[ny][nx] = matrix[y][x] + 1


if __name__ == "__main__":

    input = sys.stdin.readline

    N, M = map(int, input().split())

    matrix = [list(map(int, input().strip())) for _ in range(N)]

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    queue = []

    BFS(0, 0)
    print(matrix[N - 1][M - 1])
