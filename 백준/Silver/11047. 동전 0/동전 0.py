import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())

    coin_table = [int(input()) for _ in range(N)]

    i = N - 1
    count = 0
    while i > -1:
        if K == 0:
            break
        if K // coin_table[i] >= 1:
            count += K // coin_table[i]
            K = K % coin_table[i]
            i -= 1
        else:
            i -= 1

    print(count)
