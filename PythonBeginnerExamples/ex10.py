tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
blackslash_cat = "I'm \\ a \\ cat."
test = "This is \' test "
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print "This is a %r " % test # here %r prints raw form of a variable
print tabby_cat
print persian_cat
print blackslash_cat
print fat_cat
