grade = int(input( "Please enter your grade (1-100):"))

if grade > 100:
    print ("Your grade is A")
elif grade > 80:
    print ("Your grade is B")
elif grade > 70:
    print ("Your grade is C")
elif grade > 60:
    print ("Your grade is D")
else:
    print ("Your grade is F")