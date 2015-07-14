# -*- coding: utf-8 -*-

def bubbleSort(bubble):
    for passnum in range(len(bubble)-1,0,-1):
        for i in range(passnum):
            if bubble[i]>bubble[i+1]:
                temp = bubble[i]
                bubble[i] = bubble[i+1]
                bubble[i+1] = temp


filename = "input.txt"
myFile = open(filename)
text = myFile.read()
myFile.close()

myArray = text.split(' ')
print "There is " + str(len(myArray)) + " item in MyArray"

print "Bubble sort starts now..."

myArray = map(int, myArray)
bubbleSort(myArray)
otherText = ""

for item in myArray:
	otherText = otherText + str(item) + " "
otherText = otherText[:-1]

outputFile = open("output.txt", "w")
outputFile.write(otherText)
outputFile.close()