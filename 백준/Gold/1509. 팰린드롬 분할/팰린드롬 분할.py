import sys
input =  sys.stdin.readline

def main():
   string = input().strip()
   n = len(string)
   
   dp = [float('inf')] * (n + 1)
   dp[0] = 0
   
   is_palindrome = [[False] * n for _ in range(n)]
   
   # 길이 1, 2 초기화
   for i in range(n):
       is_palindrome[i][i] = True
       if i < n-1:
           is_palindrome[i][i+1] = string[i] == string[i+1]
           
   # 길이 3 이상 팰린드롬 체크
   for length in range(3, n + 1):
       for start in range(n - length + 1):
           end = start + length - 1
           is_palindrome[start][end] = string[start] == string[end] and is_palindrome[start+1][end-1]
   
   # 최소 분할 횟수
   for i in range(1, n + 1):
       if is_palindrome[0][i-1]:
           dp[i] = 1
       else:
           for j in range(1, i):
               if is_palindrome[j][i-1]:
                   dp[i] = min(dp[i], dp[j] + 1)
                   
   print(dp[n])

main()