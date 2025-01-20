import sys
input = sys.stdin.readline

MOD = 1000000007
N = 8

adj = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1], 
    [0, 0, 0, 1, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 1, 0, 1], 
    [0, 0, 0, 0, 1, 0, 1, 0]  
]


def matrix_square(a:list, b:list)->list:
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= MOD
    return result

def matrix_times(matrix:list, B:int)->list:
    if B == 1:
        return [[x % MOD for x in row] for row in matrix]
    
    value = matrix_times(matrix, B // 2)
    if B % 2 == 0:
        return matrix_square(value, value)
    else:
        temp = matrix_square(value, value)
        return matrix_square(temp, matrix)

def main():
    D = int(input())
    result = matrix_times(adj, D)
    print(result[0][0])  

if __name__ == "__main__":
    main()