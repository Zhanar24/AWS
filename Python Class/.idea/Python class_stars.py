for j in range(0,10):
    #inner loop
    for k in range(j,10):
        print("", end=' ')

    for i in range(0, j+1):
        print("*", end=' ')
    print("")
#Outer loop
for j in range(0, 10):
    #inner loop
    for k in range(0, j+1):
        print("", end=' ')

    for i in range(j, 10):
        print("*", end=' ')
    print("")