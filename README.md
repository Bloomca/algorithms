# Algorithms

This repository contains self-written algorithms in Python strictly for educational purposes. Don't try to run it in production!
Here there are pretty basic algorithms — I've tried to comment source code and add tests to all of them.

Now I have:
- Merge sort with inversions counting implementation
    It is the simplest [algorithm](https://en.wikipedia.org/wiki/Merge_sort) which just cut array into smallest versions and then combine in subroutine. It is running in `O(n * log(n))`
    ![merge-sort-algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Merge_sort_algorithm_diagram.svg/618px-Merge_sort_algorithm_diagram.svg.png)
- Quicksort algorithm
    This algorithm is a bit trickier -- we select pivot element, and partition elements around it into new arrays, and then combine them (they will be sorted in place). For better result it is usually written as randomized algorithm, and has average complexity as `O(n * log(n))`, and in worst case it has `O(n^2)`. Here I've implemented non-randomized pivot selection, so it is `O(n^2)` complexity, though the randomized pivot selection function is the easiest one.
    ![quicksort-algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Quicksort-diagram.svg/400px-Quicksort-diagram.svg.png)
- Minimum cut algorithm
    This algorithm finds [minimum cut](https://en.wikipedia.org/wiki/Minimum_cut) of the given graph. It uses [contraction algorithm of Karger](https://en.wikipedia.org/wiki/Karger%27s_algorithm), which is randomized algorithm with pretty small chances, but when running a lot of times, chances are pretty good. I run it n^2 times, where `n` is number of edges
- Strongly connected components
    This algorithms finds strongly connected components in given directed graph. It is an implementation of [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm).
- Dijkstra's shortest path algorithm
    This is a naive implementation of famous [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find shortest path from vertex `s` to `v`, if it exists. It works only edges are non-negative (or, strictly speaking, if all edges, except those who go from the initial vertex `s`).
