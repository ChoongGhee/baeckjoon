import sys
from itertools import permutations

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())

    nums = list(map(int, input().split()))
    nums.sort()

    perm = permutations(nums, m)

    for i in perm:
        print(*i)

main()