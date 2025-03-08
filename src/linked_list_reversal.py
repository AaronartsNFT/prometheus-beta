class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (Any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. 
                                   Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list in-place.
    
    This function reverses the links of a singly linked list, effectively 
    reversing the order of the nodes. It handles three scenarios:
    1. Empty list (head is None)
    2. List with a single node
    3. List with multiple nodes
    
    Args:
        head (ListNode): The head of the linked list to be reversed.
    
    Returns:
        ListNode: The new head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as reversal is done in-place
    """
    # Handle empty list or list with single node
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None
    current = head
    
    # Iterate through the list
    while current:
        # Store the next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (previously the last node)
    return prev