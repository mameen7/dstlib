from .node import Node
from .utils import _Position
from .exceptions import Empty
from .exceptions import ValueError


class QueueBase:
    """A base class providing a circularly linked list based queue representation"""

    def __init__(self):
        """Initiate an empty queue with a null tail node"""
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """
        Return the number of elements in the queue

        Returns: int: size of the queue
        """
        return self._size

    def is_empty(self):
        """
        Return True if queue is empty

        Returns: bool
        """
        return self._size == 0

    def enqueue(self, el, called=False):
        """
        Add a giving alement to the end of the queue

        Param el: element to be added to the queue
        Param called: a flag to seperate between user call and the system call: default to False

        Returns: None (nothing) if called is False but return the newly added node if called is set to True
        """
        new_tail_node = Node(el, None)
        if self.is_empty():
            new_tail_node._next = new_tail_node
        else:
            new_tail_node._next = self._tail._next
            self._tail._next = new_tail_node

        self._tail = new_tail_node
        self._size += 1
        if called:
            return new_tail_node

    def dequeue(self):
        """
        Remove an alement from the front of the queue

        Returns: the removed element
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return head._element

    def first(self):
        """Returns the first element in the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._tail._next._element

    def last(self):
        """Returns the last element in the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._tail._element

    def rotate(self):
        """Takes the first element to the end of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty! You cannot rotate an empty queue")
        self._tail = self._tail._next

    def concat_detroy(self, Q):
        """
        Join a giving queue to the current queue from the end of the current queue and destroy the giving queue

        Param Q: A queue object to join with the current queue

        Returns: None
        """
        if Q.is_empty():
            return
        for _ in Q:
            self.enqueue(Q.dequeue())
            if Q.is_empty():
                break

    def concat(self, Q):
        """
        Join a giving queue to the current queue from the end of the current queue
        Param Q: A queue object to be joined with the current queue

        Returns: None
        """
        if Q.is_empty():
            return
        for el in Q:
            self.enqueue(el)

    def __iter__(self):
        """
        Special method (iterator) to allow iterating over the queue

        Returns: None (nothing)
        """
        if self._tail == None:
            return
        first_node = self._tail._next
        while first_node is not None:
            yield first_node._element
            if first_node == self._tail:
                break
            first_node = first_node._next


class Queue(QueueBase):
    """Position based queue implementation using a queue base class"""

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

    def enqueue_position(self, el):
        """
        Add a giving element to the end of the queue

        Param el: element (value) to be added to the queue

        Returns: position object
        """
        enqueued_node = self.enqueue(el, called=True)
        return self._get_position(enqueued_node)

    def first_position(self):
        """Returns the position of the first element in the queue"""
        return self._get_position(self._tail._next)

    def last_position(self):
        """Returns the position of the last element in the queue"""
        return self._get_position(self._tail)
