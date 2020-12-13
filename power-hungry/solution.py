import functools

def solution(xs):
    positive = []
    negative = []

    for num in xs:
        if (num > 0):
            positive.append(num)
        elif (num < 0):
            negative.append(num)

    if (len(negative) % 2 > 0 and len(xs) > 1):
        negative.remove(min(map(lambda x: x * -1, negative)) * -1)
    
    if (len(positive) == 0 and len(negative) == 0):
        return "0"

    power = functools.reduce(lambda a, b: a * b, positive + negative)
    return str(power)

print(solution([2, 0, 2, 2, 0]) == "8")
print(solution([-2, -3, 4, -5]) == "60")
print(solution([0]) == "0")
print(solution([0, 0, -2, 0]) == "0")
print(solution([2]) == "2")
print(solution([-1]) == "-1")
print(solution([2, -2]) == "2")
print(solution([2, -2, -2]) == "8")
