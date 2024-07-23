import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    T = int(input())

    for i in range(T):
        N = int(input())

        recruits = []
        for _ in range(N):
            recruits.append(list(map(int, input().split())))

        recruits.sort()

        check = recruits[0][1]
        cnt = 1
        for i in range(1, N):
            if check > recruits[i][1]:
                check = recruits[i][1]
                cnt += 1
            elif check == 1:
                break
        print(cnt)
