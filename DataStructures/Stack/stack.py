from __future__ import print_function


class Stack(object):
    """ A class for implementing a kind of data type "stack"

        It works Last in First Out basis.
    """

    def __init__(self, size_limit=20):
        self.stack = []
        self.size_limit = size_limit

    def push(self, new_data):
        if len(self.stack) >= self.size_limit:
            raise OverFlowError
        else:
            self.stack.append(new_data)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            return value
        else:
            return None

    def get_size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


class OverFlowError(BaseException):
    pass
