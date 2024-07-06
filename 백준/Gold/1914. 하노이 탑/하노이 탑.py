def hanoi(n, x, y, z):
        if n > 20:
             return 0
        if n==1 :
            print(x, y)
        
        else: 
            hanoi(n-1, x, z, y)
            print(x, y)
        
            hanoi(n-1, z, y, x)
 

        
n = int(input())

v = 1 # 패턴 1의 횟수

for i in range(1,n):
    d = v*2 + 1
    v = d

print(v)

hanoi(n, 1, 3, 2)
