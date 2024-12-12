import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(info:list, visi:list, idx:int, cur_list:list, pos:dict)->int:
    if idx in pos:  
        return len(cur_list) - pos[idx]  
   
    if visi[idx]:
        return 0

    visi[idx] = True
    pos[idx] = len(cur_list)
    cur_list.append(idx)
    
    return dfs(info, visi, info[idx], cur_list, pos)  

def test():
    n = int(input())
    info = [0]
    info.extend(map(int, input().split()))
    
    visi = [False] * (n+1)
    anyone_no = n

    for i in range(1, n+1):
        if not visi[i]:
            anyone_no -= dfs(info, visi, i, [], {})
   
    print(anyone_no)

def main():
    T = int(input())
    for _ in range(T):
        test()

main()