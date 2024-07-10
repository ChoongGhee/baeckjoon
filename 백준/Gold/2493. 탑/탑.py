n = int(input())
towers = list(map(int, input().split()))

stack = []
result = [0] * n

for i in range(n):
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    
    if stack:
        result[i] = stack[-1] + 1
    
    stack.append(i)

print(*result)