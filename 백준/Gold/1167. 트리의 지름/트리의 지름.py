import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline
info = []
maxx = 0

def dfs(parent:int, node:int)->int:
    global maxx
    if len(info[node]) == 1 and parent != 0: 
        return info[node][0][1]

    one, two = 0, 0
    vall = 0
    for child in info[node]:
   
        if child[0] == parent:
            vall += child[1]
            continue
        val = dfs(node, child[0])

        if one < val:
            two = one  # 기존의 최대값을 두 번째로 밀어냄
            one = val
        elif two < val:  # 단순히 두 번째 값 갱신
            two = val

    if maxx < (one+two):
        maxx = one+two
    

    return max(vall+one, vall+two)



def main():
    global info, maxx
    n = int(input())

    info = [[] for _ in range(n+1)]

    for i in range(n):
        temp = list(map(int, input().split()))
        now = 1
        while temp[now] != -1:
            info[temp[0]].append([temp[now], temp[now+1]])
            now += 2

    dfs(0,1)

    print(maxx)

main()