import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    position = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                position.append([matrix[i][j], i, j])
    position.sort()

    S, X, Y = map(int, input().split())

    q = position[:]  # 원본 리스트를 변경하지 않도록 복사

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    time = 0
    while time < S and q:  # q가 비어있지 않은 경우에만 반복
        next_q = []
        for idx, y, x in q:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 0:
                    matrix[ny][nx] = idx
                    next_q.append([idx, ny, nx])
        q = next_q
        time += 1

    print(matrix[X - 1][Y - 1])