import sys
input = sys.stdin.readline

def time_calculate(height: int) -> int:
    global b, info, n, m
    time = 0
    inventory = b

    for i in range(n):
        for j in range(m):
            if info[i][j] > height:
                # 블록을 제거하는 경우
                diff = info[i][j] - height
                time += diff * 2
                inventory += diff
            elif info[i][j] < height:
                # 블록을 쌓는 경우
                diff = height - info[i][j]
                time += diff
                inventory -= diff

    # 만약 인벤토리에 블록이 부족하면 불가능한 높이
    if inventory < 0:
        return float('inf')
    
    return time

if __name__ == "__main__":
    n, m, b = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    max_height = max(max(row) for row in info)
    min_height = min(min(row) for row in info)

    # 초기 값 설정
    time_btm = time_calculate(min_height)
    time_top = time_calculate(max_height)
    mid = (min_height + max_height + 1) // 2
    time_mid = time_calculate(mid)

    while True:
        mid_l, mid_r = (min_height + mid) // 2, (mid + max_height) // 2
        time_mid_l, time_mid_r = time_calculate(mid_l), time_calculate(mid_r)

        minimum = min(time_mid_l, time_mid, time_mid_r)

        # 조건에 따라 탐색 범위 축소
        if minimum == time_mid_r:
            if (min_height, mid, max_height) == (mid, mid_r, max_height):
                break
            min_height, mid, max_height = mid, mid_r, max_height
            time_btm, time_mid, time_top = time_mid, time_mid_r, time_top
        elif minimum == time_mid:
            if (min_height, mid, max_height) == (mid_l, mid, mid_r):
                break
            min_height, mid, max_height = mid_l, mid, mid_r
            time_btm, time_mid, time_top = time_mid_l, time_mid, time_mid_r
        else:
            if (min_height, mid, max_height) == (min_height, mid_l, mid):
                break
            min_height, mid, max_height = min_height, mid_l, mid
            time_btm, time_mid, time_top = time_btm, time_mid_l, time_mid

    # 최종 결과 출력
    if time_mid < time_top:
        print(time_mid, mid)
    else:
        print(time_top, max_height)