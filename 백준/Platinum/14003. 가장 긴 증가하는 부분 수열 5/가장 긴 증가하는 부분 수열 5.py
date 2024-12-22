import sys
input = sys.stdin.readline

def bsearch(L, target):
    start = 0
    end = len(L) - 1
    
    if not L or L[-1] < target:
        return len(L)
        
    while start < end:
        mid = (start + end) // 2
        if L[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

def main():
    N = int(input())
    info = list(map(int, input().split()))

    L = []  # LIS 길이 계산용
    P = []  # 각 원소의 L 내 위치

    # LIS 길이와 위치 구하기
    for val in info:
        pos = bsearch(L, val)
        if pos == len(L):
            L.append(val)
        else:
            L[pos] = val
        P.append(pos)
    
    # 실제 수열 구하기
    length = len(L)
    print(length)  # 길이 출력

    # 실제 수열 구하기를 최적화
    answer = []
    current_pos = length - 1  # 찾고자 하는 위치
    
    # 뒤에서부터 해당 위치의 가장 큰 값을 찾음
    for i in range(N-1, -1, -1):
        if P[i] == current_pos:
            answer.append(info[i])
            current_pos -= 1
            if current_pos < 0:
                break

    print(*answer[::-1])  # 한 번에 출력

main()