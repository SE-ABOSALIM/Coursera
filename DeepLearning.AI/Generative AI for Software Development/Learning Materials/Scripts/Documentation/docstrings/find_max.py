def find_max(numbers):
    """
    Finds and returns the largest number in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int or float: The largest number in the list.
    """
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number