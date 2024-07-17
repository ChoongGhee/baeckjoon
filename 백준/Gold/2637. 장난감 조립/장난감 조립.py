import sys
sys.setrecursionlimit(10**6)

def dfs(idx):
    if memo[idx] is not None:
        return memo[idx]
    
    if not info_table[idx]:  # 기본 부품인 경우
        memo[idx] = {idx: 1}
        return memo[idx]
    
    result = {}
    for next_part, quantity in info_table[idx]:
        sub_parts = dfs(next_part)
        for part, count in sub_parts.items():
            result[part] = result.get(part, 0) + count * quantity
    
    memo[idx] = result
    return result

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    info_table = [[] for _ in range(N + 1)]
    memo = [None] * (N + 1)

    for _ in range(M):
        X, Y, K = map(int, input().split())
        info_table[X].append((Y, K))

    result = dfs(N)

    for part in sorted(result.keys()):
        print(f"{part} {result[part]}")