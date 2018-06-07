class FileProxy:
    def __init__(self, contents):
        self.contents = contents
        self.offset = 0
        self.buffer = ""

    def read_7(self):
        start = self.offset
        end = min(self.offset + 7, len(self.contents))
        self.offset = end
        return self.contents[start:end].strip()

    def read_n(self, n):
        while len(self.buffer) < n:
            additional_chars = self.read_7()
            if not (additional_chars):
                break
            self.buffer += additional_chars

        n_chars = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return n_chars.strip()


fp = FileProxy("Hello world")
assert fp.read_7() == "Hello w"
assert fp.read_7() == "orld"
assert fp.read_7() == ""

fp = FileProxy("Hello world")
assert fp.read_n(8) == "Hello wo"
assert fp.read_n(8) == "rld"

fp = FileProxy("Hello world")
assert fp.read_n(4) == "Hell"
assert fp.read_n(4) == "o wo"
assert fp.read_n(4) == "rld"
