def binary_search(list, target):
    """
    Purpose: list
    """
    # get the first and last
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint

        elif list[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1
    return None

# verify if algorithm
def verify(index):
    if index is not None:
        print("Target fount at ", index)
    else:
        print("Trget not fount in list")


# list comprehention
numbers = [x for x in range(10 + 1)]

# test 1
result = binary_search(numbers, 12)
verify(result)

# test 2
result = binary_search(numbers, 6)
verify(result)
