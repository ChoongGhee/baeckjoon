import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    info = [int(input()) for _ in range(n)]

    stack = [0]

    result = []
    start = 1

    arr = []
    i = 0
    while info != result:
        if info[i] != stack[-1]:
            stack.append(start)
            start += 1
            arr.append("+")
        else:
            result.append(stack.pop(-1))
            i += 1
            arr.append("-")

        if start > n + 1:
            print("NO")
            exit()

    for i in arr:
        print(i)
