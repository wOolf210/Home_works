def balance_sums(A):
    positive_sum = sum(x for x in A if x > 0)
    negative_sum = sum(x for x in A if x < 0)
    diff = abs(positive_sum) - abs(negative_sum)
    A.append(diff)
    return A, diff

A = [-3, -2, 1, 2, 3, 4]
result, new_elem = balance_sums(A)
print(result)
print(new_elem)
