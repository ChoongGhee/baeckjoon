n, min_take = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort(reverse=True)

offset = [tree[i] - tree[i + 1] for i in range(len(tree) - 1)]
offset.append(tree[-1])  # 마지막 나무의 전체 높이를 추가


def find_max_height():
    sum = 0
    for startidx in range(len(offset)):
        if offset[startidx] * (startidx + 1) + sum >= min_take:
            remaining = min_take - sum
            cut = (remaining + startidx) // (startidx + 1)
            return tree[startidx] - cut
        sum += offset[startidx] * (startidx + 1)
    return 0  # 모든 나무를 다 잘라도 목표량에 도달하지 못한 경우


result = find_max_height()
print(result)
