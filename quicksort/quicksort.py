import math

def select_first(array):
    """
    The most obvious strategy to choose pivot element
    Function gets the first element of the array as a pivot
    """
    return (array[0], 0)

def select_last(array):
    """
    Takes last element of the array as a pivot
    """
    length = len(array)
    index = length - 1
    return (array[index], index)

def select_middle(array):
    """
    Choose median using following strategy:
    
    get first, last and the middle element,
    and then choose average from these elements 
    """
    length = len(array)
    index = length / 2
    if length % 2 == 0:
        index = index - 1        
    first = array[0]
    last = array[length - 1]
    middle = array[index]

    if (
        (first <= middle and middle <= last) or
        (last <= middle and middle <= first)   
    ):
        return (middle, index)
    elif (
        (middle <= first and first <= last) or
        (last <= first and first <= middle)
    ):
        return (first, 0)
    else:
        return (last, length - 1)

def quicksort(initial_array, select_pivot, comparisons = None):
    """
    Quicksort of the array using given function as a pivot selection
    strategy. It counts number of swap checks needed to sort array

    Input data is just array of numbers
    Third arguments is not needed, it is for internal swap checks calculation
    """
    # copy initial array
    array = list(initial_array)
    length = len(array)
    adjusted_comparisons = 0

    # if no comparisons it means we just started
    # so number of checks is all array length
    if comparisons is None:
        adjusted_comparisons = length - 1

    # base case
    if length <= 1:
        return (array, 0)

    pivot, index = select_pivot(array)

    # here we implement strategy in which we place pivot element
    # in the first place always
    if index != 0:
        old = array[0]
        array[0] = pivot
        array[index] = old

    # we start with i = 1, because zero-index is taken by pivot element
    i = 1

    if array[1] < pivot:
        i = 2

    for x in range(2, length):
        current = array[x]
        if current < pivot:
            array[x] = array[i]
            array[i] = current
            i = i + 1

    # change pivot and the biggest of the left subarray
    first = array[i - 1]
    array[0] = first
    array[i - 1] = pivot

    less = array[0:i - 1]
    more = array[i:]

    less_length = len(less)
    more_length = len(more)
    
    # calculate comparisons from the left
    if less_length > 1:
        adjusted_comparisons = adjusted_comparisons + less_length - 1

    # calculate comparisons from the right
    if more_length > 1:
        adjusted_comparisons = adjusted_comparisons + more_length - 1
    
    sorted_less, comparisons_from_less = quicksort(less, select_pivot, 0)
    sorted_more, comparisons_from_more = quicksort(more, select_pivot, 0)

    sorted_less.append(pivot)
    sorted_less.extend(sorted_more)

    result_sorted = sorted_less

    return (result_sorted, adjusted_comparisons + comparisons_from_less + comparisons_from_more)
