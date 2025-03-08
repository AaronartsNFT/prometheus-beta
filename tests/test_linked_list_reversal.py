import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def list_to_array(head):
    """
    Convert a linked list to an array for easy comparison.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: Array representation of the linked list values.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """
    Convert an array to a linked list.
    
    Args:
        arr (list): Array of values to convert.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def test_reverse_empty_list():
    """Test reversing an empty list."""
    head = None
    reversed_head = reverse_linked_list(head)
    assert reversed_head is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    head = ListNode(42)
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 42
    assert reversed_head.next is None

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes."""
    # Create a list: 1 -> 2 -> 3 -> 4 -> 5
    input_arr = [1, 2, 3, 4, 5]
    head = array_to_list(input_arr)
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Convert back to array and verify
    reversed_arr = list_to_array(reversed_head)
    assert reversed_arr == list(reversed(input_arr))

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    # Create a list: 10 -> 20
    input_arr = [10, 20]
    head = array_to_list(input_arr)
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Convert back to array and verify
    reversed_arr = list_to_array(reversed_head)
    assert reversed_arr == list(reversed(input_arr))

def test_verify_links_after_reversal():
    """Ensure links are correctly maintained after reversal."""
    # Create a list: 1 -> 2 -> 3 -> 4 -> 5
    input_arr = [1, 2, 3, 4, 5]
    head = array_to_list(input_arr)
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Verify links
    current = reversed_head
    for expected_val in reversed(input_arr):
        assert current is not None
        assert current.val == expected_val
        current = current.next
    
    # Ensure no additional nodes
    assert current is None