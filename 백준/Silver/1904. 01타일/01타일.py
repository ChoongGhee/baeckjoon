N = int(input())
F = [1, 1]

for i in range(2, N + 1):
    a = F[i - 2] + F[i - 1]
    F.append(a % 15746)

print(F[N])
