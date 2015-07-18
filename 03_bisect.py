# -*- coding: utf-8 -*-

def most_left(array, number, low = 0, high = None):
    if low < 0:
        return -1
    if high is None:
        high = len(array)
    while low < high:
        mid = (low + high) / 2
        if array[mid] < number: low = mid + 1
        else: high = mid
    return low

def most_right(array, number, low = 0, high = None):
    if low < 0:
        return -1
    if high is None:
        high = len(array)
    while low < high:
        mid = (low + high) / 2
        if number < array[mid]:
            high = mid
        else:
            low = mid + 1
    return low - 1

##### start part
arr = [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 10]
num = 0
while num <= 0:
    num = int(raw_input('Enter number: '))

print "Most left function:"
ml_num = most_left(arr, num)
print ml_num
print "Most right function:"
mr_num = most_right(arr, num)
print mr_num
