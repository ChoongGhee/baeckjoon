import sys

if __name__ == "__main__":
    K = int(input())
    coin_num_table = []
    coin_info_table = []
    cost_table = []

    for _ in range(K):
        coin_num_table.append(int(input()))
        coin_info_table.append(list(map(int, input().split())))
        cost_table.append(int(input()))

    for i in range(K):
        cnt = 0
        count_num = [1] + [0] * (cost_table[i])
        for j in coin_info_table[i]:
            for k in range(1, cost_table[i] + 1):
                if k >= j:
                    count_num[k] += count_num[k - j]
        print(count_num[cost_table[i]])
