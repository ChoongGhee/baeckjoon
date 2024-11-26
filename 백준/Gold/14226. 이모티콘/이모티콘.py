import sys
from collections import deque

input = sys.stdin.readline
INF = float("inf")

def main():
    s = int(input())

    q = deque([(0,1,0)])

    visi = set([1,0])

    while q:
        time, num, copy = q.popleft()

        if num == s:
            print(time)
            break

        if not (num, copy) in visi:
            visi.add((num, copy))
            new_copy = num

            del_num = num-1

            paste_num = num + copy

            time += 1
            
            q.append((time, del_num, copy))
            q.append((time, num, new_copy))
            q.append((time, paste_num, copy))
    
main()

