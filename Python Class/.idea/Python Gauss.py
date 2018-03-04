# Gauss sequance
# 1 + 2 + 3 + 4 + . . . +n

#Solution 1
def gauss_seq(number):
    if number > 0:
        return number + gauss_seq(number-1)
    else:
        return number

#print(gauss_seq(0)) - 0
#print(gauss_seq(1)) - 1
#print(gauss_seq(2)) - 3
#print(gauss_seq(3)) - 6
#print(gauss_seq(4)) - 10

print(gauss_seq(4))

#Solution 2 short one
n = 5
result = 0
for i in range(1, n+1):
    result += i
print(result)