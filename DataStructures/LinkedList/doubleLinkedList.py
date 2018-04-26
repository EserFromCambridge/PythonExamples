from __future__ import print_function


class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        """ A class for implementing a node in a double linked list

        :param data: represents the value of the Node
        :param next_node: represents the previous Node which is connected to this node
        :param prev_node: represents the next Node which is connected to this node
        """
        self._data = data
        self._prev = prev_node
        self._next = next_node

    def get_data(self):
        return self._data

    def set_data(self, new_data=None):
        self._data = new_data

    data = property(get_data, set_data)

    def get_prev(self):
        return self._prev

    def set_prev(self, new_prev=None):
        self._prev = new_prev

    prev = property(get_prev, set_prev)

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next

    next = property(get_next, set_next)


class DoubleLinkedList(object):

    def __init__(self, data=None):
        """ A class fro implementing a double linked list

        :param data: represents the Node while creating the instance
        """
        if data is not None:
            self._size = 1
            self.head = Node(data)
            self.tail = self.head
        else:
            self._size = 0
            self.head = None
            self.tail = None

    def get_size(self):
        return self._size

    size = property(get_size)

    def add_to_head(self, data):
        new_node = Node(data)
        if self._size == 0:
            self.head = new_node
        else:
            if self._size == 1:
                self.tail = self.head
            next_node = self.head
            self.head = new_node
            self.head.set_next(next_node)
            next_node.set_prev(self.head)
        self._size += 1

    def delete_from_tail(self):
        if self.size == 0:
            print("No items inside the list")
        elif self._size == 1:
            self.head = None
            self.tail = None
            self._size -= 1
        else:
            prev_node = self.tail.get_prev()
            prev_node.set_next(None)
            node = self.tail
            node.set_prev(None)
            self.tail = prev_node
            self._size -= 1

    def display(self):
        node = self.head
        while node:
            print("{}".format(node.get_data()), end='')
            node = node.get_next()
            if node:
                print(" <--> ", end='')
            else:
                print()


