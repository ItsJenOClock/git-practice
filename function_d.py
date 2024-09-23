def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    pass

    max_num = [0]
    for i in numbers:
        if i > max_num: 
            max_num = i
    return max_num
    print(max_value([1, 12, 2, 42, 8, 3]))
