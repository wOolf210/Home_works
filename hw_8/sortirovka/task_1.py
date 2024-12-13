def min_sum(N, prices):
    prices.sort(reverse=True)
    total = 0
    for i in range(0, N, 3):
        total += prices[i]
        if i + 1 < N:
            total += prices[i + 1]
    return total

N = 6
prices = [1, 5, 4, 3, 5, 7]
print(min_sum(N, prices))
