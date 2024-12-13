def closest_numbers(A):
    A.sort()
    min_diff = float('inf')
    closest_pair = None
    for i in range(1, len(A)):
        diff = A[i] - A[i - 1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (A[i - 1], A[i])
    return closest_pair

A = [9, 4, 1, 6]
print(closest_numbers(A))
