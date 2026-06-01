# Without documentation
def bubble_sort_no_doc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# With inline documentation
def bubble_sort_inline_doc(arr):
    # Get the number of elements in the array
    n = len(arr)

    # Outer loop controls how many passes we make through the array
    for i in range(n):

        # Inner loop compares adjacent elements
        # After each full pass, the largest unsorted element moves to the end
        # So we reduce the range by i because the last i elements are already sorted
        for j in range(0, n - i - 1):

            # If the current element is greater than the next element,
            # swap them so the smaller element comes first
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the sorted array
    return arr

# With docstring documentation
def bubble_sort_docstring_doc(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Bubble Sort repeatedly compares adjacent elements and swaps them
    if they are in the wrong order. After each pass, the largest
    remaining unsorted element moves to its correct position.

    Args:
        arr (list): The list of comparable elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """

    # Get the number of elements in the array
    n = len(arr)

    # Perform multiple passes through the array
    for i in range(n):

        # Compare adjacent elements up to the unsorted part of the array
        for j in range(0, n - i - 1):

            # Swap elements if they are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the sorted array
    return arr