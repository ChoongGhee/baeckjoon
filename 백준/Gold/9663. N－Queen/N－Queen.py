N = int(input())
result_num = 0
##행 검사 배열
flag_a = [False] * N
##대각선1 검사 배열
flag_b = [False] * (2 * N - 1)
##대각선2 검사 배열
flag_c = [False] * (2 * N - 1)


def queen(i):
    ##경우의 수를 저장할 변수를 사용하기 위해 전역 변수로 지정해준다.
    global result_num

    ##j만큼 반복한다.
    for j in range(N):
        ##해당 칸이 퀸을 놓을 수 있다면 실행하라
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j]:
            ##해당 칸이 퀸을 놓을 수 있으면서 마지막 행이라면 실행하라
            if i == (N - 1):
                ##경우의 수에 1 더하라
                result_num += 1
            ##마지막 행이 아니라면 퀸을 놓고 검사 조건에 포함후 다음 행으로
            else:
                ##검사 조건에 포함
                flag_a[j] = flag_b[i + j] = flag_c[i - j] = True

                ##다음 분기로 넘어가라
                queen(i + 1)
                ##포함 시켰던 검사 조건을 빼라
                flag_a[j] = flag_b[i + j] = flag_c[i - j] = False


##함수 실행
queen(0)

##경우의 수 출력
print(result_num)
