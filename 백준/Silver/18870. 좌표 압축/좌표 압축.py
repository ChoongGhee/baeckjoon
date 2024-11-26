import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    info = []
    info_save = []

    idx = 0
    for i in map(int, input().split()):
        info.append(i)
        info_save.append([i, idx])
        idx+=1
    
    temp = sorted(info_save)

    idx = 0
    for i in range(len(temp)):
        a, b = temp[i]
        info[b] = idx
        if i < len(temp) - 1 and temp[i+1][0] != a:
            idx += 1
        
    print(*info)