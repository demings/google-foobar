memo = {}

def count(current_height, bricks_left):
    if bricks_left == 0:
        return 1

    if bricks_left < current_height:
        return 0

    key = current_height, bricks_left

    if key in memo:
        return memo[key]
    
    memo[key] = count(current_height + 1, bricks_left - current_height) + count(current_height + 1, bricks_left)
    return memo[key]

def solution(n):
    return count(1, n) - 1

print(solution(200) == 487067745)
print(solution(3) == 1)
print(solution(4) == 1)
print(solution(5) == 2)

print(solution(6) == 3)
print(solution(7) == 4)