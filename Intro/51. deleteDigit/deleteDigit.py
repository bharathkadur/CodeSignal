from itertools import combinations

def solution(n):
    digits = str(n)
    combinations_list = list(combinations(digits, len(digits) - 1))
    max_num = max(int(''.join(comb)) for comb in combinations_list)
    return max_num
