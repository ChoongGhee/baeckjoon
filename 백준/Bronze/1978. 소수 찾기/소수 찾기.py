n = int(input())
numbers = list(map(int, input().split()))

count = len(numbers)

for i in range(n):
    if numbers[i] <= 1:
        count -= 1
        continue
    
    for j in range(2,numbers[i]):
        if (numbers[i] % j) == 0:
            count -= 1
            break
    
print(count)