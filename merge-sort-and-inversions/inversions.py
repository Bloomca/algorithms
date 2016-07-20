def merge(tuple1, tuple2):
    """
    Merging subroutine of merge sort

    We have two sorted arrays, which we have to merge
    into one sorted array

    Also, we calculate number of inversions, so we keep track
    of them during merging too, adding to the existing number

    Each tuple has structure (sorted_array, number_of_inversions)
    """
    arr1 = tuple1[0]
    arr2 = tuple2[0]
    firstArrayLength = len(arr1)
    secondArrayLength = len(arr2)
    result = []
    firstIndex = 0
    secondIndex = 0
    inversions = tuple1[1] + tuple2[1]
    for i in range(0, firstArrayLength + secondArrayLength):
        # if we took all from the first array
        if firstIndex == firstArrayLength:
            result.append(arr2[secondIndex])
            secondIndex = secondIndex + 1
        # if we took everything from the second array
        elif secondIndex == secondArrayLength:
            result.append(arr1[firstIndex])
            firstIndex = firstIndex + 1
        # if the next number is from the first array
        # no need to increase inversions
        elif (arr1[firstIndex] <= arr2[secondIndex]):
            result.append(arr1[firstIndex])
            firstIndex = firstIndex + 1
        elif (arr2[secondIndex] < arr1[firstIndex]):
            result.append(arr2[secondIndex])
            secondIndex = secondIndex + 1
            # we have to increase number of inversions by all left
            # elements in the left array, because they are guaranteed
            # higher than this element
            inversions = inversions + firstArrayLength - firstIndex

    return (result, inversions)

def mergeSort(arr):
    """
    Partitioning subroutine of merge sort
    Also, it counts number if inversions
    (though they are counted in merging subrouting)
    """
    arrayLength = len(arr)
    # base case: same array, 0 inversions
    if arrayLength == 1:
        return (arr, 0)

    # just separating into two parts of the same size
    separator = arrayLength / 2
    leftArr = arr[:separator]
    rightArr = arr[separator:]

    return merge(mergeSort(leftArr), mergeSort(rightArr))
