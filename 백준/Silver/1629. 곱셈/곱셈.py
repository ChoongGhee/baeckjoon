A, B, C = map(int, input().split())


def times(A, B, C):
    if B == 1:
        return A % C

    elif B > 1:
        value = times(A, B // 2, C)

        if B % 2 == 0:
            return (value * value) % C
        else:
            return (value * value * A) % C


print(times(A, B, C))
