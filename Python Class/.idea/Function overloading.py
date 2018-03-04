#Function overloading
#def hello(name='Student'):
    #print("Hello " + name)

#hello()
#hello('Jamboo')

#Task 4: Create a function which inputs 3 arguments and
# returns the least common multiple of three integers.
#Example: Common least multiple of 2, 3 and 4 is 12

#Task 5:
#Write a function which inputs 2 integers and finds
#greatest common divisor of two integers and returns it.
#Example 1: greatest common divisor of 12 and 24 is 12

#Solution for task5 and formula for 4:
num1 = 12
num2 = 24
for i in range(1, num1 * num2+1):
    if i % num1 == 0 and i % num2 == 0:
         print("Common divisible is {}".format(i))
         break
