import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    string = input().strip()

    minus_split = string.split("-")

    if len(minus_split) == 1:
        sum1 = 0
        p_split = minus_split[0].split("+")
        for i in p_split:
            sum1 += int(i)
        print(sum1)
    else:
        sum = sum(map(int, minus_split[0].split("+")))

        for i in minus_split[1:]:
            p_split = i.split("+")
            p_sum = 0
            for j in p_split:
                p_sum += int(j)
            sum -= p_sum

        print(sum)
