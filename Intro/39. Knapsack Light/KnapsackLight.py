def solution(value1, weight1, value2, weight2, maxW):
    # Initialize variables to track maximum values
    max_value1 = 0
    max_value2 = 0
    max_value_combined = 0

    # Check if the first item can be included
    if weight1 <= maxW:
        max_value1 = value1

    # Check if the second item can be included
    if weight2 <= maxW:
        max_value2 = value2

    # Check if both items can be included
    if weight1 + weight2 <= maxW:
        max_value_combined = value1 + value2

    # Return the maximum value
    return max(max_value1, max_value2, max_value_combined)
