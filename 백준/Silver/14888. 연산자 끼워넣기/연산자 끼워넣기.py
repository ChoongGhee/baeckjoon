import sys


def dfs(num, current_result):
    global min_a, max_a

    if num == N:
        min_a = min(min_a, current_result)
        max_a = max(max_a, current_result)
        return

    for i in range(4):
        if operaters[i] > 0:
            operaters[i] -= 1

            if i == 0:
                dfs(num + 1, current_result + number[num])
            elif i == 1:
                dfs(num + 1, current_result - number[num])
            elif i == 2:
                dfs(num + 1, current_result * number[num])
            else:
                dfs(num + 1, int(current_result / number[num]))

            operaters[i] += 1


if __name__ == "__main__":

    input = sys.stdin.readline

    ######## 인풋
    N = int(input())
    number = list(map(int, input().split()))
    operaters = list(map(int, input().split()))

    min_a = 1e10
    max_a = -1e10

    dfs(1, number[0])

    print(max_a)
    print(min_a)
