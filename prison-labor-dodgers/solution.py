def solution(x, y):
    if (len(x) > len(y)):
        full = x
        missing = y
    else:
        full = y
        missing = x

    for num in full:
        if (num not in missing):
            return num

    raise Exception("Bad input")


print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]) == 6)
print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]) == -4)
