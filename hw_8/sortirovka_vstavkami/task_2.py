def SelectionSort(A):
    n = len(A)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if A[j] > A[max_index]:
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
    return A

A = [1, 4, 2, 3, 4]
print(SelectionSort(A))
