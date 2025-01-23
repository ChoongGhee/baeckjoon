# 문제 1 : 그리디로 접근시 AA, BDB, A 이렇게 나누어짐, 하지만 결과는 A, ABDBA 로 2개로 하는 것이 올바름. 그리디는 그래서 못고침
# 해결 : DP로 접근하도록 해야함. dp[4]는 인덱스 3(즉, "AABD")까지의 최소 팰린드롬 분할 횟수 > So 이중 for문으로 그것을 확인함.
import sys
input =  sys.stdin.readline

def main():
    string = input().strip()
    n = len(string)
    
    is_palindrome = [[False] * n for _ in range(n)]
    
    # 길이 1인 경우 무조건 팰린드롬
    for i in range(n):
        is_palindrome[i][i] = True
    
    # 길이 2 이상의 경우 확인하는 것
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if length == 2:
                is_palindrome[start][end] = (string[start] == string[end])
            else:
                is_palindrome[start][end] = (string[start] == string[end] and 
                                           is_palindrome[start+1][end-1])
    
    # 분할 횟수를 계산하는 DP
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for j in range(i):
            if is_palindrome[j][i-1]:
                dp[i] = min(dp[i], dp[j] + 1)
    
    print(dp[n])

# def isPalindrome(arr:list)->bool:
#     left = 0
#     right = len(arr)-1
#     while left < right:
#         if arr[left] != arr[right]:
#             return False
#         left += 1
#         right -= 1
    
#     return True

# def main():
#     string = input().strip()
#     dp = [float('inf')] * (len(string) + 1)
#     dp[0] = 0
    
#     # i번째 요소 전 인덱스 까지 > dp[i] 값은 i-1 인덱스 까지의 팰린드롬 분할횟수
#     for i in range(1, len(string) + 1):
#         for j in range(i):
#             if isPalindrome(string[j:i]):
#                 dp[i] = min(dp[i], dp[j] + 1)
    
#     print(dp[-1])

# def main():
#     string = input().strip()  # strip() 추가
#     cnt = 0
#     i = 0
#     while i < len(string):
#         max_idx = i
#         for j in range(i, len(string)):
#             if isPalindrome(string[i:j+1]):
#                 max_idx = j
#         i = max_idx + 1
#         cnt += 1
#     print(cnt)

main()
