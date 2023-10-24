#!/usr/bin/python3
""" Defines classes  Node and  SinglylinkedList """


class Node:
    """
    A class which defines a node

    Attributes:
        data: data field
    """
    def __init__(self, data, next_node=None):
        """
        Makes a new instance of Node class

        Args:
            __data: data field of the node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        gets the data field instance

        Returns: data field of node
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        sets data property

        Args: value (int): data field of node

        Raises:
        TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        gets the next_node instance

        Returns: The instsance of next_node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        sets the node

        Args:
            value (none): next node of Node class

        Raises:
            TypeError: next_node must be a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class defining properties of a SinglyLinkedList

    Attributes:
        head: the head of the SinglyLinkedList
    """
    def __init__(self):
        """
        Creates SinglyLinkedList

        Args:
            head: reps the head of SinglyLinkedList
        """
        self.__head = None

    def __str__(self):
        """
        Reps class object as String

        Returns: string class object

        """
        res = self.__head
        node_list = []

        while res:
            node_list.sort()
            node_list.append(str(res.data))
            res = res.next_node

        node_list.sort(key=int)
        return ("\n".join(node_list))

    def sorted_insert(self, value):
        """
        Puts new node atgiven position

        Args:
            value: value
        """

        if self.__head is None:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
