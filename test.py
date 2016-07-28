"""
These test cases only test heappop_max, heappush_max, heappushpop_max. The
other functions are directly imported from heapq module, which are tested in
https://github.com/python/cpython/blob/master/Lib/test/test_heapq.py
"""


import random
import unittest
from unittest import TestCase

from heapq_max import heappop_max, heappush_max, heappushpop_max


class TestHeap_max(TestCase):

    def test_heappushpop(self):
        h = []
        x = heappushpop_max(h, 10)
        self.assertEqual((h, x), ([], 10))

        h = [10]
        x = heappushpop_max(h, 10.0)
        self.assertEqual((h, x), ([10], 10.0))
        self.assertEqual(type(h[0]), int)
        self.assertEqual(type(x), float)

        h = [10]
        x = heappushpop_max(h, 9)
        self.assertEqual((h, x), ([9], 10))

        h = [10]
        x = heappushpop_max(h, 11)
        self.assertEqual((h, x), ([10], 11))

    def test_push_pop(self):
        # 1) Push 256 random numbers and pop them off, verifying all's OK.
        heap = []
        data = []
        self.check_invariant(heap)
        for i in range(256):
            item = random.random()
            data.append(item)
            heappush_max(heap, item)
            self.check_invariant(heap)
        results = []
        while heap:
            item = heappop_max(heap)
            self.check_invariant(heap)
            results.append(item)
        data_sorted = data[:]
        data_sorted.sort(reverse=True)
        self.assertEqual(data_sorted, results)
        # 2) Check that the invariant holds for a sorted array
        self.check_invariant(results)

        self.assertRaises(TypeError, heappush_max, [])
        try:
            self.assertRaises(TypeError, heappush_max, None, None)
            self.assertRaises(TypeError, heappop_max, None)
        except AttributeError:
            pass

    def check_invariant(self, heap):
            # Check the heap invariant.
        for pos, item in enumerate(heap):
            if pos:  # pos 0 has no parent
                parentpos = (pos - 1) >> 1
                self.assertTrue(heap[parentpos] >= item)

if __name__ == "__main__":
    unittest.main()
