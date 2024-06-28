def closest_pair(points):
    points.sort()
    return min(((points[i], points[j]) for i in range(len(points) - 1) for j in range(i + 1, len(points))), key=lambda pair: abs(pair[0] - pair[1]))
