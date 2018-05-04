class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_char = preorder[0]
    if len(preorder) == 1:
        return Node(root_char)

    root_node = Node(root_char)
    for i, char in enumerate(inorder):
        if char == root_char:
            root_node.left = get_tree(
                preorder=preorder[1:i+1], inorder=inorder[:i])
            root_node.right = get_tree(
                preorder=preorder[i+1:], inorder=inorder[i+1:])

    return root_node


tree = get_tree(preorder=['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                inorder=['d', 'b', 'e', 'a', 'f', 'c', 'g'])
assert tree.val == 'a'
assert tree.left.val == 'b'
assert tree.left.left.val == 'd'
assert tree.left.right.val == 'e'
assert tree.right.val == 'c'
assert tree.right.left.val == 'f'
assert tree.right.right.val == 'g'

tree = get_tree(preorder=['a', 'b', 'd', 'e', 'c', 'g'],
                inorder=['d', 'b', 'e', 'a', 'c', 'g'])
assert tree.val == 'a'
assert tree.left.val == 'b'
assert tree.left.left.val == 'd'
assert tree.left.right.val == 'e'
assert tree.right.val == 'c'
assert tree.right.right.val == 'g'
