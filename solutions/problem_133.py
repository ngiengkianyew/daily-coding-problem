class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.val)


def inorder_helper(root):
    list_rep = [root]
    if root.left:
        list_rep = inorder_helper(root.left) + list_rep
    if root.right:
        list_rep = list_rep + inorder_helper(root.right)

    return list_rep


def find_next_inorder(target_node):
    root = target_node
    while root.parent:
        root = root.parent
    all_nodes = inorder_helper(root)
    for i, node in enumerate(all_nodes):
        if node == target_node:
            if i == len(all_nodes) - 1:
                return None
            return all_nodes[i + 1]


# Tests

root = Node(10)
root.left = Node(5)
root.right = Node(30)
root.left.parent = root
root.right.parent = root
root.right.left = Node(22)
root.right.right = Node(35)
root.right.left.parent = root.right
root.right.right.parent = root.right

assert not find_next_inorder(root.right.right)
assert find_next_inorder(root.right.left) == root.right
assert find_next_inorder(root) == root.right.left
assert find_next_inorder(root.left) == root
