from __future__ import print_function


class Node(object):
    """ A class for implementing a node inside a linked list

    Args:
        data        : The data value of the node
        next_data   : The pointer which points the next node
    """

    def __init__(self, data=None, next_data=None):
        self._data = data
        self._next = next_data

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next

    data = property(get_data, set_data)
    next = property(get_next, set_next)

    def __str__(self):
        return "{0.data} --> {0.next}".format(self)


class LinkedList(object):
    """
    A class for implementing a single linked list

    Args:
        node        : Initialises the "Node" which will be the first element of list
    """
    def __init__(self, node=None):
        self.head = node
        if node:
            self._size = 1
        else:
            self._size = 0

    def get_size(self):
        return self._size

    size = property(get_size)

    def pop_in(self, data):
        self.insert(data, 0)

    def pop_up(self):
        self.delete(0)

    def insert(self, data, index=None):
        if index is None:
            index = 0
        node_list = self.find_node(index)
        new_node = Node(data)
        node_list[0].next = new_node
        new_node.next = node_list[1]
        if index == 0:
            self.head = new_node

        self._size += 1

    def delete(self, index=None):
        if index is None:
            index = 0
        elif index >= self.get_size():
            index = self.get_size()-1
        node_list = self.find_node(index)
        node_list[0].next = node_list[2]
        if index == 0:
            self.head = node_list[2]
        self._size -= 1

    def find_node(self, index=None):
        if index == 0:
            prev_node = Node()
            current_node = self.head
            next_node = self.head.next
        elif index == 1:
            prev_node = self.head
            current_node = self.head.next
            next_node = current_node.next
        else:
            if index > self.get_size():
                index = self.get_size()
            i = 0
            current_node = self.head
            while i < index:
                prev_node = current_node
                current_node = current_node.next
                i += 1
                if i == index:
                    if current_node is None:
                        next_node = Node()
                    else:
                        next_node = current_node.next
                    break

        return [prev_node, current_node, next_node]

    def search(self, data):
        index = 0
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return index
            else:
                index += 1
                current_node = current_node.next
        return None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, "--> ", end='')
            current_node = current_node.next
        print("None")
