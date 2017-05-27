# imports arguments from system

from sys import argv
#initializing the name of argument variables
script, filename = argv
# opens the file specified in argument variable
# stores the file type object named 'txt'
txt = open(filename)
#print txt
# prints the name of file you want to open
print "Here's your file %r " % filename

# read from the file object txt and prints the content in file
print txt.read()

# Again opening and reading file
# this time with raw_input

print "Type the filename again: "

# raw_input will take the name of file to be read
file_again = raw_input("> ")

# txt_again will store the file object returned by open
txt_again = open(file_again)

# prints the content of file by reading it
print txt_again.read()
