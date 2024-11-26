import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    info = list(map(int, input().split()))
    info.sort()

    left_idx = 0
    right_idx = len(info)-1
    min_sum = float('inf')
    min_l = info[0]
    min_r = info[-1]

    temp = info[left_idx] + info[right_idx]

    while left_idx < right_idx:

        temp = info[left_idx] + info[right_idx]
        if temp == 0:
            min_l = info[left_idx]
            min_r = info[right_idx]
            break
        
        if min_sum > abs(temp):
            min_sum = abs(temp)
            min_l = info[left_idx]
            min_r = info[right_idx]
        
        if temp > 0:
            right_idx -= 1
        else:
            left_idx += 1


    print(min_l, min_r)


    