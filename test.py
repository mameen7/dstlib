import unittest
import dstlib


class LinkedListValuesTest(unittest.TestCase):

    def test_match(self):
        L = dstlib.LinkedList()
        self.assertEqual(len(L), 0)
        self.assertTrue(L.is_empty())
        self.assertIsNone(L.append(5))
        self.assertIsNone(L.prepend(3))
        self.assertIsNone(L.append(6))
        self.assertEqual(len(L), 3)
        self.assertFalse(L.is_empty())
        self.assertIsNone(L.prepend(2))

        p1 = L.first_position()
        p2 = L.position_after(p1)
        pl = L.last_position()
        p3 = L.position_before(pl)

        self.assertEqual(p1.element(), 2)
        self.assertEqual(p2.element(), 3)
        self.assertEqual(p3.element(), 5)
        self.assertEqual(pl.element(), 6)

        p2 = L.add_first(9)
        pl = L.add_last(1)
        p1 = L.add_before(p2, 8)
        p3 = L.add_after(p2, 7)
        self.assertEqual(len(L), 8)
        el = L.delete(p1)
        self.assertEqual(len(L), 7)
        p0 = L.add_first(0)
        self.assertEqual(p0.element(), 0)
        p0 = L.replace(p0, 8)
        self.assertEqual(p0.element(), 8)
        L.append(4)
        L.append(10)
        L.append(0)

        L2 = dstlib.LinkedList()
        L2.append(15)
        L2.append(14)
        L2.append(13)
        L2.append(12)
        L2.append(11)

        self.assertEqual(len(L2), 5)
        self.assertIsNone(L.concat(L2))
        self.assertEqual(len(L), 16)

        sorts = [i for i in range(16)]
        L.sort()
        sorted_L = [l for l in L]
        self.assertEqual(sorted_L, sorts)

        reverse = [j for j in range(15, -1, -1)]
        L.reverse()
        reverse_L = [l for l in L]
        self.assertEqual(reverse_L, reverse)

        self.assertEqual(L[0], 15)
        self.assertEqual(L[1], 14)
        self.assertEqual(L[2], 13)
        self.assertEqual(L[7], 8)
        self.assertEqual(L[8], 7)
        self.assertEqual(L[len(L)-1], 0)

        self.assertIsNone(L.insert(0, 16))
        self.assertIsNone(L.insert(17, 17))



class QueueValuesTest(unittest.TestCase):
    
    def test_match(self):
        Q = dstlib.Queue()
        self.assertEqual(len(Q), 0)
        self.assertTrue(Q.is_empty())
        self.assertIsNone(Q.enqueue(1))
        self.assertIsNone(Q.enqueue(2))
        self.assertIsNone(Q.enqueue(3))
        self.assertEqual(Q.dequeue(), 1)
        self.assertEqual(len(Q), 2)
        self.assertFalse(Q.is_empty())
        self.assertIsNone(Q.enqueue(1))
        self.assertEqual(Q.first(), 2)
        self.assertEqual(Q.last(), 1)
        self.assertIsNone(Q.rotate())
        self.assertIsNone(Q.rotate())
        self.assertEqual(Q.first(), 1)
        self.assertEqual(Q.last(), 3)

        Q2 = dstlib.Queue()
        self.assertIsNone(Q2.enqueue(4))
        self.assertIsNone(Q2.enqueue(5))
        self.assertIsNone(Q2.enqueue(6))
        self.assertIsNone(Q.concat(Q2))
        self.assertEqual(len(Q), 6)
        self.assertEqual(len(Q2), 3)
        self.assertEqual(Q.last(), 6)

        Q3 = dstlib.Queue()
        self.assertIsNone(Q3.enqueue(7))
        self.assertIsNone(Q3.enqueue(8))
        self.assertIsNone(Q3.enqueue(9))
        self.assertIsNone(Q.concat_detroy(Q3))
        self.assertEqual(len(Q), 9)
        self.assertEqual(len(Q3), 0)
        self.assertEqual(Q.last(), 9)

        p10 = Q.enqueue_position(10)
        p1 = Q.first_position()
        pl = Q.last_position()
        self.assertEqual(p10.element(), 10)
        self.assertEqual(p1.element(), 1)
        self.assertEqual(pl.element(), 10)


class StackValuesTest(unittest.TestCase):
    
    def test_match(self):
        S = dstlib.Stack()
        self.assertEqual(len(S), 0)
        self.assertTrue(S.is_empty())
        S.push(1)
        S.push(2)
        S.push(3)
        S.push(4)
        self.assertEqual(S.pop(), 4)
        self.assertEqual(S.top(), 3)

        p4 = S.push_position(4)
        S.push(5)
        top_p = S.top_position()
        self.assertEqual(p4.element(), 4)
        self.assertEqual(top_p.element(), 5)
        self.assertFalse(S.is_empty())


if __name__ == '__main__':
    unittest.main()
