DstLib - Data Structures Python Library
============================================

DstLib is a Python library for linear data structures It can be used to work with linked list, queue and stack.
Linked list is known for its better performance compared to normal python array, but python doesn't come with linked list.
So this library is here to fill this gap. Both the queue and the stack are implemented using using linked list.
Source Code (Don’t forget to put a star if you liked my project😅): `dstlib <https://github.com/algebra7dsalib>`


Installation
------------
::

    pip install dstlib

Usage
-----

Working with Linked List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    L = dstlib.LinkedList()     #initiate the linked list object
    len(L)                      #to get the number of elements in the list
    is_empty = L.is_empty()     #to know whether the list is empty or not: returns boolean
    L.append(x)                 #to append an element x
    L.prepend(y)                #to add an element y to the front of the list
    L.insert(i, x)              #to insert an element x at a given index i

    p1 = L.add_first(x)         #do the same as L.prepend() but return the position of the added element x
    pl = L.add_last(y)          #do the same as L.append() but return the position of the added element y

    p2 = L.add_after(p1, x)     #to add an element x after element at position p1 and return the position of the added element x
    p3 = L.add_before(pl, y)    #to add an element y before element at position pl and return the position of the added element y

    x = L.delete(p)             #to delete an element at position p and get the deleted element
    p = L.replace(p, x)         #

    L.reverse()                 #to reverse the list
    p1 = L.first_position()     #to get the position of the first element in the list
    pl = L.last_position()      #to get the position of the last element in the list
    p2 = L.position_after(p1)   #to get the position of the element that is after position p1
    p1 = L.position_before(p2)  #to get the position of the element that is before position p2

    L2 = dstlib.LinkedList()    #initiate another linked list object
    L2.append(x)                #append an element x
    L2.append(y)                #append an element y
    L.concat(L2)                #to concatenate L2 to L (append all L2 elements to L)

    L.sort()                    #to sort the elements of L in ascending order

    L[i]                        #to get the element at index i in the linked list

    

Working with Queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    Q = dstlib.Queue()          #initiate the Queue object
    len(Q)                      #to get the number of elements in the queue
    is_empty = Q.is_empty()     #to know whether the queue is empty or not: returns boolean
    Q.enqueue(x)                #to add an element x to the end of the queue
    el = Q.dequeue(x)           #to remove an element x from the front of the queue and return the element
    Q.first()                   #to get the first element in the queue
    Q.last()                    #to get the last element in the queue
    Q.rotate()                  #to take the first element in the queue back to the end of the queue

    Q2 = dstlib.Queue()         #initiate another queue object
    Q.concat_detroy()           #to concatenate Q2 to Q (add all Q2 elements to the end of Q) and destroy Q2
    Q.concat()                  #same as concat_detroy() but does not destroy Q2

    p = Q.enqueue_position(x)   #to add an element x to the end of the queue and return the position of the element
    p1 = Q.first_position()     #to get the position of the first element in the queue
    pl = Q.last_position()      #to get the position of the last element in the queue

    

Working with Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    S = dstlib.Stack()          #initiate the stack object
    len(S)                      #to get the number of elements in the stack
    is_empty = S.is_empty()     #to know whether the stack is empty or not: returns boolean
    S.push(x)                   #to push an element x to the stack
    el = S.pop()                #to remove an element from the top of the stack and return the element
    el = S.top()                #to get the element in the top of the stack without removing its
    p = S.push_position(x)      #to add an element x to the top of the stack and return the position of the element
    pt = S.top_position()       #to get the position of the top element in the stack
