__author__ = 'Dario Hermida'
from sys import argv

script, filename = argv

print ("We're going to erase {}.".format(filename))
print ("If you don't want that, hit Ctrl-C (caretC).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file:")
target = open(filename, 'w')
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print ("I'm going to write these on the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it")

target.close()
