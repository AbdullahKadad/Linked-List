# Singly Linked List Implementation

This repository contains a Python implementation of a singly linked list.

## Node Class

The `Node` class represents a single node in the linked list.

```python
class Node:
    def __init__(self, data=None):
        """
        Initializes a node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None
```

## LinkedList Class

The `LinkedList` class represents a list of Nodes.

```python
class LinkedList:
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.

        Args:
            data: The data to be stored in the new node.
        """

    def __len__(self):
        """
        Calculates the length of the linked list.

        Returns:
            int: The number of nodes in the linked list.
        """

    def __getitem__(self, index):
        """
        Gets the data at the specified index in the linked list.

        Args:
            index (int): The index of the node whose data is to be retrieved.

        Returns:
            Any: The data stored in the node at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """

    def __str__(self):
        """
        Converts the linked list to a string representation.

        Returns:
            str: A string representation of the linked list.
        """
