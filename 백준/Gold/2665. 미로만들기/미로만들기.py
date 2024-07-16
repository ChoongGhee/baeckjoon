import sys
import heapq


class Node:
    def __init__(self, y, x, val):
        self.y = y
        self.x = x
        self.weight = 1 - val
        self.neighbors = []

        if y > 0:
            self.neighbors.append([y - 1, x])
        if x > 0:
            self.neighbors.append([y, x - 1])
        if y < N - 1:
            self.neighbors.append([y + 1, x])
        if x < N - 1:
            self.neighbors.append([y, x + 1])


def Dijkstra(y, x):
    q = [[0, y, x]]
    cost_table[0][0] = 0

    while q:
        cost, y, x = heapq.heappop(q)

        if cost_table[y][x] < cost:
            continue

        for ny, nx in node_matrix[y][x].neighbors:
            new_cost = cost + node_matrix[ny][nx].weight
            if new_cost < cost_table[ny][nx]:
                cost_table[ny][nx] = new_cost
                heapq.heappush(q, (new_cost, ny, nx))


if __name__ == "__main__":

    input = sys.stdin.readline

    INF = int(1e9)

    N = int(input())

    matrix = [list(map(int, input().strip())) for _ in range(N)]

    node_matrix = []
    cost_table = []
    for i in range(N):
        node_row = []
        for j in range(N):
            node = Node(i, j, matrix[i][j])
            node_row.append(node)

        cost_table.append(list([INF] * N))
        node_matrix.append(node_row)

    Dijkstra(0, 0)
    print(cost_table[N - 1][N - 1])
