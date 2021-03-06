#!/usr/bin/python

__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"

''' A class for a linked list that has the nodes in a FIFO order (such as a queue)'''


from node import Node



class LinkedListFIFO(object):

    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None # this is different from ll lifo


    # print each node's value, starting from the head
    def _printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.pointer

    # add a node in the first position
    # read will never be changed again while not empty
    def _addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    # delete a node in the first position, ie
    # when there is no previous node
    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print('The list is empty.')

    # add a node in a position different from head,
    # ie, in the end of the list
    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node


    # add nodes in general
    def addNode(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._add(value)

    # locate node with some index
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    # delete nodes in general
    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev :
                    self.head = node.pointer
                else:
                    prev.pointer = node.pointer
                if not self.tail == node:
                    self.tail = prev
            else:
                print('Node with index {} not found'.format(index))





if __name__ == '__main__':
    ll = LinkedListFIFO()
    for i in range(1, 5):
        ll.addNode(i)
    print('The list is:')
    ll._printList()
    print('The list after deleting node with index 2:')
    ll.deleteNode(2)
    ll._printList()
    print('The list after adding node with value 15')
    ll._add(15)
    ll._printList()
    print("The list after deleting everything...")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printList()
