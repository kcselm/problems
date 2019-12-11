#best:   O(n^2) time | O(1) space
#worst:  O(n^2) time | O(1) space
array = [ 8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4,]

def sort(array):
    currentIndex = 0
    while currentIndex < len(array) - 1:
        smallestIndex = currentIndex
        for i in range(currentIndex + 1, len(array)):
            if array[smallestIndex] > array[i]:
                smallestIndex = i 
        array[currentIndex], array [smallestIndex] = array[smallestIndex], array[currentIndex]
        currentIndex += 1
    return array

print(sort(array))

