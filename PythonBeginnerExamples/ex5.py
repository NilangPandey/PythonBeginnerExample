name = 'Nilang Pandey'
age = 24
height = 69
weight = 183.67 # lbs
heightInFeet = height*0.0833
weightInKg = weight*0.45
weightInKgStr = "%.3f" % weightInKg
eyes = 'Dark Brown'
teeth = 'White'
hair = 'Black'
print weightInKg
print 'Let\'s talk about %s'% name
print 'He\'s %d inches tall' % heightInFeet
print 'He\'s %s kgs heavy' % weightInKgStr
print 'Actually that\'s not too heavy.'
print 'He\'s got %s eyes and %s hair.' % (eyes, hair)
print 'His teeth are usually %s depending on the coffee' % teeth

# this line is tricky try to get it right

print 'If I add %d, %d and %d I get %d.' % (age, height, weight, age+height+weight)
