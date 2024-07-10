n, min_take = map(int, input().split())
tree = list(map(int, input().split()))
# 내림차순 정렬
tree.sort(reverse=True)

# 내림차로 정렬된 나무들의 차이 리스트
offset = [tree[i] - tree[i + 1] for i in range(len(tree) - 1)]
# 마지막 나무 높이 추가 (마지막 나무 - 지면(0m))
offset.append(tree[-1])


def find_max_height():
    sum = 0
    for startidx in range(len(offset)):
        if offset[startidx] * (startidx + 1) + sum >= min_take:
            # 조건이 만족하면 남은 부분을 계산
            remaining = min_take - sum
            # offset값 기준으로 자를 위치 계산(올림으로 최소의 M을 만족시킴)
            cut = (remaining + startidx) // (startidx + 1)
            # 자른 위치 반환
            return tree[startidx] - cut
        # 자른 총량 계산
        sum += offset[startidx] * (startidx + 1)
    # 나무를 다 자랐음에도 min_take가 만족하지 않았으면 0반환
    return 0


result = find_max_height()
print(result)