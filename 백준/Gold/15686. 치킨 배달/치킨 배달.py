import sys
import itertools

input = sys.stdin.readline


def all(M: int, two_test: list):
    it = itertools.combinations(two_test, M)
    min_sum = 99999
    for i in it:
        final_info = []
        for j in i:
            final_info.append(two_info[j])

        min_info = [100] * ocnt
        for i in range(ocnt):
            for j in range(M):
                min_info[i] = min(
                    min_info[i],
                    abs(one_info[i][0] - final_info[j][0])
                    + abs(one_info[i][1] - final_info[j][1]),
                )
        min_sum = min(min_sum, sum(min_info))

    print(min_sum)


if __name__ == "__main__":
    N, M = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(N)]
    one_info = []
    two_info = []
    tcnt = 0
    ocnt = 0
    for i in range(N):
        for j in range(N):
            if info[i][j] == 2:
                tcnt += 1
                two_info.append([i, j])
            elif info[i][j] == 1:
                ocnt += 1
                one_info.append([i, j])

    if M >= tcnt:
        min_info = [100] * ocnt
        for i in range(ocnt):
            for j in range(tcnt):
                min_info[i] = min(
                    min_info[i],
                    abs(one_info[i][0] - two_info[j][0])
                    + abs(one_info[i][1] - two_info[j][1]),
                )

        print(sum(min_info))
    else:
        two_test = range(len(two_info))

        all(M, two_test)
