import sys


input = sys.stdin.readline

def compute_add_val(foot_position, next_position):
    if foot_position == 0:
        return 2
    elif foot_position == next_position:
        return 1
    elif abs(foot_position-next_position) == 2:
        return 4
    else:
        return 3
    
def main():
    input_arr = list(map(int, input().split()))

    dp = [[[4*len(input_arr) for _ in range(5)] for _ in range(5)]  for _ in range(len(input_arr))]

    dp[0][0][0] = 0

    for i in range(len(input_arr)-1):
        next_po = input_arr[i]
        for left in range(5):
            for right in range(5):
                dp[i+1][left][next_po] = min(dp[i+1][left][next_po], dp[i][left][right] + compute_add_val(right, next_po))
                dp[i+1][next_po][right] = min(dp[i+1][next_po][right], dp[i][left][right] + compute_add_val(left, next_po))

    print(min(map(min, dp[len(dp)-1])))

        
main()