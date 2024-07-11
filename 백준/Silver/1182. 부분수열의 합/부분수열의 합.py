n, s = map(int, input().split())

arr = list(map(int, input().split()))

count = 0
sum = 0


def find_sum_DFS(idx):
    global count, sum

    sum += arr[idx]
    if idx < n - 1:
        find_sum_DFS(idx + 1)

    if sum == s:
        count += 1

    sum -= arr[idx]

    if idx < n - 1:
        find_sum_DFS(idx + 1)


find_sum_DFS(0)

print(count)
