n, k = map(int, input().split())
arr = list(range(1, n + 1))
index = 0
result = []

while True:
    if len(arr) == 0:
        break

    # 원형으로 이동
    index = (index + k - 1) % len(arr)

    # 현재 위치의 원소 출력 및 제거
    removed = arr.pop(index)
    result.append(str(removed))

    # 배열이 비어있지 않은 경우에만 index 조정
    if arr:
        index = index % len(arr)

# 결과 출력
print("<" + ", ".join(result) + ">")
