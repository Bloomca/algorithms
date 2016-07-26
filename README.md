# Algorithms

This repository contains self-written algorithms in Python strictly for educational purposes. Don't try to run it in production!
Here there are pretty basic algorithms — I've tried to comment source code and add tests to all of them.

Now I have next algorithms:

- Merge sort with inversions counting implementation
    
    It is the simplest [algorithm](https://en.wikipedia.org/wiki/Merge_sort) which just cut array into smallest versions and then combine in subroutine. It is running in `O(n * log(n))`

- Quicksort algorithm
    
    This algorithm is a bit trickier -- we select pivot element, and partition elements around it into new arrays, and then combine them (they will be sorted in place). For better result it is usually written as randomized algorithm, and has average complexity as `O(n * log(n))`, and in worst case it has `O(n^2)`. Here I've implemented non-randomized pivot selection, so it is `O(n^2)` complexity, though the randomized pivot selection function is the easiest one.

- Minimum cut algorithm
    
    This algorithm finds [minimum cut](https://en.wikipedia.org/wiki/Minimum_cut) of the given graph. It uses [contraction algorithm of Karger](https://en.wikipedia.org/wiki/Karger%27s_algorithm), which is randomized algorithm with pretty small chances, but when running a lot of times, chances are pretty good. I run it n^2 times, where `n` is number of edges

- Strongly connected components
    
    This algorithms finds strongly connected components in given directed graph. It is an implementation of [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm).

- Dijkstra's shortest path algorithm
    
    This is a naive implementation of famous [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find shortest path from vertex `s` to `v`, if it exists. It works only edges are non-negative (or, strictly speaking, if all edges, except those who go from the initial vertex `s`).

And data structures:

- Heap

    [Heap](https://en.wikipedia.org/wiki/Heap_%28data_structure%29) is a data structure to quickly extract minimum (or maximum) element, in `O(log(n))`, and insert new elements without violating heap property in the same time. O(log(n)).
    Here I have the most basic implementation of [binary heap](https://en.wikipedia.org/wiki/Binary_heap) data structure, which supports both min and max usage, storing all data in single array with few rules. First — each node has it's children in `i * 2 + 1/2` indices, and the second is that after extracting and insertion we have to rearrange internal array. When we insert a new element, we add it to the end, and then start to swap with parent if it violates the heap property. If we extract an element, then we have to place the last element to root position, and then swap it with children if it violates. 
