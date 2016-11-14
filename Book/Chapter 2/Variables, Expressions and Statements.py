message = 'And now for something completely different'
n = 17
pi = 3.141592653589793

#>>> 76trombones = 'big parade'
#SyntaxError: invalid syntax
#>>> more@ = 1000000
#SyntaxError: invalid syntax
#>>> class = 'Advanced Theoretical Zymurgy'
#SyntaxError: invalid syntax

miles = 26.2
print(miles * 1.61)

print(1)
x = 2
print(x)

5
x = 5
print x
y = x + 1
print y


first = 'throat'
second = 'warbler'
print first + second
print "{0}{1}".format(first, second)

print 'Spam' * 3


#The volume of a sphere with radius r is 4 / 3 r3.What is the volume of a sphere with radius 5?

pi = 3.1415926535897931
r = 5
4 / 3 * pi * r ** 3  # This is the wrong answer
392.69908169872411
r = 5.0  # Radius can be a float here as well, but is not _necessary_.
4.0 / 3.0 * pi * r ** 3  # Using floats give the correct answer
523.59877559829886


#Suppose the cover price of a book is $24.95, but bookstores get a 40 % discount.Shipping costs $3 for the
#first copy and 75 cents for each additional copy.What is the total wholesale cost for 60 copies?

#$24.95  Cost
#$9.98   Discount per book
#$14.97  Cost per book after discount
#60      Total number of books
#$898.20 Total cost not inc delivery
#$3.00   First book delivery
#59      Remaining books
#$0.75   Delivery cost for extra books
#$44.25  Total cost for extra books
#$47.25  Total Delivery cost

#$945.45 Total Bill

#This answer is wrong because 40.0 / 100.0 return wrong value 0.40000000000000002 for more info see IEEE 754
#(Standard for Floating-Point Arithmetic)

(24.95 - 24.95 * 40.0 / 100.0) * 60 + 3 + 0.75 * (60 - 1)
945.44999999999993
24.95 * 0.6 * 60 + 0.75 * (60 - 1) + 3
945.45


#If I leave my house at 6:52 am and run 1 mile at an easy pace(8:15 per mile), then 3 miles at tempo(7:12 per mile) and 1
#mile at easy pace again, what time do I get home for breakfast?
#Answer: 7:30am

#How I did it:

start = (6 * 60 + 52) * 60
easy = (8 * 60 + 15) * 2
fast = (7 * 60 + 12) * 3
finish_hour = (start + easy + fast) / (60 * 60.0)
finish_floored = (start + easy + fast) // (60 * 60)  # int() function can also be used to get integer value, but isn't taught yet.
finish_minute = (finish_hour - finish_floored) * 60
print 'Finish time was %d:%d' % (finish_hour, finish_minute)
#Finish time was 7:30

#** *ANOTHERWAY ** *
start_time_hr = 6 + 52 / 60.0
easy_pace_hr = (8 + 15 / 60.0) / 60.0
tempo_pace_hr = (7 + 12 / 60.0) / 60.0
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr - int(breakfast_hr)) * 60
breakfast_sec = (breakfast_min - int(breakfast_min)) * 60

print ('breakfast_hr', int(breakfast_hr))
print ('breakfast_min', int(breakfast_min))
print ('breakfast_sec', int(breakfast_sec))
