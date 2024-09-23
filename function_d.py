def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    return max(numbers)
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

    max_num = [0]
    for i in numbers:
        if i > max_num: 
            max_num = i
    return max_num
    print(max_value([1, 12, 2, 42, 8, 3]))
