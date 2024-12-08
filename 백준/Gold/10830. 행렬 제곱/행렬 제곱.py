import sys 
input = sys.stdin.readline
N = 0

def matrix_times(matrix:list, B)->list:
    if B == 1:
        for row in range(N):
            for column in range(N):
                matrix[row][column] %= 1000
        return matrix

    value = matrix_times(matrix, B // 2)
    if B % 2 == 0:
        return matrix_square(value, value)  
    else:
        temp = matrix_square(value, value)  
        return matrix_square(temp, matrix)

def matrix_square(matrix1:list, matrix2:list)->list:
    global N
    result = [[0] * N for _ in range(N)]  
    
    for row in range(N):
        for column in range(N):
            for k in range(N):
                result[row][column] += matrix1[row][k] * matrix2[k][column]
            result[row][column] %= 1000
    
    return result
    
def main():
    global N
    N, B = map(int, input().split())

    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    result = matrix_times(matrix, B)

    for i in result:
        print(*i)
   
main()