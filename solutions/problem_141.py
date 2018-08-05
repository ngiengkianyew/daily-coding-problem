class Stack:
    def __init__(self):
        self.list = []

    def __repr__(self):
        return str(self.list)

    def pop(self, stack_number):
        if not stack_number < len(self.list):
            return

        stack = self.list[stack_number]
        if not stack:
            return

        val = stack.pop()
        return val

    def push(self, item, stack_number):
        if stack_number < len(self.list):
            stack = self.list[stack_number]
            stack.append(item)
        elif stack_number == len(self.list):
            new_stack = list()
            new_stack.append(item)
            self.list.append(new_stack)


# Tests
st = Stack()

st.push(1, 0)
assert st.list == [[1]]
st.push(2, 1)
st.push(3, 2)
assert st.list == [[1], [2], [3]]
val = st.pop(3)
assert not val
val = st.pop(2)
assert val == 3
assert st.list == [[1], [2], []]
st.push(6, 0)
st.push(7, 0)
assert st.list == [[1, 6, 7], [2], []]
val = st.pop(0)
assert st.list == [[1, 6], [2], []]
