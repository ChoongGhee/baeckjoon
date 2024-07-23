import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    info.sort(key=lambda x: (x[1], x[0]))

    temp = []
    temp.append(info[0])
    cnt = 1
    for i in range(1, len(info)):
        if temp[0][1] <= info[i][0]:
            temp.append(info[i])
            temp.pop(0)
            cnt += 1

    print(cnt)
