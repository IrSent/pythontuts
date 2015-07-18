# -*- coding: utf-8 -*-
# import sys
# sys.setrecursionlimit(10000)

def recursiveBinarySearch(array, number, low_index, high_index):
	if high_index < low_index:
		return -1
	else:
		mid = (low_index + high_index) / 2
		if array[mid] == number:
			return mid
		else:
			if number < array[mid]:
				high_index = mid - 1
				return recursiveBinarySearch(array, number, low_index, high_index)
			else:
				low_index = mid + 1
				return recursiveBinarySearch(array, number, low_index, high_index)

def binarySearch(array, number):
	first = 0
	last = len(array) - 1
	while first <= last:
		mid = (first + last) / 2
		if array[mid] == number:
			return mid
		else:
			if number < array[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return -1

num = -1
while num < 0:
	print "Type in number you want to find:"
	num = int(raw_input('> '))

with open('output.txt', 'r') as f:
	arr = map(int, f.readline().strip().split())

print binarySearch(arr, num)
print recursiveBinarySearch(arr, num, 0, len(arr))
