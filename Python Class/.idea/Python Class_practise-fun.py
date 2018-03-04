#Task1
#write a function which calculates factorial of a number
#Functions has to accept a single argument, integer

#Factorial formula
#Factorial of n is
#n! = 1 * 2 * 3 ... n
def factorial(number):
    result = 1
    for i in range(1, number+1):
     result = result * i

    print("Factorial of {} is {}".format(number, result))

for i in range(1, 11):
    factorial(i)

