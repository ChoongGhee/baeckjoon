import sys
import heapq
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    
    
    jewels = []
    for _ in range(N):
        M, V = map(int, input().split())

        if M > 100000000:
            N -= 1
            continue
        
        jewels.append((M, V))

    bags = []
    for _ in range(K):
        bags.append(int(input()))
    
    jewels.sort(reverse=True)
    bags.sort(reverse=True)

    max_hq = []
    sum_val = 0
    while bags:
        bag = bags.pop()
        while jewels:
            weight, cost = jewels.pop()
            if weight <= bag:
                heapq.heappush(max_hq,-cost)
            else:
                jewels.append((weight, cost))
                break
        if max_hq:
            sum_val -= heapq.heappop(max_hq)
            
    print(sum_val)

    
main()

