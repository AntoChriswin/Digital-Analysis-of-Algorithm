def knapsack_greedy(values, weights, capacity):
    n = len(values)
    index = list(range(n))
    ratio = [v/w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*n

    for i in index:
        if weights[i] <= capacity:
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            fractions[i] = capacity / weights[i]
            max_value += values[i] * fractions[i]
            break

    return max_value

values = [80, 70, 50, 80]
weights = [40, 30, 20, 30]
capacity = 100

print("Maximum value that can be obtained:", knapsack_greedy(values, weights, capacity))
