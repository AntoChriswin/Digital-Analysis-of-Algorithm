import sys

def tsp(graph, start):
    n = len(graph)
    all_vertices = set(range(n))
    memo = {}

    def tsp_helper(curr, remaining):
        if (curr, remaining) in memo:
            return memo[(curr, remaining)]

        if not remaining:
            return graph[curr][start]

        min_cost = sys.maxsize
        for next_vertex in remaining:
            new_remaining = remaining - {next_vertex}
            cost = graph[curr][next_vertex] + tsp_helper(next_vertex, new_remaining)
            min_cost = min(min_cost, cost)

        memo[(curr, remaining)] = min_cost
        return min_cost

    return tsp_helper(start, all_vertices - {start})

# Example graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_vertex = 0
min_cost = tsp(graph, start_vertex)
print(f"Minimum cost for the Travelling Salesman Problem starting at vertex {start_vertex}: {min_cost}")
