# this could take multiple arguments
def print_two(*arguments): # here * puts all the arguments in a list
    arg1, arg2, testarg = arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    print "testarg: %r" % (testarg)

#takes two parameters/arguments
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#takes one parameter/argument
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."

print_two("Nilang", "Pandey", "Eccentric")
print_two_again("Rafa", "Nadal")
print_one("Chelsea")
print_none()
