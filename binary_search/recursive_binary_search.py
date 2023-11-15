def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True

        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1 :], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("target found", result)


# list comprehention
numbers = [x for x in range(10 + 1)]

# test 1
result = recursive_binary_search(numbers, 12)
verify(result)

# test 2
result = result = recursive_binary_search(numbers, 6)
verify(result)
 