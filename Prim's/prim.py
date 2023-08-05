import pprint
import random

DIRECTIONS_COUNT = 4


class Prim:
    # To create a Minimum Spanning Tree for square grid-like graph

    # Each node has four neighbors (boundary nodes are exceptions)
    TOP, LEFT, BOTTOM, RIGHT = range(DIRECTIONS_COUNT)

    def __init__(self, row_len):
        self.row_len = row_len
        self.total_nodes = row_len**2

    def generate_mst(self):
        mst = [[0] * DIRECTIONS_COUNT for _ in range(self.total_nodes)]
        to_visit = list(range(self.total_nodes))

        visited = [to_visit.pop(0)]

        while to_visit:
            edge = random.choice(self.edges_to_unvisited_nodes(visited))
            node, next_node = edge
            self.connect_nodes(mst, node, next_node)
            visited.append(next_node)
            to_visit.remove(next_node)

        return mst

    def edges_to_unvisited_nodes(self, visited):
        edges_pool = []
        for node in visited:
            neighbors = self.get_neighbours(node)
            unvisited_neighbors = [n for n in neighbors if n not in visited]
            edges_pool.extend([(node, n) for n in unvisited_neighbors])
        return edges_pool

    def get_neighbours(self, node):
        row, column = divmod(node, self.row_len)
        neighbors = []
        if row > 0:
            neighbors.append(node - self.row_len)
        if column > 0:
            neighbors.append(node - 1)
        if row < self.row_len - 1:
            neighbors.append(node + self.row_len)
        if column < self.row_len - 1:
            neighbors.append(node + 1)
        return neighbors

    def connect_nodes(self, mst, node, next_node):
        direction = self.get_neighbour_direction(node, next_node)
        mst[node][direction] = 1

        # Set the connection for the neighboring node as well.
        # The opposite side should also be marked.
        opposite_direction = (direction + 2) % 4
        mst[next_node][opposite_direction] = 1

    def get_neighbour_direction(self, node, next_node):
        diff = next_node - node
        if diff == -self.row_len:
            return self.TOP
        elif diff == -1:
            return self.LEFT
        elif diff == self.row_len:
            return self.BOTTOM
        elif diff == 1:
            return self.RIGHT


if __name__ == '__main__':
    n = DIRECTIONS_COUNT
    prim = Prim(n)
    pprint.pp(prim.generate_mst())
