numbers = [123, 54, 2, -1, 43, 22333, 1, 99, 883423]
numbers_len = len(numbers)
max_number = numbers[0]

for i in range(1, numbers_len):
    if max_number < numbers[i]:
        max_number = numbers[i]

print("This is the largest: {}".format(max_number))

numbers_len = len(numbers)
min_number = numbers[0]

for i in range(1, numbers_len):
    if min_number > numbers[i]:
        min_number = numbers[i]


#print(max(numbers)) short cut
#print(min(numbers))

print("This is lowest: {}".format(min_number))
