def solution(n, b):
    ids = []

    for _ in range(100):
        loop_count = get_loop_count(ids, n)

        if (loop_count != -1):
            return loop_count

        ids.append(n)

        x, y = get_x_y(n)
        n = get_z(x, y, len(n), b)

def get_x_y(n):
    return ''.join(sorted(list(n), reverse=True)), ''.join(sorted(list(n)))

def get_z(x, y, k, b):
    z = int(x, b) - int(y, b)
    chars = map(lambda x: str(x), number_to_base(z, b))
    z_base = str(''.join(chars))
    return "0" * (k - len(z_base)) + z_base

def number_to_base(n, b):
    if n == 0:
        return [0]

    digits = []

    while n:
        digits.append(int(n % b))
        n //= b

    return digits[::-1]

def get_loop_count(ids, current):
    count = 0

    for num in reversed(ids):
        count = count + 1
        if (num == current):
            return count

    return -1

print(solution('1211', 10) == 1)
print(solution('210022', 3) == 3)

# got 50% - not efficient enough? while loop duuh