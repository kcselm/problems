arr = [4, 3, 23, -5, 12]

def smallest(arr):
    #fastest
    # return min(arr)
    min = arr[0]
    for i in arr[1:]:
        if i < min:
            min = i
    return min


print(smallest(arr))