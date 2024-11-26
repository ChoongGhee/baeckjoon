import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def dfs(y,x):
    info[y][x] = 0
    for i in range(8):
        ny = dy[i]  + y
        nx = dx[i] + x
        if (0 <= ny < h) and (0 <= nx < w) and (info[ny][nx] == 1):
            dfs(ny,nx)
   

if __name__ == "__main__":
    while True:
        T = input().strip()
        if T == "0 0":
            break

        w, h = map(int, T.split())
        
        info = []
        for i in range(h):
            info.append(list(map(int, input().split())))

        dx = [0,0,1,-1,1,-1,1,-1]
        dy = [1,-1,0,0,1,1,-1,-1]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if info[i][j] == 1:
                    dfs(i,j)
                    cnt +=1

        print(cnt)

    
