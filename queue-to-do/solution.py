import functools

def my_solution(start, length):
    checksum = 0

    for i in range(length):
        row_start = start + i * length
        row_end = row_start + length - i - 1
        lol = get_row_xor(row_start, row_end), get_row_xor_2(row_start, row_end)
        checksum = checksum ^ get_row_xor(row_start, row_end)

    return checksum

def get_row_xor(start, end):
    return functools.reduce(lambda a, b: a ^ b, range(start, end + 1))

def get_row_xor_2(start, end):
    return XOR(end) ^ XOR(start)

# row_xor = XOR(row_start - 1) ^ XOR(row_end - 1)
# def XOR(n):
#     val = n % 4
#     if val == 0:
#         return n
#     if val == 1:
#         return 1
#     if val == 2:
#         return n + 1
#     return 0

# def solution(start, length):
#     current = start
#     checksum = 0

#     for i in range(length):
#         for j in range(length):
#             if length - j > i:
#                 checksum = checksum ^ current
#             current = current + 1

#     return checksum


def XOR(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0

def other_solution(start, length):
    if length == 1:
        return start

    first = start + 2*(length-1)
    checksum = XOR(first)

    if start > 1:
        checksum = checksum ^ XOR(start - 1)

    for i in range(length-2):
        elements = length - 2 - i
        current = start + length*(2 + i) - 1
        checksum = checksum ^ XOR(current) ^ XOR(current + elements)

    return checksum


# print(other_solution(0, 3) == 2)
print(other_solution(17, 4) == 14)

for i in range(1, 20):
    print(str(i) + " -> " + str(my_solution(0, i) == other_solution(0, i)))

# for i in range(1, 16):
#     print(str(i) + " -> " + str(get_row_xor(1, i)))
