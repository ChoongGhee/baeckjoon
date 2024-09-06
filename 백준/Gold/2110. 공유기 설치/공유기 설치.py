import sys

input = sys.stdin.readline


def isok(offset: int) -> bool:
    global c, N
    count = 1
    prev = info[0]

    for i in range(1, N):
        if info[i] - prev >= offset:
            count += 1
            prev = info[i]
            if count == c:
                return True
    return False


if __name__ == "__main__":
    N, c = map(int, input().split())
    info = []
    for i in range(N):
        info.append(int(input()))

    info.sort()

    # if c == 2:
    #     print(info[1] - info[0])
    #     exit()

    start = 1
    end = info[-1]

    while start <= end:
        mid = (start + end) // 2

        if isok(mid):
            start = mid + 1
            offset = mid
        else:
            end = mid - 1

    print(offset)
