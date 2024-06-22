def container_loading(items, container_capacity):
    items.sort(reverse=True)
    containers = [[] for _ in range(len(items))]

    for item in items:
        for container in containers:
            if sum(container) + item <= container_capacity:
                container.append(item)
                break
        else:
            containers.append([item])

    return containers


# Example
items = [3, 2, 5, 7, 1, 4, 8]
container_capacity = 10
loaded_containers = container_loading(items, container_capacity)
print(loaded_containers)
