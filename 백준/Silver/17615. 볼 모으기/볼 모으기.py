import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    string = input().strip()

    r_r_cnt = string[: string.rfind("B")].count("R")

    r_l_cnt = string[string.find("B") :].count("R")

    b_r_cnt = string[: string.rfind("R")].count("B")

    b_l_cnt = string[string.find("R") :].count("B")

    print(min(r_r_cnt, r_l_cnt, b_l_cnt, b_r_cnt))
