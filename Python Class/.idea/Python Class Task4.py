numbers = []
for i in range(0, 5):
    numbers.append(int(input("Please enter number {}: ".format(i + 1))))

sum_of_numbers = 0
for i in range(0, 5):
    sum_of_numbers += numbers[i]

print("Average numbers is: {}".format(sum_of_numbers // 5 ))