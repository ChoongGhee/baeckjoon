import sys
input = sys.stdin.readline

def main():
    n = int(input())

    if n < 11:
        print(n)
        return
    
    cnt = 0
    num = 0
    while n != cnt-1:
        arr = list(map(int, str(num)))

        if num > 9876543210:
            print(-1)
            return
        
        for i in range(1, len(arr)):
            if arr[i-1] <= arr[i]:
                arr[i-1] += 1
                for j in range(i, len(arr)):
                    arr[j] = 0
                
                num = int(''.join(map(str, arr)))
                break
        else:
            cnt += 1
            num += 1
            
    print(num-1)

main()