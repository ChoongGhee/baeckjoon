import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    sequence = list(map(int, input().split()))

    check = list(set(sequence))
    check.sort()

    lcs_list = [[0 for _ in range(len(sequence) + 1)] for i in range(len(check) + 1)]

    for i in range(1, len(check) + 1):
        for j in range(1, len(sequence) + 1):
            if check[i - 1] == sequence[j - 1]:
                lcs_list[i][j] = lcs_list[i - 1][j - 1] + 1
            else:
                lcs_list[i][j] = max(lcs_list[i - 1][j], lcs_list[i][j - 1])

    print(lcs_list[-1][-1])
