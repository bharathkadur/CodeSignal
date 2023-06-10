def solution(n):
    factors_dict = create_factors_dict_below_n(n)
    new_dict = create_new_dictionary(factors_dict)
    return find_largest_value(new_dict)
     
def create_factors_dict_below_n(n):
    factors_dict = {}
    for num in range(1, n+1):
        factors_count = 0
        for i in range(1, num+1):
            if num % i == 0:
                factors_count += 1
        factors_dict[num] = factors_count
    return factors_dict

import itertools
def create_new_dictionary(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        count = 0
        for val in itertools.islice(dictionary.values(), key-1):
            if val > value:
                count += 1
        new_dict[key] = count
    return new_dict

def find_largest_value(dictionary):
    largest_value = max(dictionary.values())
    occurrence_count = list(dictionary.values()).count(largest_value)
    return [largest_value, occurrence_count]
