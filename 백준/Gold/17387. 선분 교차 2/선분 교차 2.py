import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    if temp > 0: return 1
    elif temp < 0: return -1
    return 0

def check_intersection(line1, line2)->int:
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    
    abc = ccw(x1, y1, x2, y2, x3, y3)
    abd = ccw(x1, y1, x2, y2, x4, y4)
    cda = ccw(x3, y3, x4, y4, x1, y1)
    cdb = ccw(x3, y3, x4, y4, x2, y2)
    
    # 일직선 상에 있는 경우 추가 검사
    if abc * abd == 0 and cda * cdb == 0:
        # 각 선분의 x, y 범위가 겹치는지 확인
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and \
           min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1
        return 0
        
    return int(abc * abd <= 0 and cda * cdb <= 0)


def main():
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))

    print(check_intersection(line1, line2))

if __name__ == "__main__":
    main()