#Nested loops

#first line
for i in range(0,10):
    print("*", end=' ')
print("")
#second lines
for j in range(0,8):
    #inner loop
    print("*", end=' ')
    for i in range(0,8 - 0):
        print(" ", end=' ')
    print("*", end=' ')
    print("")
#last line
for i in range(0,10):
    print("*", end=' ')
