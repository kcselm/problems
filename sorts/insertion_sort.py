#best   O(n) time   | O(n) space 
#worst  O(n^2) time | o(n) space
array = [ 8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4,]

def sort(array):
    for i in range(1, len(array)):
        j = i 
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array

print(sort(array))