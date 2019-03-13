import sys


class ValueSet:
    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None


class MagicStruct:
    def __init__(self):
        self.keys = dict()
        self.values = dict()
        self.values[0] = ValueSet()
        self.values[sys.maxsize] = ValueSet()
        self.values[0].next = self.values[sys.maxsize]
        self.values[sys.maxsize].prev = self.values[0]
        self.vhead = self.values[0]
        self.vtail = self.values[sys.maxsize]

    def plus(self, k):
        vs = None
        if k not in self.keys:
            self.keys[k] = 0
            vs = ValueSet()
            prev_vs = self.vhead
            next_vs = self.vhead.next

        v = self.keys[k] + 1
        self.keys[k] = v

        if v in self.values:
            vs = self.values[v]
            prev_vs = self.values[v].prev
        vs.keys.add(k)
        next_vs = prev_vs.next

        vs.prev = prev_vs
        vs.next = next_vs

        if v-1 in self.values:
            old_vs = self.values[v-1]
            if not old_vs.keys:
                oprev = old_vs.prev
                onext = old_vs.next
                oprev.next = onext
                onext.prev = oprev

    def minus(self, k):
        if k not in self.keys:
            return

        vs = self.keys[k]
        prev_vs = vs.prev
        next_vs = vs.next
        v = self.keys[k] - 1

        if not v:
            prev_vs.next = next_vs
            next_vs.prev = prev_vs

    def get_max(self):
        pass

    def get_min(self):
        pass


# Tests
ms = MagicStruct()
ms.plus("a")
ms.plus("b")
ms.plus("a")
ms.plus("a")
print(ms.keys, ms.values)
ms.minus("a")
print(ms.keys, ms.values)
ms.minus("b")
print(ms.keys, ms.values)
print(ms.get_max())
