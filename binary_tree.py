class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self. right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left), self._height(node.right))


def solution(tree):
    if len(tree) == 0:
        return 0
    nodes = [Node(value) for value in tree if value != -1]
    for index in range(1, len(nodes)):
        node = nodes[index]
        parent_index = (index - 1) // 2
        parent = nodes[parent_index]
        setattr(parent, "left" if index % 2 else "right", node)
    tree = Tree(nodes[0])
    return tree.height()


tree = [1, 2, 3, 4, -1, -1, -1]
assert solution(tree) == 3