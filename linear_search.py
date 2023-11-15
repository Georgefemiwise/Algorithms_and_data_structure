def linear_search(list, target):
    """
    Returns the index position of the target if found, else return None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target fount at ", index)
    else:
        print("Trget not fount in list")


# list comprehention
numbers = [x for x in range(10 + 1)]

# test 1
result = linear_search(numbers, 12)
verify(result)

# test 2
result = linear_search(numbers, 6)
verify(result)
