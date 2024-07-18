import sys


def dfs(idx_y, idx_x, before_info):
    if idx_y >= N or idx_x >= M or before_info != matrix[idx_y][idx_x]:
        return
    elif visit[idx_y][idx_x] == False:
        visit[idx_y][idx_x] = True
        if matrix[idx_y][idx_x] == "-":
            dfs(idx_y, idx_x + 1, matrix[idx_y][idx_x])
        if matrix[idx_y][idx_x] == "|":
            dfs(idx_y + 1, idx_x, matrix[idx_y][idx_x])


if __name__ == "__main__":
    input = sys.stdin.readline

    N, M = map(int, input().split())

    # 판자 모양 행렬 데이터 받음
    matrix = [list(input().strip()) for _ in range(N)]

    # 방문 체크 테이블 생성
    visit = []
    for i in range(N):
        temp = []
        for j in range(M):
            temp.append(False)
        visit.append(temp)

    # 카운트
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == False:
                dfs(i, j, matrix[i][j])
                cnt += 1

    print(cnt)
