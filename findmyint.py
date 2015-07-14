# -*- coding: utf-8 -*-
#
#def binarySearch(array, number):
#    if len(array) == 0:
#        return False
#    else:
#        mid = len(array) // 2
#        if array[mid] == number:
#          return True
#        else:
#          if number < array[mid]:
#            return binarySearch(array[:mid], number)
#          else:
#            return binarySearch(array[mid+1:], number)
#
def binarySearch(array, number):
	first = 0
	last = len(array) - 1
	found = False
	howManyTimes = 0
	while first <= last and not found:
		mid = (first + last) // 2
		howManyTimes += 1
		print howManyTimes
		if array[mid] == number:
			howManyTimes += 1
			print howManyTimes
			print mid
			found = True
		else:
			if number < array[mid]:
				last = mid - 1
				howManyTimes += 1
				print howManyTimes
			else:
				first = mid + 1
				howManyTimes += 1
				print howManyTimes
	return found

num = -1
while num < 0:
	print "Type in number you want to find:"
	num = int(raw_input('> '))

with open('output.txt', 'r') as f:
	arr = map(int, f.readline().strip().split())

print binarySearch(arr, num)
