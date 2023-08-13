'''
class DisjointSet
Description: This class implements the disjoint set data structure.
The disjoint set data structure is implemented using a forest of trees. Each
tree represents a set of connected cells. Each node in the tree represents a
cell. Each node has a parent pointer that points to the parent node. The root
node of each tree represents the set. The root node has a parent pointer that
points to itself. The disjoint set data structure has two operations: find and
union. The find operation returns the root node of the tree that contains the
given node. The union operation merges two trees into one tree by making the
root node of one tree point to the root node of the other tree.
'''
import random


class DisjointSet:

    def __init__(self, width, height):
        self.set_count = width * height
        self.parent_list = [i for i in range(self.set_count)]
        self.size_list = [1 for i in range(self.set_count)]
        self.width = width
        self.height = height
        self.color_list = [self.generate_random_hex_color()
                           for i in range(self.set_count)]

    def find(self, cell):
        '''
        Description: This function returns the root node of the tree that contains the given node.
        Parameters: cell - The cell.
        Return: The root node of the tree that contains the given node.
        '''
        # Find the root of the tree.
        root_index = (cell.y // 2) * self.width + (cell.x // 2)
        while root_index != self.parent_list[root_index]:
            root_index = self.parent_list[root_index]

        # Compress the path leading back to the root.
        current_node = (cell.y // 2) * self.width + (cell.x // 2)
        while current_node != root_index:
            parent_node = self.parent_list[current_node]
            self.parent_list[current_node] = root_index
            current_node = parent_node

        return root_index

    def union(self, cell1, cell2):
        '''
        Description: This function merges two trees into one tree by making the root node of one tree point to the root node of the other tree.
        Parameters: cell1 - The first cell.
                    cell2 - The second cell.
        '''
        # Find the roots and stop if they are already the same.
        root1 = self.find(cell1)
        root2 = self.find(cell2)
        if root1 == root2:
            return

        # Merge the smaller tree into the larger tree.
        if self.size_list[root1] < self.size_list[root2]:
            self.parent_list[root1] = root2
            self.size_list[root2] += self.size_list[root1]
        else:
            self.parent_list[root2] = root1
            self.size_list[root1] += self.size_list[root2]
        self.set_count -= 1

    def generate_random_hex_color(self):
        '''
        Description: This function generates a random hexadecimal color.
        Return: A random hexadecimal color.
        '''
        return '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
