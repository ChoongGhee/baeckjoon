import sys

input = sys.stdin.readline

if __name__ == "__main__":
    strr = input().strip()
    bomb = input().strip()

    bl = len(bomb)
    stack = []
    i = 0

    while i < len(strr):
        stack.append(strr[i])

        if len(stack) >= bl and "".join(stack[-bl:]) == bomb:
            del stack[-bl:]

        i += 1

    result = "".join(stack)

    if result == "":
        print("FRULA")
    else:
        print(result)
