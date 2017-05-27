from sys import argv
from decimal import *

script, marks, outof = argv
dmarks = Decimal(marks)
doutof = Decimal(outof)

#this function finds percentage
def percent(score, total):
    per = (score/total)*100
    print "You scored %d     marks in subject." % per

percent(dmarks, doutof)
