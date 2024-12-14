import sys
import heapq
input = sys.stdin.readline

def main():
    V, E = map(int, input().split())
    info = [[] for _ in range(V+1)]

    for _ in range(E):
        A, B, C = map(int, input().split())
        info[A].append([B, C])
        info[B].append([A, C])

    visi = [False] * (V + 1)
    visi[1] = True

    hq = []
    for next_node, cost in info[1]:
        heapq.heappush(hq, [cost, next_node])

    total = 0

    while hq:
        cur_cost, cur_node = heapq.heappop(hq)

        if visi[cur_node] == True:
            continue
        
        visi[cur_node] = True
        
        total += cur_cost
        for next_node, cost in info[cur_node]:
            if visi[next_node] == False:
                heapq.heappush(hq, [cost, next_node])

    print(total)

main()