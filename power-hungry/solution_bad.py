import functools

def solution(xs):
    positive = []
    negative = []
    removed = False

    for num in xs:
        if (num > 0):
            positive.append(num)
        elif (num < 0):
            negative.append(num)
        else:
            removed = True

    if (len(negative) % 2 > 0):
        negative = remove_abs_min(negative, True)
        removed = True

    if (not removed):
        positive, negative = remove_lowest_value(positive, negative)

    if (len(positive) == 0 and len(negative) == 0):
        return "0"

    power = functools.reduce(lambda a, b: a * b, positive + negative)
    return str(power)

def remove_abs_min(array, negative_nums):
    min_value = min(map(lambda x: abs(x), array))

    if (negative_nums):
        min_value = min_value * -1

    array.remove(min_value)
    return array

def remove_lowest_value(positive, negative):
    if (len(negative) == 0):
        return remove_abs_min(positive, False), negative

    if (len(positive) == 0):
        negative = remove_abs_min(negative, True)
        return positive, remove_abs_min(negative, True)

    first_min = max(negative)
    negative_copy = negative.copy()
    negative_copy.remove(first_min)
    second_min = max(negative_copy)

    if (min(positive) > first_min * second_min):
        negative = remove_abs_min(negative, True)
        return positive, remove_abs_min(negative, True)

    return remove_abs_min(positive, False), negative


print(solution([2, 0, 2, 2, 0]) == "8")
print(solution([-2, -3, 4, -5]) == "60")
print(solution([-2, -3, -6]) == "18")
print(solution([2, 3, 6]) == "18")
print(solution([8, 9, -2, -3]) == "72")
print(solution([2, 8, -2, -3]) == "48")
print(solution([-2, -2, -3, -6]) == "18")
print(solution([0]) == "0")
print(solution([2]) == "0")
print(solution([-1]) == "0")
print(solution([2, -2]) == "2")
print(solution([2, -2, -2]) == "4")
