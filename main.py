def find_single_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
A = [1, 2, 2, 3, 1]
print(find_single_occurrence(A))
A = [1, 2, 2]
print(find_single_occurrence(A))
