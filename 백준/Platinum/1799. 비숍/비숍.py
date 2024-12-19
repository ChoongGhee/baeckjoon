import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
wall = [list(map(int, input().split())) for _ in range(N)]

max_bishops = 0  
flag_b = [False] * (2 * N - 1)  # i+j
flag_c = [False] * (2 * N - 1)  # i-j

def get_possible_count(pos):  # pos는 현재 우상향 대각선 번호
    able = 0
    for diag in range(pos, 2 * N - 1):  # 현재 대각선부터 마지막 대각선까지
        for y in range(diag + 1):
            x = diag - y
            if 0 <= y < N and 0 <= x < N and wall[y][x] and not flag_c[x - y + N-1]:
                able += 1
                break
    return able

def bishop(pos, cnt):  # pos는 현재 우상향 대각선 번호
    global max_bishops
    
    if pos == 2 * N:  # 2*N-1이 아닌 2*N에서 종료
        max_bishops = max(max_bishops, cnt)
        return

    if cnt + get_possible_count(pos) <= max_bishops:
        return
        
    # 현재 우상향 대각선에서 가능한 모든 위치 확인
    for y in range(pos + 1):
        x = pos - y
        if 0 <= y < N and 0 <= x < N:
            if wall[y][x] and not flag_b[pos] and not flag_c[x - y + N-1]:
                flag_b[pos] = True
                flag_c[x - y + N-1] = True
                bishop(pos + 1, cnt + 1)
                flag_b[pos] = False
                flag_c[x - y + N-1] = False
    
    bishop(pos + 1, cnt)

bishop(0, 0)
print(max_bishops)