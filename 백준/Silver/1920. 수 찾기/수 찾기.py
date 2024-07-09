n1 = int(input())

a = list(map(int, input().split()))

a.sort()

n2 = int(input())

m = list(map(int, input().split()))


def find(i):
    pl = 0
    pr = n1 - 1
    while True:
        pc = (pl + pr) // 2
        if a[pc] == m[i]:
            return 1

        elif a[pc] < m[i]:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            return 0


for i in range(n2):
    print(find(i))
