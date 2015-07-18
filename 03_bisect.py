# -*- coding: utf-8 -*-

def most_left(array, number, low = 0, high = None):
    if low < 0:
        raise ValueError("Low < 0. Must be positive")
        # return -1
    if high is None:
        high = len(array)
    while low < high:
        mid = (low + high) / 2
        # print "================="
        # print "low before: " + str(low)
        # print "mid before: " + str(mid)
        # print "high before: " + str(high)
        if array[mid] < number: low = mid + 1
        else: high = mid
        # print ">>>>>>>>>>>>>>>>>"
        # print "low after: " + str(low)
        # print "mid after: " + str(mid)
        # print "high after: " + str(high)
    return low

def most_right(array, number, low = 0, high = None):
    if low < 0:
        raise ValueError("Low < 0. Must be positive")
        # return -1
    if high is None:
        high = len(array)
    while low < high:
        mid = (low + high) / 2
        # print "================="
        # print "low before: " + str(low)
        # print "mid before: " + str(mid)
        # print "high before: " + str(high)
        if number < array[mid]:
            high = mid
        else:
            low = mid + 1
        # print ">>>>>>>>>>>>>>>>>"
        # print "low after: " + str(low)
        # print "mid after: " + str(mid)
        # print "high after: " + str(high)
    return low - 1

##### start part
arr = [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 10]
num = 0
while num <= 0:
    num = int(raw_input('Enter number: '))
# print len(arr)
# print len(arr) / 2

print "Most left function:"
ml_num = most_left(arr, num)
print ml_num
print "Most right function:"
mr_num = most_right(arr, num)
print mr_num
