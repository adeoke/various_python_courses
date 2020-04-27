"""This module will attempt to replicate a linked list"""


# Singularly linked list properties
# has a head, which is the first item in the list
# as its a singularly linked list then it has a next pointer to the next need
# in the list this is a trail until we reach the lst item in the list.

class Node:
    """this class represents a node in the linked list"""

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        """get the current node value"""
        return self.__data

    @data.setter
    def data(self, data):
        """set value for node"""
        print('trying to set data')
        self.__data = data

    @property
    def next(self):
        """return the next node"""
        return self.__next

    @next.setter
    def next(self, next_node):
        """set the next node to node object"""
        self.__next = next_node


class LinkedList:
    """This class represents the graph between the link list nodes"""

    def __init__(self):
        self.__node = None
        self.__head = None
        self.__tail = None
        self.__count = 0

    def append_node(self, data):
        """This method adds a node to the head of the linked list"""
        self.__node = Node(data)
        self.__node.next = self.__head
        self.__head = self.__node
        self.__tail = self.__node.next if self.__tail is None else self.__tail
        self.__count += 1

    def find(self, data):
        """This method will return the FIRST Node for a given value"""
        # Very important to start iterating from the HEAD
        item = self.__head

        while item:
            print('coming in the find loop')
            print('node data is: ', item.data)
            if data is item.data:
                print('found the item in the list')
                print('just for clarification this is', item.data)
                return item
            item = item.next

        return None

    def delete_node_with_data(self, data):
        item = self.__head

        if item.data is data:
            print('this is the head being deleted')
            self.__head = item.next
            self.__count -= 1
            return

        while item:
            if data is item.data:
                # delete this item
                del item
                self.__count -= 1
                return

            item.next = item.next.next

        return None

    def print_list(self):
        """print through al the node items in the linked list"""
        item = self.__head

        while item:
            print('node data is: ', item.data)
            item = item.next

    @property
    def count(self):
        print('Count is: ', self.__count)
        return self.__count

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, a_node):
        self.__head = a_node

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, a_node):
        self.__tail = a_node


# node = Node(3)

# node_2 = Node(5)
# node.next = node_2
#
# node_3 = Node(7)
# node_2.next = node_3

# print('loop through nodes')
#
# while node is not None:
#     print(node.data)
#     node = node.next

# node = Node(3)

linked_list = LinkedList()
linked_list.append_node(7)
linked_list.append_node(9)
linked_list.append_node(11)
linked_list.append_node(13)
print(linked_list.count)

# print('data is ', linked_list.get_node().data)
print('head is: ', linked_list.head.data)
print('tail is: ', linked_list.tail.data)
# linked_list.print_list()
linked_list.delete_node_with_data(13)
print('head is now: ', linked_list.head.data)
print(linked_list.count)
linked_list.print_list()
linked_list.delete_node_with_data(11)
linked_list.print_list()
print(linked_list.count)
