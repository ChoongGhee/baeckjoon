import heapq
import sys

input = sys.stdin.readline

max_value = 100000


def dstra(start, end):
    global distance

    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        next_node1 = node * 2
        if next_node1 <= (end + 1) and distance[next_node1] > dist:
            distance[next_node1] = dist
            heapq.heappush(q, (dist, next_node1))

        next_node2 = node + 1
        if next_node2 <= (end + 1) and distance[next_node2] > dist + 1:
            distance[next_node2] = dist + 1
            heapq.heappush(q, (dist + 1, next_node2))

        if node > 0:
            next_node3 = node - 1
            if distance[next_node3] > dist + 1:
                distance[next_node3] = dist + 1
                heapq.heappush(q, (dist + 1, next_node3))


if __name__ == "__main__":
    n, k = map(int, input().split())

    if k <= n:
        print(n - k)
        exit()
    else:
        distance = [max_value] * (k + 5)

    dstra(n, k)

    print(distance[k])
