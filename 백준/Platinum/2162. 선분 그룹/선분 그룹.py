def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    if temp > 0: return 1
    elif temp < 0: return -1
    return 0

def check_intersection(line1, line2):
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
            return True
        return False
        
    return abc * abd <= 0 and cda * cdb <= 0

def solve(N, lines):
    parent = list(range(N))
    size = [1] * N
    
    # 모든 선분 쌍에 대해 교차 검사
    for i in range(N):
        for j in range(i+1, N):
            if check_intersection(lines[i], lines[j]):
                union(parent, size, i, j)
    
    # 그룹 수 계산
    groups = set(find(parent, i) for i in range(N))
    # 가장 큰 그룹의 크기 계산
    max_size = max(size)
    
    return len(groups), max_size

# 입력 처리
N = int(input())
lines = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((x1, y1, x2, y2))

# 결과 출력
group_count, max_group_size = solve(N, lines)
print(group_count)
print(max_group_size)