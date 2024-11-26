import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start:int, pa_list:list)->list:
    if info[start] == 0:
        return pa_list

    pa_list.append(info[start])

    return dfs(info[start], pa_list)

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        n = int(input())

        info = [0] * (n+1)

        for j in range(n-1):
            parent, child = map(int, input().split())
            info[child] = parent
        
        a, b = map(int,input().split())

        a_pa_list = dfs(a, [a])
        b_pa_list = dfs(b, [b])

        short_list:list
        long_list:list

        # print(a_pa_list, b_pa_list)

        if len(a_pa_list) < len(b_pa_list):
            short_list = a_pa_list
            long_list = b_pa_list
        else:
            short_list = b_pa_list
            long_list = a_pa_list

        for k in short_list:
            for l in long_list:
                if k == l:
                    print(l)
                    break
            else:
                continue
            break
        


