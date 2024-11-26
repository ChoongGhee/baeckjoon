import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, p =map(int, input().split())


    cnt = 0
    sta = [[0] for _ in range(7)]

    for i in range(n):
        line, plet = map(int, input().split())
        
        if sta[line][-1] < plet:
            cnt +=1
            sta[line].append(plet)

        elif sta[line][-1] > plet:
            while sta[line][-1] > plet:
                sta[line].pop()
                cnt += 1

            if sta[line][-1] < plet:
                cnt += 1
                sta[line].append(plet)

    print(cnt)
