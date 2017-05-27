#storing the format specifier %r in a variable
formatter = "%r %r %r %r"
'''
%r basically formats all type of characters, be it boolean,
string, decimal,
'''
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type upright.",
    "But it didn\'t sing.",
    "So I said goodnight."
)
