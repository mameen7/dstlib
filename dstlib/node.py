class Node:
    """Class for storing linked list node."""
    
    def __init__(self, element, next_pointer, prev_pointer=None):
        self._element = element
        self._next = next_pointer
        self._prev = prev_pointer