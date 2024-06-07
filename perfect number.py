def is_perfect(num):
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num

def find_perfect_numbers(limit):
    perfect_numbers = [num for num in range(1, limit) if is_perfect(num)]
    return perfect_numbers

limit = 10000
perfect_nums = find_perfect_numbers(limit)
print("Perfect numbers up to", limit, "are:", perfect_nums)
