import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())

    info = list(map(int, input().split()))

    check = []
    check.append(info.pop(0))

    while len(check) != N and info:
        if info[0] not in check:
            check.append(info.pop(0))
        else:
            info.pop(0)

    cnt = 0

    while info:
        if info[0] in check:
            info.pop(0)
        else:
            temp = 0
            idx = 0
            found = False
            for i in range(len(check)):
                if check[i] not in info:
                    check[i] = info.pop(0)
                    cnt += 1
                    found = True
                    break
                else:
                    if temp < info.index(check[i]):
                        temp = info.index(check[i])
                        idx = i

            if not found and info:
                check[idx] = info.pop(0)
                cnt += 1

    print(cnt)
