# import sys

# input = sys.stdin.readline

# if __name__ == "__main__":
#     N = int(input())

#     info = [list(map(int, input().split())) for _ in range(N)]

#     info.sort(key=lambda x: (x[0], x[1]))

#     start_m = 3
#     start_d = 1
#     temp_end_m = 3
#     temp_end_d = 1

#     i = 0
#     cnt = 0
#     while True:
#         if (info[i][0] < start_m) or (info[i][0] == start_m and info[i][1] <= start_d):
#             if (temp_end_m < info[i][2]) or (
#                 info[i][2] == temp_end_m and info[i][3] > temp_end_d
#             ):
#                 temp_end_m = info[i][2]
#                 temp_end_d = info[i][3]
#                 i += 1
#                 if temp_end_m > 11:
#                     cnt += 1
#                     break
#             else:
#                 if (info[i][2] < start_m) or (
#                     info[i][2] == start_m and info[i][3] < start_d
#                 ):
#                     i += 1
#                     continue
#                 cnt += 1
#                 start_m = temp_end_m
#                 start_d = temp_end_d
#         else:
#             cnt += 1
#             start_m = temp_end_m
#             start_d = temp_end_d
#             if start_m > 11:
#                 cnt += 1
#                 break

#     print(cnt)

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    info = [list(map(int, input().split())) for _ in range(N)]

    info.sort(key=lambda x: (x[0], x[1]))

    start_m = 3
    start_d = 1
    temp_end_m = 3
    temp_end_d = 1

    i = 0
    cnt = 0
    while True:
        updated = False
        while i < N and (
            info[i][0] < start_m or (info[i][0] == start_m and info[i][1] <= start_d)
        ):
            if (temp_end_m < info[i][2]) or (
                info[i][2] == temp_end_m and info[i][3] > temp_end_d
            ):
                temp_end_m = info[i][2]
                temp_end_d = info[i][3]
                updated = True
            i += 1

        if not updated:
            # 더 이상 범위를 확장할 수 없는 경우
            print(0)
            break

        cnt += 1
        start_m = temp_end_m
        start_d = temp_end_d

        if start_m > 11:
            print(cnt)
            break
