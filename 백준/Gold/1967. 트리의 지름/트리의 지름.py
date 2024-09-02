import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(idx, parent, sum) -> tuple:
    max_cost = sum
    max_idx = idx

    for next_idx, cost in info[idx]:
        if next_idx == parent:
            continue

        temp_idx, temp_cost = dfs(next_idx, idx, sum + cost)
        if max_cost < temp_cost:
            max_cost = temp_cost
            max_idx = temp_idx

    return max_idx, max_cost


if __name__ == "__main__":
    N = int(input())

    info = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        pa, ch, cost = map(int, input().split())
        info[pa].append([ch, cost])
        info[ch].append([pa, cost])

    long_idx, _ = dfs(1, -1, 0)

    _, max_val = dfs(long_idx, -1, 0)

    print(max_val)
