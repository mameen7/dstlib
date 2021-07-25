from .node import Node
from .utils import _Position
from .exceptions import Empty

class StackBase:
    """A base class providing a Stack implementation using a singly linked list."""

    def __init__(self):
        """Initiate an empty queue with a null head node"""
        self._head = None
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the stack

        Returns: int: size of the stack
        """
        return self._size

    def is_empty(self):
        """
        Return True if stack is empty

        Returns: bool
        """
        return self._size == 0

    def push(self, el, called=False):
        """
        Add a giving alement to the top of the stack

        Param el: element to be added to the stack
        Param called: a flag to seperate between user call and the system call: default to False

        Returns: None (nothing) if called is False but return the newly added node if called is set to True
        """
        self._head = Node(el, self._head)
        self._size += 1
        if called:
            return self._head

    def pop(self):
        """
        Remove an alement from the end of the stack

        Returns: the removed element
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        head = self._head
        self._head = head._next
        self._size -= 1
        return head._element

    def top(self):
        """
        Returns an alement from the end of the stack

        Returns: the top element
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def __iter__(self):
        """
        Special method (iterator) to allow iterating over the stack

        Returns: None (nothing)
        """
        if self._head == None:
            return
        first_node = self._head
        while first_node is not None:
            yield first_node._element
            if first_node._next is None:
                break
            first_node = first_node._next
    

class Stack(StackBase):
    """Position based stack implementation using a stack base class"""

    class Position(_Position):
        """extension of the inherited _Position class for positioning of nodes"""
        pass

    def _get_position(self, node):
        """
        Returns the postion of the the giving node if the giving node is nonsentinel node

        Returns: the position object if node is nonsentinel else return None
        """
        return self.Position(self, node)

    def _validate(self, p):
        """Return position's node if position is valid, else raise inappropriate error."""
        if not isinstance(p, self.Position):
            raise TypeError("improper Position")
        if p._container is not self:
            raise ValueError("position does not belong to this container")
        if p._node._next == None:
            raise ValueError("position is no longer valid")
        return p._node

    def push_position(self, el):
        """
        Add a giving element to the top of the stack

        Param el: element (value) to be added to the stack

        Returns: position object
        """
        pushed_node = self.push(el, called=True)
        return self._get_position(pushed_node)

    def top_position(self):
        """Returns the position of the top element in the stack"""
        return self._get_position(self._head)
