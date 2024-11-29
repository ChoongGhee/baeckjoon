import sys 
input = sys.stdin.readline

def main():
    A = int(input())
    B = int(input())
    C = int(input())

    strr = str(A*B*C)
    arr = [0] * 10
    for i in strr:
        arr[int(i)] += 1
    
    for j in arr:
        print(j)

main()