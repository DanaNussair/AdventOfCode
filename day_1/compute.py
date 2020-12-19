import sys
from functools import reduce
from .data import arr

# Part #1
print("Part 1:")
def two_num_sum(requested_sum):
    obj = {n: i for (i, n) in enumerate(arr)}
    for index, num in enumerate(arr):
        if requested_sum - num in obj and index != obj.get(requested_sum - num):
            return [num, requested_sum - num]
    return False

two_numbers = two_num_sum(2020)
multiplied = reduce(lambda a, b: a * b, two_numbers)
print("Two Numbers: ", two_numbers)
print("Multiplied: ", multiplied)


#############################
# Part #2
print("Part 2")
def three_num_sum(requested_sum):
    for number in arr:
        two_numbers = two_num_sum(requested_sum - number)
        if two_numbers:    
            return [number] + two_numbers

three_numbers = three_num_sum(2020)
multiplied = reduce(lambda a, b: a * b, three_numbers)
print("Three Numbers", three_numbers)
print("Multiplied: ", multiplied)
