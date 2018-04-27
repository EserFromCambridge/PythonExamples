from __future__ import print_function


class Queue(object):

    def __init__(self, limit=100):
        self.items = []
        self.limit = limit

    def __str__(self):
        return str(self.items)

    def add(self, data):
        if self.limit > len(self.items):
            self.items.append(data)             # inserts the data to the end of the list
        else:
            print("Exceeds the limits of the queue")    # TODO raise an exception

    def get(self):
        if len(self.items) > 0:
            self.items.pop(0)
        else:
            print("Queue is already empty")     # TODO raise an exception

    def get_size(self):
        return len(self.items)

    def see_front(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            print("Queue is already empty")
