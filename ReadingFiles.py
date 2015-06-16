__author__ = 'Dario Hermida'
from sys import argv

script, filename, create = argv
count = 0
print ("Opening the file:")
target = open(filename, 'r')
output = open(create, 'w')
writing = True

print ("I'm going to read from the target file:")

while count < 93:
    s = target.readline()
    if "League Rules" in s: writing = not writing
    if writing: output.write(s)
    count += 1

print ("And finally, we close it")

target.close()
output.close()
