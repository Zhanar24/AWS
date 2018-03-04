 # listOfNumbers = list(range(40))
 # odd_num = []
 # even_num = []

# # for i in listOfNumbers:
# #     if i % 2 == 0:
# #         even_num.append(i)
# #     else:
# #         odd_num.append(i)
# # print("odd num: {} |nEven num: {}".format(odd_num, even_num))
#
 # while len(listOfNumbers) != 0:
 #     i = listOfNumbers[len(listOfNumbers) - 1]
 #     if i % 2 == 0:
#         even_num.append(i)
#     else:
#         odd_num.append(i)
#     listOfNumbers.pop(len(listOfNumbers) - 1)
#     print(listOfNumbers)
# print("odd num: {} \nEven num: {}".format(odd_num, even_num))

# dictionaries = {}
# list_of_names = ["Timboo", "Jamboo", "Damboo", "Hamboo"]
#
# for i in range(0, len(list_of_names)):
#     dictionaries["{}".format(i)] = list_of_names[i]
# print(list_of_names)
# print(dictionaries)
# print(dictionaries["0"])
# dictionaries['2'] = "DAMBOO"
# print(dictionaries['2'])
# print(dictionaries)
# dictionaries['StudentOne'] = 89.99
# print(dictionaries)

# dictionaries = {}
# for i in range(0, 20):
#     dictionaries['key {}'.format(i)] = i
# print(dictionaries)
# for i in dictionaries:
#     print("{}, Value: {} ".format(i, dictionaries[i]))

# live = 3
# number = '5'
#
# while live != 0:
#     print("Remaining Tries: {}".format(tries))
#     guess = input("Please")

class Dog():
    def __int__(self,breed):
        self.breed = breed
mydog = Dog(breed = "Lab")
print(mydog.breed)