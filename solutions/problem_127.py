FACTOR = 10


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)

    @staticmethod
    def convert_num_to_list(num):
        numstr = str(num)
        dummy_head = Node(0)
        prev = dummy_head
        for num in numstr[::-1]:
            curr = Node(int(num))
            prev.next = curr
            prev = curr

        return dummy_head.next

    @staticmethod
    def convert_list_to_num(head):
        curr = head
        num = 0
        factor = 1
        while curr:
            num += factor * curr.val
            curr = curr.next
            factor *= FACTOR

        return num

    @staticmethod
    def add_nums(list_a, list_b):
        new_dummy_head = Node(0)
        prev_res = new_dummy_head

        curr_a, curr_b = list_a, list_b
        carry = 0

        while carry or curr_a or curr_b:
            res_digit = 0
            if carry:
                res_digit += carry
            if curr_a:
                res_digit += curr_a.val
                curr_a = curr_a.next
            if curr_b:
                res_digit += curr_b.val
                curr_b = curr_b.next

            carry = res_digit // FACTOR
            curr_res = Node(res_digit % FACTOR)

            prev_res.next = curr_res
            prev_res = curr_res

        return new_dummy_head.next


assert Node.convert_list_to_num(
    Node.add_nums(Node.convert_num_to_list(0),
                  Node.convert_num_to_list(1))) == 1
assert Node.convert_list_to_num(
    Node.add_nums(Node.convert_num_to_list(1000),
                  Node.convert_num_to_list(1))) == 1001
assert Node.convert_list_to_num(
    Node.add_nums(Node.convert_num_to_list(99),
                  Node.convert_num_to_list(25))) == 124
