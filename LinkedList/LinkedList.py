class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

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
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __len__(self):
        """
        Calculates the length of the linked list.

        Returns:
            int: The number of nodes in the linked list.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

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
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __str__(self):
        """
        Converts the linked list to a string representation.

        Returns:
            str: A string representation of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements)



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Length of linked list:", len(ll))
    print("Linked list:", ll)
    print("Element at index 2:", ll[2])
    print("Element at index 2:", ll[3])