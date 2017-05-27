from sys import argv

script, textfile = argv
print textfile

txt = open(textfile, 'w')
print "Enter in following lines to write in text file"

line1 = raw_input("line1 ")
line2 = raw_input("line2 ")
line3 = raw_input("line3 ")

finalLines = "%s\n %s\n %s\n" % (line1, line2, line3)

txt.write(finalLines)
txt.close()

txt2 = open(textfile)
print "This is new content."
print txt2.read()
