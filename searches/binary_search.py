# O(log(n)) time   | O(1) space 
array = [0, 1, 21, 33, 45, 61, 71, 72, 73, 355]
target = 355

def binary_search(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2 
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch: 
            right = middle -1
            # return binary_search_helper(array, target, left, middle - 1)
        else:
            left = middle + 1
            # return binary_search_helper(array, target, middle + 1, right)
    return -1

print(binary_search(array, target, 0, len(array)-1))