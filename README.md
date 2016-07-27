Heapq_max
======================


## Description
A maxHeap version of heapq module for Python. Similar to heapq, c implementation is used when available to ensure performance.


## Usage
tl;dr: same as heapq module except adding '_max' to all functions.
```
heap_max = []                           # creates an empty heap
heappush_max(heap_max, item)            # pushes a new item on the heap
item = heappop_max(heap_max)            # pops the largest item from the heap
item = heap_max[0]                      # largest item on the heap without popping it
heapify_max(x)                          # transforms list into a heap, in-place, in linear time
item = heapreplace_max(heap_max, item)  # pops and returns largest item, and
                                        # adds new item; the heap size is unchanged
```

## License
MIT
