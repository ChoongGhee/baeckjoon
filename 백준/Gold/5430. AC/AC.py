import sys
import ast

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        fun = input()

        flag = False

        n = int(input())
        info = input()
        info = list(ast.literal_eval(info))

        cnt = 0
        for j in range(len(fun)):
            if fun[j] == "D":
                cnt += 1

        if cnt > n:
            print("error")
            continue

        for i in range(len(fun)):
            if flag == True and fun[i] == "R":
                flag = False
            elif flag == False and fun[i] == "R":
                flag = True
            elif (flag == True) and (fun[i] == "D"):
                info.pop(-1)
            elif (flag == False) and (fun[i] == "D"):
                info.pop(0)

        if flag == True:
            info = reversed(info)
            info = "[" + ",".join(map(str, info)) + "]"
            print(info)
        else:
            info = "[" + ",".join(map(str, info)) + "]"
            print(info)
