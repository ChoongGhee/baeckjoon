import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        a, b = map(int, input().split())
        print(a + b)
