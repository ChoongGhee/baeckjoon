import sys

def DFS(test_arr, test_visited, before_table, idx, before_color):
    test_visited[idx] = True
    before_table[idx] = not before_color

    for i in test_arr[idx]:
        if not test_visited[i]:
            if DFS(test_arr, test_visited, before_table, i, not before_color) == -1:
                return -1
        elif before_table[i] == before_table[idx]:
            return -1
    return 0

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline

    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        arr = [[] for _ in range(V + 1)]

        for _ in range(E):
            key, value = map(int, input().split())
            arr[key].append(value)
            arr[value].append(key)

        visited = [False] * (V + 1)
        before_table = [None] * (V + 1)

        is_bipartite = True
        for i in range(1, V + 1):
            if not visited[i]:
                if DFS(arr, visited, before_table, i, False) == -1:
                    is_bipartite = False
                    break

        print("YES" if is_bipartite else "NO")