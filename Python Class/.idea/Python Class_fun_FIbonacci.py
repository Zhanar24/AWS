#Task 3
#Write a function which will calculate fibonacci sequence
#Example:
#fib(7)
# 1 1 2 3 5 8 13 21 . . .
#n = (n-1) + (n-2)
def fibonacci(number):
    n1 = 1
    n2 = 1
    fib = 1

    for i in range (1, number+1):
        if i == 1:
            pass
        elif i == 2:
            pass
        else:
            n2 = n1
            n1 = fib
            fib = n1 + n2
        print(fib)
fibonacci(100)
