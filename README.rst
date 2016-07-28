Heapq\_max
==========

Description
-----------

A maxHeap version of heapq module for Python. Similar to heapq, c
implementation is used when available to ensure performance.

Dependencies
------------

Python >=3 Python 2 support will be implemented by 8/15/2016.

Installation
------------

::

    pip install heapq_max

Usage
-----

tl;dr: same as heapq module except adding '\_max' to all functions.

::

    from heapq_max import *

    heap_max = []                           # creates an empty heap
    heappush_max(heap_max, item)            # pushes a new item on the heap
    item = heappop_max(heap_max)            # pops the largest item from the heap
    item = heap_max[0]                      # largest item on the heap without popping it
    heapify_max(x)                          # transforms list into a heap, in-place, in linear time
    item = heapreplace_max(heap_max, item)  # pops and returns largest item, and
                                            # adds new item; the heap size is unchanged

License
-------

MIT
