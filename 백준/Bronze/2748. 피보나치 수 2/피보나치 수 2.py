import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    F = [0, 1]

    for i in range(2, N + 1):
        a = F[i - 2] + F[i - 1]
        F.append(a)

    print(F[N])
