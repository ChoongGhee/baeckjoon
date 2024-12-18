import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y, z = map(int, input().split())
        points.append((x, y, z, i))  # i는 원래 인덱스
    
    edges = []
    # x, y, z 각각 정렬해서 인접한 것들만 간선으로 추가
    for k in range(3):  # x,y,z 순서대로
        points.sort(key=lambda x: x[k])  # k번째 좌표 기준 정렬
        for i in range(N-1):
            edges.append((abs(points[i][k] - points[i+1][k]), points[i][3], points[i+1][3]))
    
    # 이제 모든 간선을 정렬
    edges.sort()
    
    # 크루스칼 수행
    parent = list(range(N))
    result = 0
    
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
    
    print(result)

main()