import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n, h = map(int, input().split())

    h1_info = [0] *(h+1)
    h2_info = [0] *(h+1)

    for i in range(n):
        height = int(input())
        if i % 2 == 0:
            h1_info[height] += 1
        else:
            h2_info[height] += 1

    h_ = [0] * (h+1)

    h_[1] = sum(h1_info[1:]) + h2_info[h]

    for j in range(2,h+1):
        h_[j] = h_[j-1] - h1_info[j-1] +h2_info[h-j+1]

    min_val = min(h_[1:])
    print(min_val, h_[1:].count(min_val))
