from .node import Node
from .utils import _Position
from .exceptions import ValueError
import math

class _DoubleLinkedBase:
    """A base class providing a doubly linked list representation"""

    def __init__(self):
        """Initiate an empty linked list with two sentinel nodes (head & tail)."""
        self._head = Node(None, None)
        self._tail = Node(None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        """
        Return the number of elements in the list

        Returns: int: size of the Linked List
        """
        return self._size

    def __getitem__(self, i):
        """Return element at index i"""
        if not 0 <= i < self._size:
            raise IndexError("invalid index")
        
        max_index = self._size - 1
        if i == 0:
            return self._head._next._element
        if i == max_index:
            return self._tail._prev._element
        
        current_node = self._get_current_node(i, max_index)
        return current_node._element

    def _delete_node(self, node):
        """
        Delete nonsentinel node from the linked list and return its element

        Param node: the node to be deleted from the linked list.

        Returns: deleted node value
        """
        prev_node = node._prev
        next_node = node._next
        prev_node._next = next_node
        next_node._prev = prev_node
        removed_element = node._element
        node._prev = node._next = node._element = None
        self._size -= 1
        return removed_element

    def _insert_between(self, el, predecessor, successor):
        """
        Insert node between two given nodes predecessor & successor

        Param el: element (value) to be inserted into a new node in between predecessor & successor
        Param predecessor: the node that will the new node will be next to
        param successor: the node that will be next to the new node

        Returns: the inserted node
        """
        new_node = Node(el, successor, predecessor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def is_empty(self):
        """
        Return True if list is empty

        Returns: bool
        """
        return self._size == 0

    def append(self, el):
        """
        Add a given element to the end of the linked list

        Param el: element (value) to be added

        Returns: None (nothing)
        """
        new_node = Node(el, self._tail, self._tail._prev)
        self._tail._prev._next = new_node
        self._tail._prev = new_node
        self._size += 1

    def prepend(self, el):
        """
        Add a given element to the front of the linked list

        Param el: element (value) to be added

        returns: None (nothing)
        """
        new_node = Node(el, self._head._next, self._head)
        self._head._next._prev = new_node
        self._head._next = new_node
        self._size += 1

    def insert(self, i, el):
        """
        Insert a given element 'el' at a given index 'i' in the linked list

        Param el: element (value) to be added

        returns: None (nothing)
        """
        max_index = self._size - 1
        if i == 0:
            self.prepend(el)
        elif i > max_index:
            self.append(el)
        else:
            current_node = self._get_current_node(i, max_index)
            prev_node = current_node._prev
            new_node = Node(el, current_node, prev_node)
            prev_node._next = new_node
            current_node._prev = new_node
            self._size += 1

    def reverse(self):
        """
        Reverse the linked list

        Returns: None (nothing)
        """
        temp = None
        initial_first = self._head._next
        current = initial_first
        while current is not None:
            temp = current._prev
            current._prev = current._next
            current._next = temp
            current = current._prev

        if temp is not None:
            self._head._next = temp

        self._tail._next = None
        initial_first._next = self._tail
        self._tail._prev = initial_first
        self._head._prev = None

    def _get_current_node(self, i, max_index):
        """Utility method"""
        mid = math.ceil(max_index/2)
        if i <= mid:
            count = 0
            current_node = self._head._next
            while count != i:
                next_node = current_node._next
                count += 1
                current_node = next_node
        else:
            count = max_index
            current_node = self._tail._prev
            while count != i:
                prev_node = current_node._prev
                count -= 1
                current_node = prev_node

        return current_node



class LinkedList(_DoubleLinkedBase):
    """Position based linked list implementation using doubly linked list base class"""

    class Position(_Position):
        """extension of the inherited _Position class for positioning of nodes"""

        def _get_key(self):
            """Returns the identifier of the current position"""
            return id(self)
        
    def __iter__(self):
        """
        Special method (iterator) to allow iterating over the linked list

        Returns: None (nothing)
        """
        position = self.first_position()
        while position is not None:
            yield position.element()
            position = self.position_after(position)

    def _get_position(self, node):
        """
        Returns the postion of the the giving node if the giving node is nonsentinel node

        Returns: the position object if node is nonsentinel else return None
        """
        if node is self._head or node is self._tail:
            return None
        return self.Position(self, node)

    def _insert_between(self, el, predecessor, successor):
        """
        Insert node between two given nodes predecessor & successor

        Param el: element (value) to be inserted into a new node in between predecessor & successor
        Param predecessor: the node that will the new node will be next to
        param successor: the node that will be next to the new node

        Returns: the position object
        """
        node = super()._insert_between(el, predecessor, successor)
        return self._get_position(node)

    def _validate(self, p):
        """Returns position's node if position is valid, else raise inappropriate error"""
        if not isinstance(p, self.Position):
            raise TypeError("improper Position")
        if p._container is not self:
            raise ValueError("position does not belong to this container")
        if p._node._next == None:
            raise ValueError("position is no longer valid")
        return p._node

    def first_position(self):
        """Returns the position of the first element in the linked list"""
        return self._get_position(self._head._next)

    def last_position(self):
        """Returns the position of the last element in the linked list"""
        return self._get_position(self._tail._prev)

    def position_after(self, p):
        """
        Returns the position next to the giving position in the linked 

        Param p: a position object

        Returns: position object
        """
        node = self._validate(p)
        return self._get_position(node._next)

    def position_before(self, p):
        """
        Returns the position before the giving position in the linked 

        Param p: a position object

        Returns: position object
        """
        node = self._validate(p)
        return self._get_position(node._prev)

    def add_first(self, el):
        """
        Add a giving element to the front of the linked list

        Param el: element (value) to be added to the linked list

        Returns: position object
        """
        return self._insert_between(el, self._head, self._head._next)

    def add_last(self, el, no_return=False):
        """
        Add a giving element to the end of the linked list

        Param el: element (value) to be added to the linked list

        Returns: position object
        """
        p = self._insert_between(el, self._tail._prev, self._tail)
        if not no_return:
            return p

    def add_before(self, p, el):
        """
        Add a giving element before the giving position 

        Param el: element (value) to be added to the linked list
        Param p: the position to add the element before

        Returns: position object
        """
        node = self._validate(p)
        return self._insert_between(el, node._prev, node)
    
    def add_after(self, p, el):
        """
        Add a giving element after the giving position 

        Param el: element (value) to be added to the linked list
        Param p: the position to add the element after

        Returns: position object
        """
        node = self._validate(p)
        return self._insert_between(el, node, node._next)

    def delete(self, p):
        """
        Deletes element at a giving position

        Param p: The position of the element that will be deleted

        Returns: the deleted element
        """
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, el):
        """
        Replaces element at a giving position with the giving element

        Param p: the position that its element will be replaced
        Param el: element to replace the previous element

        Returns position object
        """
        node = self._validate(p)
        node._element = el
        return p

    def concat(self, L):
        """
        Join a giving linked list to the current linked list from the end of the current linked list and destroy the giving linked list

        Param Q: a linked list object to join with the current linked list

        Returns: None
        """
        if L.is_empty():
            return
        for el in L:
            p = self.add_last(el, no_return=True)

    def sort(self):
        """Sort Linked List of comparable elements into nondecreasing order using insertion sort algorithm"""
        if len(self) > 1:
            first_position = self.first_position()
            marker = first_position
            while marker != self.last_position() and self.position_after(marker) != None:
                pivot = self.position_after(marker)
                pivot_value = pivot.element()
                if pivot_value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while self.position_before(walk) != None and walk._get_key() != first_position._get_key() and self.position_before(walk).element() > pivot_value:
                        walk = self.position_before(walk)

                    self.delete(pivot)
                    self.add_before(walk, pivot_value)
