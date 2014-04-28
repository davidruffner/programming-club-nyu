#!/usr/bin/python

# Open a file
fo = open("input.txt", "r+")
print "Name of the file: ", fo.name
for line in fo.readlines():
    print line
# Close opend file
fo.close()
