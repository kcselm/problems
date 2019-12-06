"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""
def find_outlier(integers):
    for i in map(int, (range(integers[0:3]))):
        i % 2
        return i
    
print(find_outlier([2, 4, 6, 8, 10, 3]))