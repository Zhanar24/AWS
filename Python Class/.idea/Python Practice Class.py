#string = "This is a string with bunch of words"
#print(string[8])
#print(len(string))
#for i in range(0, len(string)):
#    print(i)
#for i in string:
#     print(i)

# for i in range(0, len(string)):
#     for j in string:
#         print("This is index {} this is a char {}".format(i, string[i]))
#string = "this sample string exercercize"

#for i in range(0, len(string)):
    #if string[i] == ' ':
     #   print("This is an index {} of the character SPACE".format(i))
    #else:
     #   print("This is an index {} of the character {}".format(i, string[i]))
#list = [1, 1.4, 'hello', True]

#for i in

#list = []

#number = input("Please give a number:")
#list.append(number)
#print(list)

#list = []
#for i in range(0, 5):
 #   name = input ("Please give your name:")
#    list.append(name)
#print(list)
#for name in list:
#    print("Hello, {}".format(name))

list = []

for i in range(0, 2):
    name = input("Please give your name:")
    list.append(name)
print(list)
for name in list:
    if 'A' in name:
        print("Name has A")
    elif 'a' in name:
        print("Name has a")
    else:
        print("This name has no A or a")