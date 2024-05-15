import pytest
from LinkedList.LinkedList import LinkedList

def test_linked_list_operations():
    # Create an empty linked list
    ll = LinkedList()

    # Test append method
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    # Test length of linked list
    assert len(ll) == 5

    # Test __str__ method
    assert str(ll) == "1 -> 2 -> 3 -> 4 -> 5"

    # Test __getitem__ method
    assert ll[0] == 1
    assert ll[2] == 3
    assert ll[4] == 5

    # Test accessing out of bounds index
    with pytest.raises(IndexError):
        ll[5]

if __name__ == "__main__":
    pytest.main()
