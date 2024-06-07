def generate_pascals_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 2))

num_rows = 5
pascals_triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(pascals_triangle)
