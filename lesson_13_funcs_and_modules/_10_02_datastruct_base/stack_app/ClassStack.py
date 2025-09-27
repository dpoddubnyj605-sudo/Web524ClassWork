class MyStack:
    def __init__(self, stack=None):
        if stack:
            self.stack = stack
        else:
            self.stack = []

    def push(self, data):
        self.stack.append(data)
        return True

    def pop_stack(self):
        if self.stack:
            return self.stack.pop()
        return None

    def is_stack(self):
        if self.stack:
            return self.stack
        return None

