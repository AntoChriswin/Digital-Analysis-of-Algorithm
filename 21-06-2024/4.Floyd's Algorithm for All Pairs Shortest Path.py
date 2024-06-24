INF = 99999

def floyd_warshall(graph):
    n = len(graph)
    dist = graph

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = [
    [0, 8, 7, 8],
    [9, 0, 11, 12],
    [10, 9, 0, 11],
    [8, 10, 11, 0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)
