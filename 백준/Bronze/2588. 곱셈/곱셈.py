import sys

input = sys.stdin.readline
if __name__ == "__main__":

    a = int(input())
    b = input()

    for i in range(2, -1, -1):
        print(a * int(b[i]))

    print(a * int(b))
