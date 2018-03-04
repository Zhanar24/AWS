
 # class ATM:
 #     bal = 250 #bonus
 #     lim = 500
 #     def __init__(self, balance):
 #         #Attribute
 #         #self.bal = balance
 #         self.bal += balance
 #        # print("This is your balance: {}".format(balance))
 #         print("Your balance is : {}".format(balance))
 #     # Getter method - gets value out of Class/object
 #     def show_balance(self):
 #         print("This is your balance: {}".format(self.bal))
 #     # Setter method - sets value
 #     def deposit(self, amount):
 #         self.bal += amount
 #         print("${} was deposited".format(amount))
 #     def withdrawal(self, amount):
 #         if amount > self.bal:
 #             print("You don't have enough suffient")
 #         elif amount > self.lim:
 #             print("You exceed")
 #         else:
 #             self.bal -= amount
 #             print("${} was withdrawal".format(amount))
 #
 #
 #
 # chase = ATM(20000)
 # chase.show_balance()
 # chase.bal = 100000
 # chase.withdrawal(600)
 # chase.show_balance()

# chase.deposit(100)
# chase.show_balance()
# chase.withdrawal(2000) #or 1000 for not negative
# chase.show_balance()
# class ATM:
#     __bal = 250
#     __lim = 500
#
#     def __init__(self, balance):
#         # Attribute
#         self.__bal += balance
#         print("Your deposit amount is: {}".format(balance))
#
#     # Getter method - gets value out of Class/object
#     def show_balance(self):
#         print("This is your balance: {}".format(self.__bal))
#
#     # Setter method - sets value
#     def deposit(self, amount):
#         self.__bal += amount
#         print("${} was deposited".format(amount))
#
#     # Setter
#     def withdrawal(self, amount):
#         if amount > self.__bal:
#             print("You do not have sufficient funds!")
#         elif amount > self.__lim:
#             print("Withdrawal amount exceeds your daily limit")
#         else:
#             self.__bal -= amount
#             print("${} was withdrawn".format(amount))
# class Bank(ATM, CurrencyExchange):
#     def __int__(self, balance, limit):
#         ATM.__init__(self, balance, limit)
#
#     def loan(self):
#         print("Yes , we do provide loans")
#
# chase = ATM(20000)
# chase.show_balance()
# chase.withdrawal(600) #it doesn't give money make less then 600 make 500
# chase.show_balance()
#
# #Bank account

class ATM:
     __bal = 0
     __lim = 500

     def __init__(self, balance, limit):
         # Attribute
         self.__bal += balance
         self.__lim = limit
         print("Your deposit amount is: {}".format(balance))

     # Getter method - gets value out of Class/object
     def show_balance(self):
         print("This is your balance: {}".format(self.__bal))

     # Setter method - sets value
     def deposit(self, amount):
         self.__bal += amount
         print("${} was deposited".format(amount))

     # Setter
     def withdrawal(self, amount):
         if amount > self.__bal:
             print("You do not have sufficient funds!")
         elif amount > self.__lim:
             print("Withdrawal amount exceeds your daily limit")
         else:
             self.__bal -= amount
             print("${} was withdrawn".format(amount))


class CurrencyExchange:
     def transfer_money(self):
         print("Yes, we do transfer money")


class Bank(ATM, CurrencyExchange):
     def __init__(self, balance, limit):
         ATM.__init__(self, balance, limit)

     def loan(self):
         print("Yes, we do provide loans")


 # Bank account
bof = Bank(10000, 5000)
bof.show_balance()
bof.deposit(2000)
bof.show_balance()
bof.loan()
bof.transfer_money()