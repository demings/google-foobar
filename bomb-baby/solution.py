def solution(x, y):
    M = int(x)
    F = int(y)
    generations = 0

    while True:
        if M == 1 and F == 1:
            return str(generations)
        elif M < 1 or F < 1:
            return 'impossible'

        if M == 1:
            generations = generations + F - 1
            F = 1
            continue

        if F == 1:
            generations = generations + M - 1
            M = 1
            continue

        if M > F:
            div, M = get_div_mod(M, F)
        else:
            div, F = get_div_mod(F, M)

        generations = generations + div

def get_div_mod(x, y):
    return x // y, x % y

print(solution('4', '7') == '4')
print(solution('2', '1') == '1')
print(solution('2', '4') == 'impossible')

print(solution('1', '1') == '0')
