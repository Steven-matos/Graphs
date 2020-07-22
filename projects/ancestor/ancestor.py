from util import Stack


def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    distance = 0
    s.push((starting_node, distance))

    visited = set()
    parent = (starting_node, distance)

    neighbor = get_neighbors(starting_node, ancestors)
    if len(neighbor) < 1:
        return -1

    while s.size():
        removed_tuple = s.pop()

        removed_parent = removed_tuple[0]

        distance = removed_tuple[1]
        if distance > parent[1]:
            parent = removed_tuple
        if distance == parent[1] and removed_parent < parent[0]:
            parent = removed_tuple
        if removed_parent not in visited:
            visited.add(removed_parent)
            for neighbor in get_neighbors(removed_parent, ancestors):
                s.push((neighbor, distance + 1))

    return parent[0]


def get_neighbors(node, ancestors):
    neighbors = []
    for ancestor in ancestors:
        if ancestor[1] == node:
            neighbors.append(ancestor[0])
    return neighbors
