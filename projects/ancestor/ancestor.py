from util import Stack


def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push(starting_node)

    visited = set()
    parent = starting_node

    neighbor = get_neighbors(starting_node, ancestors)
    if len(neighbor) < 1:
        return -1

    while s.size():
        removed = s.pop()
        parent = removed
        if removed not in visited:
            visited.add(removed)
            for neighbor in get_neighbors(parent, ancestors):
                s.push(neighbor)

    return parent


def get_neighbors(node, ancestors):
    neighbors = []
    for ancestor in ancestors:
        if ancestor[1] == node:
            neighbors.append(ancestor[0])
    return neighbors
