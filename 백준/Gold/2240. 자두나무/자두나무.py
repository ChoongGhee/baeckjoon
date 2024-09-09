import sys


def dfs(sec: int, posi: int, mov: int, t: int, w: int, info: list, dp: list) -> int:
    if sec == t:
        return 0

    if mov > w:
        return -float("inf")

    if dp[sec][mov] != -1:
        return dp[sec][mov]

    score = 1 if info[sec] == posi else 0
    stay = dfs(sec + 1, posi, mov, t, w, info, dp) + score
    change = dfs(sec + 1, 3 - posi, mov + 1, t, w, info, dp) + score

    dp[sec][mov] = max(stay, change)
    return dp[sec][mov]


def main():
    input_func = sys.stdin.readline
    t, w = map(int, input_func().split())

    info = [0] * t
    for i in range(t):
        info[i] = int(input_func())

    dp = [[-1] * (w + 1) for _ in range(t)]

    result = max(dfs(0, 1, 0, t, w, info, dp), dfs(0, 2, 1, t, w, info, dp))
    print(result)


if __name__ == "__main__":
    main()
