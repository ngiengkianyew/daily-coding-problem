def is_parent_locked(node):
    if not node.parent:
        return False
    elif node.parent.locked:
        return True
    return is_parent_locked(node.parent)


def update_parent(node, enable_locks):
    increment = 1 if enable_locks else -1
    if node.parent:
        node.parent.locked_descendants += increment
        update_parent(node.parent, enable_locks)


class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self.locked = False
        self.locked_descendants = 0

    def __str__(self):
        return "val={}; locked={}; locked_descendants={}".format(
            self.val, self.locked, self.locked_descendants)

    def lock(self):
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            self.locked = True
            update_parent(node=self, enable_locks=True)
            return True

    def unlock(self):
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            self.locked = False
            update_parent(node=self, enable_locks=False)
            return True

    def is_locked(self):
        return self.locked


a = Node("a", None)
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", c)
g = Node("g", c)

assert b.lock()
assert b.is_locked()
assert c.lock()
assert b.unlock()
assert not b.is_locked()
assert d.lock()

assert not g.lock()
assert c.unlock()
assert g.lock()

assert f.lock()
assert e.lock()
assert a.locked_descendants == 4
assert b.locked_descendants == 2
assert c.locked_descendants == 2
