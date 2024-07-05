n =int(input())

for i in range(n):
    R, S = input().split()
    R = int(R)
    
    result =''
    for char in S:
        result += char * R
    
    print(result)