print 'hello world'
print type(2)
print type(42.0)
print type('hello world')
print type ('2')

print 1,000,000


#If you run a 10 kilometer race in 42 minutes 30 seconds, what is your average time per mile?
# What is your average speed in miles per hour? (Hint: there are about 1.61 kilometers in a mile.)

10 / 1.61 # Convert kilometers to miles
6.2111801242236018
(42 * 60) + 42 # Convert time to seconds
2562
2562 / 6.2111801242236018 # what is your average time (seconds) per mile
412.482
412.482 / 60 # what is your average time (minutes) per mile
6.874700000000001
60 / 6.874700000000001 # Miles per hour
8.727653570337614

#How about
10 / 42.5 # avg kilometers per minute
0.23573785950023574
0.23573785950023574*60 # kilometers per hour
14.144271570014144
14.144271570014144 / 1.61 # convert to M.P.H
8.785261844729282

#or a one-liner
(10 / 1.61) / (42.5 / 60)   # (distance in miles) / (time in hours)
8.567144998929106         # miles/hour

#making it 'pretty' & exploring how print works....

print round((10 / 1.61) / (42.5 / 60), 2), 'mph'    # (distance in miles)/(time in hours) rounded to 2 places
#8.77 mph

