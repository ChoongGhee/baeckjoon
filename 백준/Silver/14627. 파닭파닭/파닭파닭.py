import sys

input = sys.stdin.readline


def isok(offset: int):
    global s, c
    count = 0
    for i in range(s):
        count += info[i] // offset
    if count >= c:
        return 1
    else:
        return 0


if __name__ == "__main__":
    s, c = map(int, input().split())
    info = [int(input()) for _ in range(s)]

    start = 1
    end = max(info)

    while start <= end:
        mid = (start + end) // 2

        if isok(mid):
            start = mid + 1
            offset = mid
        else:
            end = mid - 1

    remain = 0
    cnt = 0

    for i in range(s):
        remain += info[i] % offset
        cnt += info[i] // offset

    remain += (cnt - c) * offset

    print(remain)
