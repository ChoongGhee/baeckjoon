import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

def bottom_up(target, memo, parent, time_table):
   if target in memo:
       return memo[target]
       
   if not parent[target]:
       return time_table[target]
       
   max_time = 0
   for prev_building in parent[target]:
       time = bottom_up(prev_building, memo, parent, time_table)
       max_time = max(max_time, time)
   
   total_time = max_time + time_table[target]
   memo[target] = total_time
   return total_time

def test():
   N, K = map(int, input().split())
   time_table = list(map(int, input().split()))

   parent = [[] for _ in range(N)]
   child = [[] for _ in range(N)]

   for _ in range(K):
       X, Y = map(int, input().split())
       X, Y = X-1, Y-1
       parent[Y].append(X)  
       child[X].append(Y)   

   W = int(input()) - 1  
   memo = {}
   
   print(bottom_up(W, memo, parent, time_table))

def main():
   T = int(input())
   for _ in range(T):
       test()

if __name__ == "__main__":
   main()