import sys

input = sys.stdin.readline


def find(parents_table, x) -> int:
    if parents_table[x] != x:
        parents_table[x] = find(parents_table, parents_table[x])
    return parents_table[x]


def union(parents_table, a, b):
    a = find(parents_table, a)
    b = find(parents_table, b)
    if a < b:
        parents_table[b] = a
    else:
        parents_table[a] = b


V, E = map(int, input().split())

cost_arr = []

for _ in range(E):
    a, b, c = map(int, input().split())
    cost_arr.append([c, a, b])


cost_arr.sort()
parents_table = [0] * (V + 1)
for i in range(1, V + 1):
    parents_table[i] = i

total_cost = 0

for i in range(E):
    cost, a, b = cost_arr[i]

    if find(parents_table, a) != find(parents_table, b):
        union(parents_table, a, b)
        total_cost += cost

print(total_cost)
